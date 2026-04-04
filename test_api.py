#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 测试 API_KEY
API_KEY = os.getenv('API_KEY', "sk-8c75fa43fc9d4b00b730a521c2fcacd6")
API_URL = os.getenv('API_URL', "https://api.deepseek.com/chat/completions")

print(f"API_KEY: {API_KEY}")
print(f"API_URL: {API_URL}")
print(f"API_KEY 长度: {len(API_KEY)}")
print(f"API_KEY 非空: {bool(API_KEY)}")

# 测试导入
print("\n测试导入模块...")
try:
    import requests
    import feedparser
    from bs4 import BeautifulSoup
    print("✓ 所有模块导入成功")
except Exception as e:
    print(f"✗ 导入失败: {e}")

# 测试网络连接
print("\n测试网络连接...")
try:
    response = requests.get("https://www.baidu.com", timeout=5)
    print(f"✓ 网络连接正常，状态码: {response.status_code}")
except Exception as e:
    print(f"✗ 网络连接失败: {e}")