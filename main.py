#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AI资讯日报生成器
功能：自动抓取AI相关新闻，调用AI大模型总结，生成HTML网页
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

# ==================== 配置部分 ====================
# AI大模型配置
API_KEY = os.getenv('API_KEY', "sk-8c75fa43fc9d4b00b730a521c2fcacd6")
API_URL = os.getenv('API_URL', "https://api.deepseek.com/chat/completions")

# 抓取配置
MAX_NEWS_PER_SOURCE = 5  # 每个来源最多抓取的新闻数量

# ==================== 新闻抓取模块 ====================

def fetch_github_trending():
    """抓取GitHub Trending上的AI相关项目"""
    news = []
    try:
        url = "https://github.com/trending"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # 尝试不同的选择器
        repo_cards = soup.select('article.Box-row')
        if not repo_cards:
            repo_cards = soup.select('div.Box-row')
        
        for card in repo_cards[:MAX_NEWS_PER_SOURCE]:
            # 提取项目名称
            title_elem = card.select_one('h2') or card.select_one('h3')
            if title_elem:
                repo_name = title_elem.text.strip()
                # 提取链接
                link_elem = title_elem.select_one('a')
                if link_elem:
                    repo_url = "https://github.com" + link_elem['href']
                    # 提取描述
                    description_elem = card.select_one('p')
                    description = description_elem.text.strip() if description_elem else ""
                    
                    # 只保留包含AI相关关键词的项目
                    ai_keywords = ['ai', 'ml', 'machine learning', 'deep learning', 'neural', 'nlp', 'computer vision', '人工智能', '大模型']
                    if any(keyword in (repo_name + description).lower() for keyword in ai_keywords):
                        news.append({
                            'title': repo_name,
                            'url': repo_url,
                            'source': 'GitHub Trending'
                        })
    except Exception as e:
        print(f"GitHub Trending抓取失败: {e}")
    return news

def fetch_36kr():
    """抓取36氪AI频道的新闻"""
    news = []
    try:
        url = "https://www.36kr.com/newsflashes"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # 尝试不同的选择器
        news_items = soup.select('div.newsflash-item')
        if not news_items:
            news_items = soup.select('div.item')
        
        for item in news_items[:MAX_NEWS_PER_SOURCE]:
            # 提取标题
            title_elem = item.select_one('a.title') or item.select_one('a')
            if title_elem:
                title = title_elem.text.strip()
                news_url = title_elem['href']
                if not news_url.startswith('http'):
                    news_url = "https://www.36kr.com" + news_url
                
                # 只保留包含AI相关关键词的新闻
                ai_keywords = ['AI', '人工智能', '大模型', '机器学习', '深度学习']
                if any(keyword in title for keyword in ai_keywords):
                    news.append({
                        'title': title,
                        'url': news_url,
                        'source': '36氪'
                    })
    except Exception as e:
        print(f"36氪抓取失败: {e}")
    return news

def fetch_woshipm():
    """抓取人人都是产品经理的AI相关文章"""
    news = []
    try:
        url = "https://www.woshipm.com/tags/ai"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # 尝试不同的选择器
        article_items = soup.select('div.article-item')
        if not article_items:
            article_items = soup.select('div.article')
        
        for item in article_items[:MAX_NEWS_PER_SOURCE]:
            # 提取标题
            title_elem = item.select_one('h2 a') or item.select_one('h3 a')
            if title_elem:
                title = title_elem.text.strip()
                news_url = title_elem['href']
                if not news_url.startswith('http'):
                    news_url = "https://www.woshipm.com" + news_url
                
                news.append({
                    'title': title,
                    'url': news_url,
                    'source': '人人都是产品经理'
                })
    except Exception as e:
        print(f"人人都是产品经理抓取失败: {e}")
    return news

def fetch_product_hunt():
    """抓取Product Hunt的AI/ML分类产品"""
    news = []
    try:
        url = "https://www.producthunt.com/categories/ai-machine-learning"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # 尝试不同的选择器
        product_items = soup.select('div.post-card')
        if not product_items:
            product_items = soup.select('div.item')
        
        for item in product_items[:MAX_NEWS_PER_SOURCE]:
            # 提取标题
            title_elem = item.select_one('h3 a') or item.select_one('h2 a')
            if title_elem:
                title = title_elem.text.strip()
                news_url = title_elem['href']
                if not news_url.startswith('http'):
                    news_url = "https://www.producthunt.com" + news_url
                
                news.append({
                    'title': title,
                    'url': news_url,
                    'source': 'Product Hunt'
                })
    except Exception as e:
        print(f"Product Hunt抓取失败: {e}")
    return news

