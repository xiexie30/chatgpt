import openai
import json

# openai.api_base = "https://api.chatanywhere.com.cn/v1"
# openai.api_key = "sk-" 
openai.api_key = "sk-"

class msg:
    def __init__(self) -> None:
        self.msgs = [{"role": "user", "content": "你是我的助手，你叫小爱同学，我叫你干嘛你就干嘛"}, 
                {"role": "assistant", "content": "好的，你有什么要求都可以跟我说。(*￣︶￣)"}]
        self.msgSize = 0

    def append_userMsg(self, content):
        message = {"role": "user", "content": content}
        self.msgs.append(message)
        self.msgSize += 1

    def append_assistantMsg(self, content):
        message = {"role": "assistant", "content": content}
        self.msgs.append(message)
        self.msgSize += 1
        if (self.msgSize > 30):
            del self.msgs[3]
            del self.msgs[2]
            self.msgSize -= 2

msgs = msg()

while True:
  msgs.append_userMsg(input("> "))
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=msgs.msgs
  )
  result = completion["choices"][0]["message"]["content"]
  # result = json.loads(completion)
  print(result)
  msgs.append_assistantMsg(result)