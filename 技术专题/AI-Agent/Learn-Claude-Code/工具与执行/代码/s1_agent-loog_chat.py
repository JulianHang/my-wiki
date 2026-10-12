import json
import os
import subprocess

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
model_id = os.getenv("OPENAI_MODEL_ID")

client = OpenAI(api_key = api_key, base_url = base_url)

# Claude Code 的运行环境和工具定义放在全局，便于复用和扩展。
ENVIRONMENT_PROMPT = (
    "当前是 Windows 系统，bash 工具通过 cmd.exe 执行；请使用 cmd.exe 语法，不要使用 Unix Bash 或 PowerShell 语法"
    if os.name == "nt"
    else "当前是类 Unix 系统，bash 工具通过系统 Shell 执行"
)
SYSTEM_PROMPT = (
    f"你是一个代码代理，当前工作目录是 {os.getcwd()}。"
    f"运行环境：{ENVIRONMENT_PROMPT}。"
    "请使用 bash 工具检查和修改工作区；直接执行任务，不要只解释方案。"
)


def run_bash(command: str) -> str:
    """执行脚本"""
    try:
        r = subprocess.run(command, capture_output=True, shell=True, cwd=os.getcwd(), text=True, timeout=120, errors="replace")
        out = (r.stdout + r.stderr).strip()
        return out[:50000] if out else "没有输出"
    except Exception as e:
        return f"脚本执行错误：{e}"


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "run_bash",
            "description": "Run a shell command in the current workspace.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The shell command to execute."
                    }
                },
                "required": ["command"],
                "additionalProperties": False
            }
        }
    }
]

TOOL_HANDLERS = {
    "run_bash": run_bash
}


def _parse_tool_params(raw_arguments: str) -> dict:
    try:
        args = json.loads(raw_arguments)
    except Exception:
        return {}

    return args if isinstance(args, dict) else {}


def agent_loop(query: str) -> list:
    messages = [{"role": "system", "content":SYSTEM_PROMPT}, {"role": "user", "content": query}]
    round = 0

    while True:
        response = client.chat.completions.create(messages=messages, model = model_id, max_tokens = 8000, tools= TOOLS)
        msg = response.choices[0].message
        assistant_content = msg.content or ""
        tool_calls = msg.tool_calls or []

        # OpenAI chat版本的格式，要把响应内容在告诉大模型
        assistant_entry: dict = {"role": "assistant", "content": assistant_content}
        if not tool_calls:
            break

        assistant_entry["tool_calls"] = [
            {
                "id": tool_call.id,
                "type": tool_call.type,
                "function": {
                    "name": tool_call.function.name,
                    "arguments": tool_call.function.arguments
                }
            }
            for tool_call in tool_calls
        ]

        messages.append(assistant_entry)
        # 开始调用工具
        print("=" * 20, f"🔎 第 {round + 1} 轮开始", "=" * 20)

        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            tool_params = _parse_tool_params(tool_call.function.arguments)
            output = TOOL_HANDLERS[tool_name](**tool_params)
            print(f"💡 工具调用 -> {tool_name}, 入参 -> {tool_params}, 输出 -> {output[:200]}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": output
            })

        print()
        round += 1

    return messages



if __name__ == '__main__':
    print("1️⃣ 学习OpenAI Chat - Agent Loop")
    query = "请帮我创建hello-world-oc.py文件"
    reply = agent_loop(query)
    r = reply[-1]["content"]
    if isinstance(r, str):
        print(f"🔊 任务 -> {r}")
    print(f"✅ 练习通过。")