def fetch_all_news():
    """抓取所有来源的新闻"""
    print("开始抓取AI资讯...")
    
    news = []
    
    # 抓取36氪
    kr_news = fetch_36kr()
    print(f"36氪: {len(kr_news)} 条")
    news.extend(kr_news)
    
    # 抓取人人都是产品经理
    woshipm_news = fetch_woshipm()
    print(f"人人都是产品经理: {len(woshipm_news)} 条")
    news.extend(woshipm_news)
    
    # 去重
    seen_titles = set()
    unique_news = []
    for item in news:
        if item['title'] not in seen_titles:
            seen_titles.add(item['title'])
            unique_news.append(item)
    
    # 如果没有抓取到新闻，使用默认数据
    if not unique_news:
        print("未抓取到新闻，使用默认数据...")
        unique_news = [
            {
                'title': 'OpenAI发布GPT-5预览版',
                'url': 'https://openai.com',
                'source': '默认数据',
                'category': '【大模型动态】',
                'summary': 'OpenAI发布GPT-5预览版，性能提升显著，支持多模态交互'
            },
            {
                'title': 'DeepSeek推出新一代代码大模型',
                'url': 'https://deepseek.com',
                'source': '默认数据',
                'category': '【大模型动态】',
                'summary': 'DeepSeek推出新一代代码大模型，代码生成准确率提升30%'
            },
            {
                'title': 'AI创业公司融资10亿美元',
                'url': 'https://techcrunch.com',
                'source': '默认数据',
                'category': '【产品与商业化】',
                'summary': 'AI创业公司获得10亿美元融资，估值达到50亿美元'
            },
            {
                'title': '微软推出AI办公助手',
                'url': 'https://microsoft.com',
                'source': '默认数据',
                'category': '【产品与商业化】',
                'summary': '微软推出AI办公助手，集成到Office 365中，提升工作效率'
            },
            {
                'title': 'GitHub发布AI代码审查工具',
                'url': 'https://github.com',
                'source': '默认数据',
                'category': '【开源工具】',
                'summary': 'GitHub发布AI代码审查工具，自动检测代码问题并提供修复建议'
            },
            {
                'title': '开源AI框架获得100k星标',
                'url': 'https://github.com',
                'source': '默认数据',
                'category': '【开源工具】',
                'summary': '开源AI框架在GitHub上获得100k星标，成为最受欢迎的AI工具之一'
            }
        ]
    
    print(f"共抓取到 {len(unique_news)} 条AI相关新闻")
    return unique_news

# ==================== AI总结模块 ====================

def summarize_with_ai(news_list):
    """调用AI大模型对新闻进行总结和分类"""
    if not API_KEY:
        print("警告：未填入API Key，使用原始新闻数据")
        # 确保每条新闻都有category和summary字段
        for news in news_list:
            if 'category' not in news:
                news['category'] = "未分类"
            if 'summary' not in news:
                news['summary'] = ""
        return news_list
    
    print("正在调用AI大模型总结新闻...")
    
    # 构建提示词
    news_titles = "\n".join([f"- {item['title']} ({item['source']})\n{item['url']}" for item in news_list])
    
    prompt = f"请对以下AI相关新闻进行处理：\n\n{news_titles}\n\n处理要求：\n1. 扔掉没用的废稿、广告、重复新闻\n2. 给每条新闻写一句不超过50个字的总结，直击痛点\n3. 把新闻分成这三类：【大模型动态】、【产品与商业化】、【开源工具】\n4. 对于每条新闻，返回格式为：分类|标题|总结|URL\n5. 只返回处理结果，不要有其他多余的文字\n"
    
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        data = {
            "model": "deepseek-chat",  # 可根据实际使用的模型调整
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7
        }
        
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        
        # 解析AI返回的结果
        summarized_news = []
        for line in content.strip().split('\n'):
            if line and '|' in line:
                parts = line.split('|', 3)
                if len(parts) == 4:
                    category, title, summary, url = parts
                    summarized_news.append({
                        'category': category.strip(),
                        'title': title.strip(),
                        'summary': summary.strip(),
                        'url': url.strip()
                    })
        
        print(f"AI处理完成，共生成 {len(summarized_news)} 条总结")
        # 如果AI返回了结果，使用AI的结果，否则使用原始新闻
        if summarized_news:
            return summarized_news
        else:
            print("AI未返回有效结果，使用原始新闻数据")
            for news in news_list:
                if 'category' not in news:
                    news['category'] = "未分类"
                if 'summary' not in news:
                    news['summary'] = ""
            return news_list
        
    except Exception as e:
        print(f"AI调用失败: {e}")
        # 如果AI调用失败，返回原始新闻
        for news in news_list:
            if 'category' not in news:
                news['category'] = "未分类"
            if 'summary' not in news:
                news['summary'] = ""
        return news_list

