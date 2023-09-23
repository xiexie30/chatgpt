# 使用文心一言进行单轮对话
import requests
import json

API_KEY = ""
SECRET_KEY = ""

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

def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    
    while True:
        msgs.append_userMsg(input("> "))

        payload = json.dumps({
            "messages": msgs.msgs
        })
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(response.text)
        if "result" not in result:
            print(response.text)
        else:
            print(result["result"])
            msgs.append_assistantMsg(result["result"])
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()
