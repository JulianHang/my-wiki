from openai import OpenAI

class OpenAICompatibleClient:
    """
    一个用于调用任何兼容OpenAI接口的LLM服务的客户端
    """

    def __init__(self, model: str, api_key: str, base_url: str):
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def generate(self, prompt: str, system_prompt: str) -> str:
        """调用LLM API来生成回应"""
        print("正在调用大语言模型...")
        try:
            messages = [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt}
            ]
            # 实际上接口规范是OpenAI定义的，但是LLM模型仍然是各自厂商的
            response = self.client.chat.completions.create(model=self.model, messages=messages, stream=False)
            answer = response.choices[0].message.content
            print('大语言模型响应成功')
            return answer
        except Exception as e:
            print(f'调用LLM API时发生错误：{e}')
            return "错误：调用语言模型服务时出错。"