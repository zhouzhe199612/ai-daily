#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试HTML生成功能
"""

from datetime import datetime
import os

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "AI日报.html")

print("当前目录: " + current_dir)
print("HTML文件路径: " + html_path)

# 测试数据
test_news = [
    {
        'title': '测试新闻1',
        'url': 'https://example.com/1',
        'summary': '这是测试新闻的摘要',
        'category': '【大模型动态】',
        'source': '测试来源'
    },
    {
        'title': '测试新闻2',
        'url': 'https://example.com/2',
        'summary': '这是测试新闻的摘要2',
        'category': '【产品与商业化】',
        'source': '测试来源2'
    }
]

# 生成HTML
big_model_html = ""
for news in [n for n in test_news if '大模型' in n['category']]:
    big_model_html += f"""
    <div class="news-item">
        <h3><a href="{news['url']}" target="_blank">{news['title']}</a></h3>
        <p class="summary">{news['summary']}</p>
        <p class="source">来源: {news.get('source', '未知')}</p>
    </div>
    """

product_html = ""
for news in [n for n in test_news if '商业化' in n['category']]:
    product_html += f"""
    <div class="news-item">
        <h3><a href="{news['url']}" target="_blank">{news['title']}</a></h3>
        <p class="summary">{news['summary']}</p>
        <p class="source">来源: {news.get('source', '未知')}</p>
    </div>
    """

final_html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>AI日报 - {datetime.now().strftime('%Y年%m月%d日')}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .news-item {{ margin-bottom: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
        .source {{ color: #999; font-size: 12px; }}
    </style>
</head>
<body>
    <h1>AI日报 - {datetime.now().strftime('%Y年%m月%d日')}</h1>
    <div class="category">
        <h2>【大模型动态】</h2>
        {big_model_html}
    </div>
    <div class="category">
        <h2>【产品与商业化】</h2>
        {product_html}
    </div>
</body>
</html>
"""

# 写入文件
try:
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print("AI日报.html 生成成功！")
    print("文件位置: " + html_path)
    
    # 验证文件是否存在
    if os.path.exists(html_path):
        print("文件验证成功，大小: " + str(os.path.getsize(html_path)) + " 字节")
    else:
        print("文件未找到")
except Exception as e:
    print("生成失败: " + str(e))
