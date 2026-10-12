
import os
import subprocess
from pathlib import Path
import re
from random import choices

from anthropic import Anthropic
from dotenv import load_dotenv


# 加载环境变量
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
base_url = os.getenv("ANTHROPIC_BASE_URL")
model_id = os.getenv("ANTHROPIC_MODEL_ID")

WORKDIR = Path.cwd()

client = Anthropic(api_key = api_key, base_url = base_url)

# Claude Code 的运行环境和工具定义放在全局，便于复用和扩展。
ENVIRONMENT_PROMPT = (
    "当前是 Windows 系统，bash 工具通过 cmd.exe 执行；请使用 cmd.exe 语法，不要使用 Unix Bash 或 PowerShell 语法，并优先使用专门的文件工具进行文件操作"
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


def safe_path(p: str) -> Path:
    """获取绝对路径"""
    # resolve是将路径规范化为绝对路径
    path = (WORKDIR / p).resolve()
    # is_relative_to是判断path方法是否是WORKDIR的子目录
    if not path.is_relative_to(WORKDIR):
        raise ValueError(f"路径超出工作目录：{p}")
    return path

# limit要设置默认值，否则就是必填参数
def run_read(path: str, limit: int | None = None) -> str:
    """读取文件内容"""
    try:
        lines = safe_path(path).read_text(encoding="utf-8").splitlines()
        if limit and limit < len(lines):
            lines = lines[:limit] + [f"... ({len(lines) - limit} more lines)"]
        return "\n".join(lines)
    except Exception as e:
        return f"读取文件错误：{e}"


def run_write(path: str, content: str) -> str:
    """写入文件"""
    try:
        file_path = safe_path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
        return f"文件写入成功：{path}"
    except Exception as e:
        return f"写入文件错误：{e}"

def run_edit(path: str, old_text: str, new_text: str) -> str:
    try:
        file_path = safe_path(path)
        text = file_path.read_text(encoding="utf-8")
        if old_text not in text:
            return f"在 {path} 文件中未发现字符串"

        file_path.write_text(text.replace(old_text, new_text, 1), encoding="utf-8")
        return f"文件编辑成功：{path}"
    except Exception as e:
        return f"编辑文件错误：{e}"

def run_glob(pattern: str) -> str:
    """搜索文件"""
    import glob as g
    try:
        # 使用集合推导式可以去重
        matches = sorted({match for match in g.glob(pattern, root_dir=WORKDIR, recursive=True) if (WORKDIR / match).resolve().is_relative_to(WORKDIR)})
        shown = matches[:200]
        if len(matches) > 200:
            shown.append("... (more matches omitted; narrow the pattern)")
        return "\n".join(shown) if shown else "未找到匹配项"
    except Exception as e:
        return f"文件搜索错误：{e}"


TOOLS = [
    {
        "name": "bash",
        "description": "Run a shell command.",
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string"
                }
            },
            "required": [
                "command"
            ]
        }
    },

    {
        "name": "read_file",
        "description": "Read file contents.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string"
                },
                "limit": {
                    "type": "integer"
                }
            },
            "required": [
                "path"
            ]
        }
    },

    {
        "name": "write_file",
        "description": "Write content to a file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string"
                },
                "content": {
                    "type": "string"
                }
            },
            "required": [
                "path",
                "content"
            ]
        }
    },

    {
        "name": "edit_file",
        "description": "Replace exact text in a file once.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string"
                },
                "old_text": {
                    "type": "string"
                },
                "new_text": {
                    "type": "string"
                }
            },
            "required": [
                "path",
                "old_text",
                "new_text"
            ]
        }
    },

    {
        "name": "glob",
        "description": "Find files matching a glob pattern; ** matches recursively.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {
                    "type": "string"
                }
            },
            "required": [
                "pattern"
            ]
        }
    },
]

TOOL_HANDLERS = {
    "bash": run_bash,
    "read_file": run_read,
    "write_file": run_write,
    "edit_file": run_edit,
    "glob": run_glob,
}

DENY_LIST = ["rm -rf /", "sudo", "shutdown", "reboot", "mkfs", "dd if=", "> /dev/sda"]
DESTRUCTIVE_COMMAND_WORD = re.compile(
    r"(?i)(?:^|[;&|()\n])\s*(?:rm|del)(?=\s|$|[;&|()])"
)
DESTRUCTIVE = ["rm ", "> /etc/", "chmod 777"]

# 定义钩子的时机点
HOOKS = {"UserPromptSubmit": [], "PreToolUse": [], "PostToolUse": [], "Stop": []}

# 添加钩子函数
def register_hook(event: str, callback):
    HOOKS[event].append(callback)

