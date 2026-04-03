#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import sys

# 设置输出编码
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

API_KEY = os.getenv('API_KEY', "sk-8c75fa43fc9d4b00b730a521c2fcacd6")
API_URL = os.getenv('API_URL', "https://api.deepseek.com/chat/completions")

print("测试AI调用...")
print(f"API_KEY: {API_KEY[:10]}...")
print(f"API_URL: {API_URL}")

try:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": "你好，请回复'测试成功'"
            }
        ],
        "temperature": 0.7
    }
    
    print("正在发送请求...")
    response = requests.post(API_URL, headers=headers, json=data, timeout=30)
    print(f"响应状态码: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        content = result['choices'][0]['message']['content']
        print(f"AI回复: {content}")
        print("✓ AI调用成功！")
    else:
        print(f"✗ 请求失败: {response.text}")
        
except Exception as e:
    print(f"✗ 调用失败: {e}")
