from datetime import datetime
from jinja2 import Template

def render_html(data):
    template = Template('''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI极简日报</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f6f6ef;
        }
        header {
            border-bottom: 2px solid #ff6600;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        h1 {
            font-size: 24px;
            color: #ff6600;
            margin: 0;
        }
        .date {
            color: #666;
            font-size: 14px;
            margin-top: 5px;
        }
        .news-item {
            background-color: white;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 4px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .news-item h2 {
            font-size: 18px;
            margin: 0 0 10px 0;
        }
        .news-item h2 a {
            color: #333;
            text-decoration: none;
        }
        .news-item h2 a:hover {
            text-decoration: underline;
        }
        .news-meta {
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
        }
        .news-summary {
            font-size: 14px;
            color: #555;
        }
        .category {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
            margin-right: 10px;
        }
        .category.技术进展 { background-color: #e6f7ff; color: #1890ff; }
        .category.产品发布 { background-color: #f6ffed; color: #52c41a; }
        .category.行业动态 { background-color: #fff7e6; color: #fa8c16; }
        .category.研究论文 { background-color: #f9f0ff; color: #722ed1; }
        .category.其他 { background-color: #f0f0f0; color: #666; }
        footer {
            margin-top: 30px;
            border-top: 1px solid #ddd;
            padding-top: 10px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>AI极简日报</h1>
        <div class="date">{{ date }}</div>
    </header>
    
    <main>
        {% for item in news %}
        <div class="news-item">
            <div class="news-meta">
                <span class="category {{ item.category }}">{{ item.category }}</span>
                <span>来源: {{ item.source }}</span>
            </div>
            <h2><a href="{{ item.link }}" target="_blank">{{ item.title }}</a></h2>
            <div class="news-summary">{{ item.summary }}</div>
        </div>
        {% endfor %}
    </main>
    
    <footer>
        <p>AI极简日报 - 每日AI资讯精选</p>
    </footer>
</body>
</html>
''')
    
    date = datetime.now().strftime('%Y年%m月%d日')
    html = template.render(news=data, date=date)
    
    # 写入index.html文件
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("HTML生成完成")