# 触发钩子调用
def trigger_hook(event: str, *args):
    for callback in HOOKS[event]:
        result = callback(*args)
        if result is not None:
            return result
    return None

def contains_destructive_command(command: str) -> bool:
    return bool(DESTRUCTIVE_COMMAND_WORD.search(command))


# 权限钩子
def permission_hook(block):
    if block.name == 'bash':
        command = block.input.get('command', '')
        for pattern in DENY_LIST:
            if pattern in command:
                return "Permission denied by deny list"

        if contains_destructive_command(command) or any(kw in command for kw in DESTRUCTIVE):
            print(f"工具：{block.name}({block.input})，破坏性命令，校验权限，请审批。")
            choice = input("是否允许执行? [Y/N]\n").strip().lower()
            if not choice in ('y', 'yes', 'Y'):
                return "Permission denied by user"

    if block.name in ("read_file", "write_file", "edit_file"):
        path = block.input.get("path", "")
        if not (WORKDIR / path).resolve().is_relative_to(WORKDIR):
            print(f"工具：{block.name}({block.input})，访问工作区外空间，校验权限，请审批。")
            choice = input("   Allow? [y/N] ").strip().lower()
            if choice not in ("y", "yes"):
                return "Permission denied by user"
    return None


def log_hook(block):
    # 打印每个工具调用的信息
    args_preview = str(list(block.input.values())[:2])[:60]
    print(f"\033[90m[HOOK] {block.name}({args_preview})\033[0m")
    return None


def large_output_hook(block, output):
    if len(str(output)) > 100000:
        print(f"\033[33m[HOOK] Large output from {block.name}: {len(str(output))} chars\033[0m")
    return None


# UserPromptSubmit hook: log user input before it reaches the LLM
def context_inject_hook(query: str):
    print(f"\033[90m[HOOK] UserPromptSubmit: working in {WORKDIR}\033[0m")
    return None

# Stop hook: print summary when loop is about to exit
def summary_hook(messages: list):
    # 打印工具调用的数量
    tool_count = sum(1 for m in messages
                     for b in (m.get("content") if isinstance(m.get("content"), list) else [])
                     if isinstance(b, dict) and b.get("type") == "tool_result")
    print(f"\033[90m[HOOK] Stop: session used {tool_count} tool calls\033[0m")
    return None


register_hook("UserPromptSubmit", context_inject_hook)
register_hook("PreToolUse", permission_hook)
register_hook("PreToolUse", log_hook)
register_hook("PostToolUse", large_output_hook)
register_hook("Stop", summary_hook)


# 循环体
def agent_loop(query: str) -> list:

    messages = [{"role": "user", "content": query}]
    round = 0

    while True:
        response = client.messages.create(system = SYSTEM_PROMPT, model = model_id, messages = messages, max_tokens = 8000, tools = TOOLS)
        # 模型并不知道此次对话返回了什么内容，加入这个消息是要在下一轮中告诉模型任务的执行进度，与后面添加的工具结果形成一一对应，这个是必须项，否则模型可能会以为工具没执行
        messages.append({"role": "assistant", "content": response.content})

        tool_use_list = [block for block in response.content if block.type == "tool_use"]
        if not tool_use_list:
            force = trigger_hook("Stop", messages)
            if force:
                messages.append({"role": "user", "content": force})
                continue
            break

        reply_llm = []
        print("=" * 20, f"🔎 第 {round + 1} 轮开始", "=" * 20)
        for tool_use_block in tool_use_list:
            blocked = trigger_hook("PreToolUse", tool_use_block)
            if blocked:
                reply_llm.append({"type": "tool_result", "tool_use_id": tool_use_block.id,
                                "content": str(blocked)})
                continue

            tool_name = tool_use_block.name
            tool_params = tool_use_block.input
            output = TOOL_HANDLERS[tool_name](**tool_params)
            print(f"💡 工具调用 -> {tool_name}, 入参 -> {tool_params}, 输出 -> {output[:200]}")

            trigger_hook("PostToolUse", tool_use_block, output)  # s04: post hook

            # 工具执行完的结果要告知给模型，以便它可以继续后面的执行动作，这个是必须项
            reply_llm.append({
                "type": "tool_result",
                "tool_use_id": tool_use_block.id,
                "content": output
            })

        messages.append({"role": "user", "content": reply_llm})
        print()
        round += 1


    return messages




if __name__ == '__main__':
    print("4️⃣ 学习ClaudeCode - Hook")
    query = "请帮我创建test.txt文件"
    trigger_hook("UserPromptSubmit", query)
    reply = agent_loop(query)
    r = reply[-1]["content"]
    if isinstance(r, list):
        for block in r:
            if getattr(block, "type", None) == "text":
                print(f"🔊 任务 -> {block.text}")
                break
    print(f"✅ 练习通过。")

