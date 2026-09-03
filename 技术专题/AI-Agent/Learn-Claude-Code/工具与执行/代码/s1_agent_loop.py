import os
import subprocess
from dotenv import load_dotenv
from anthropic import Anthropic
from typing import List, Dict, Any

# 加载.env文件
load_dotenv()

"""
name、description、input_schema 是Claude Code API声明工具的固定格式
input_schema内部的格式是标准的JSON Schema的格式，不是固定的
"""

TOOLS = [{
    "name": "bash",
    "description": "Run a shell command.",
    "input_schema": {
        "type": "object",
        "properties": {"command": {"type": "string"}},
        "required": ["command"],
    },
}]


SYSTEM=f"你是 {os.getcwd()} 的一名编码代理。使用 bash 完成任务。行动起来，无需解释。"

class ClaudeCodeLLM:

    def __init__(self, api_key: str = None, base_url: str = None, model_id: str = None):
        self.model_id = model_id or os.getenv("MODEL_ID")
        api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        base_url = base_url or os.getenv("ANTHROPIC_BASE_URL")

        if not all([self.model_id, api_key, base_url]):
            raise ValueError("model_id、api_key、base_url都是必填项")

        self.client = Anthropic(api_key=api_key, base_url=base_url)


    def think(self, messages: List[Dict[str, Any]], system: str, tools: List[Dict[str, Any]], max_token: int = 1000):

        print(f"🧠 正在调用 {self.model_id} 模型...")
        try:
            response = self.client.messages.create(model=self.model_id, messages=messages, system=system, tools=tools, max_tokens=max_token)
            print("✅ 大语言模型响应成功:")

            collected_content = []
            for chunk in response.content:
                if not chunk:
                    continue
                collected_content.append(chunk)

            print()
            return collected_content
        except Exception as e:
            print(f"❌ 调用LLM API时发生错误: {e}")
            return None


# -- Tool execution --
def run_bash(command: str) -> str:
    dangerous = ["rm -rf /", "sudo", "shutdown", "reboot", "> /dev/"]
    if any(d in command for d in dangerous):
        return "错误: 危险命名已阻止"
    try:
        r = subprocess.run(command, shell=True, cwd=os.getcwd(),
                           capture_output=True, text=True, errors="replace", timeout=120)
        out = (r.stdout + r.stderr).strip()
        return out[:50000] if out else "(no output)"
    except subprocess.TimeoutExpired:
        return "错误: 超时 (120s)"
    except (FileNotFoundError, OSError) as e:
        return f"错误: {e}"


def agent_loop(messages: List[Dict[str, Any]], system: str, tools: List[Dict[str, Any]]) -> List:
    while True:
        content = client.think(messages, system, tools)
        if not content:
            break
        # 添加LLM返回的响应到消息中, 继续发问
        messages.append({"role": "assistant", "content": content})
        # 获取工具调用列表
        tool_calls = [block for block in content if block.type == 'tool_use']
        if not tool_calls:
            break

        # 收集工具执行的结果，将其在反馈给LLM
        results = []
        for block in tool_calls:
            print(f"\033[33m$ {block.input['command']}\033[0m")
            output = run_bash(block.input["command"])
            print(output[:200])
            results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": output,
            })
        messages.append({"role": "user", "content": results})

    return messages



client = ClaudeCodeLLM()

if __name__ == '__main__':
    print("s01: Agent Loop")
    print("Enter a question, press Enter to send. Type q to quit.\n")

    query = input("\001\033[36m\002s01 >> \001\033[0m\002")
    init_messages = [{"role": "user", "content": query}]

    agent_loop(init_messages, SYSTEM, TOOLS)
    response_content = init_messages[-1]["content"]
    # 打印出最终的结果
    if isinstance(response_content, list):
        for r_block in response_content:
            if getattr(r_block, "type", None) == 'text':
                print("结论：", r_block.text)

    print()