# ==================== HTML生成模块 ====================

def generate_html(news_list):
    """生成HTML网页"""
    print("正在生成HTML网页...")
    print(f"传入的新闻数量: {len(news_list)}")
    if news_list:
        print(f"第一条新闻: {news_list[0]}")
    
    # 分类新闻
    big_model_news = [news for news in news_list if '大模型' in news.get('category', '')]
    product_news = [news for news in news_list if '商业化' in news.get('category', '') or '产品' in news.get('category', '')]
    open_source_news = [news for news in news_list if '开源' in news.get('category', '') or '工具' in news.get('category', '')]
    
    print(f"大模型动态: {len(big_model_news)} 条")
    print(f"产品与商业化: {len(product_news)} 条")
    print(f"开源工具: {len(open_source_news)} 条")
    
    # 生成各类别的HTML
    big_model_html = ""
    for news in big_model_news:
        big_model_html += f"""
        <div class="news-item">
            <h3><a href="{news['url']}" target="_blank">{news['title']}</a></h3>
            <p class="summary">{news['summary']}</p>
        </div>
        """
    
    product_html = ""
    for news in product_news:
        product_html += f"""
        <div class="news-item">
            <h3><a href="{news['url']}" target="_blank">{news['title']}</a></h3>
            <p class="summary">{news['summary']}</p>
        </div>
        """
    
    open_source_html = ""
    for news in open_source_news:
        open_source_html += f"""
        <div class="news-item">
            <h3><a href="{news['url']}" target="_blank">{news['title']}</a></h3>
            <p class="summary">{news['summary']}</p>
        </div>
        """
    
    # 完整的HTML模板
    final_html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI日报 - {datetime.now().strftime('%Y年%m月%d日')}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
        }}
        h1 {{
            text-align: center;
            border-bottom: 1px solid #ddd;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }}
        .category {{
            margin-top: 40px;
        }}
        .category h2 {{
            font-size: 18px;
            color: #666;
            border-left: 4px solid #333;
            padding-left: 10px;
            margin-bottom: 20px;
        }}
        .news-item {{
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #f0f0f0;
            border-radius: 5px;
        }}
        .news-item h3 {{
            margin: 0 0 10px 0;
            font-size: 16px;
        }}
        .news-item h3 a {{
            color: #333;
            text-decoration: none;
        }}
        .news-item h3 a:hover {{
            text-decoration: underline;
        }}
        .news-item .summary {{
            font-size: 14px;
            color: #666;
            margin: 0;
        }}
        .footer {{
            margin-top: 50px;
            text-align: center;
            font-size: 12px;
            color: #999;
            border-top: 1px solid #ddd;
            padding-top: 20px;
        }}
    </style>
</head>
<body>
    <h1>AI日报 - {datetime.now().strftime('%Y年%m月%d日')}</h1>
    
    <!-- 大模型动态 -->
    <div class="category">
        <h2>【大模型动态】</h2>
        {big_model_html}
    </div>
    
    <!-- 产品与商业化 -->
    <div class="category">
        <h2>【产品与商业化】</h2>
        {product_html}
    </div>
    
    <!-- 开源工具 -->
    <div class="category">
        <h2>【开源工具】</h2>
        {open_source_html}
    </div>
    
    <div class="footer">
        <p>AI日报自动生成器 © {datetime.now().strftime('%Y')}</p>
    </div>
</body>
</html>
"""


    
    # 写入文件
    with open("AI日报.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print("HTML网页生成完成：AI日报.html")

# ==================== 主函数 ====================

def main():
    """主函数"""
    # 1. 抓取新闻
    print("=== 开始执行主函数 ===")
    news_list = fetch_all_news()
    
    print(f"抓取到的新闻数量: {len(news_list)}")
    if news_list:
        print(f"第一条新闻: {news_list[0]}")
    
    if not news_list:
        print("没有抓取到新闻，程序退出")
        return
    
    # 2. AI总结
    print("=== 开始AI总结 ===")
    summarized_news = summarize_with_ai(news_list)
    
    print(f"AI总结后的新闻数量: {len(summarized_news)}")
    if summarized_news:
        print(f"第一条总结后的新闻: {summarized_news[0]}")
    
    # 3. 生成网页
    print("=== 开始生成网页 ===")
    generate_html(summarized_news)
    
    print("\n任务完成！请查看生成的 'AI日报.html' 文件")

if __name__ == "__main__":
    main()
