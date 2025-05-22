import json
import requests
import random

def generate_code():
    """生成4位随机验证码"""
    return ''.join(random.choices('0123456789', k=4))

def send_code(code: str, phone: str):
    """发送验证码并保存"""
    url = 'https://api-v4.mysubmail.com/sms/send'

    headers = {
        'content-type': 'application/json'
    }

    data = {
        'appid': '98850',
        'to': phone,
        'content': f"【昆明软源科技有限公司】验证码 —— {code}",
        'signature': 'f4c3a8afa4a0856f6a1af846591c87c7'
    }

    try:
        response = requests.post(
            url=url,
            headers=headers,
            data=json.dumps(data)
        )

        # 检查响应状态码
        response.raise_for_status()

        # 返回JSON响应
        return response.json()

    except requests.RequestException as e:
        return f"发送短信时发生错误: {e}"