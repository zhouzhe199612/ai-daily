import os
import json
import openai
from dotenv import load_dotenv
from config import LLM_MODEL, LLM_TEMPERATURE

# 加载环境变量
load_dotenv()

# 配置OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

def process_with_llm(entries):
    if not entries:
        return []
    
    # 构建提示
    entries_text = "\n".join([f"标题: {e['title']}\n简述: {e['summary']}\n来源: {e['source']}" for e in entries])
    
    prompt = '''请对以下AI相关资讯进行处理，输出JSON格式的结果：

''' + entries_text + '''

处理要求：
1. 对每个条目生成一个简洁的摘要（不超过50字）
2. 对每个条目进行分类，分类包括：技术进展、产品发布、行业动态、研究论文、其他
3. 按照重要性排序（1-5，5为最重要）
4. 输出格式如下：
[
    {
        "title": "条目标题",
        "link": "条目链接",
        "summary": "生成的摘要",
        "category": "分类",
        "importance": 重要性评分,
        "source": "信息来源"
    },
    ...
]
'''
    
    try:
        response = openai.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "你是一个专业的AI资讯分析助手，擅长对科技资讯进行摘要和分类。"},
                {"role": "user", "content": prompt}
            ],
            temperature=LLM_TEMPERATURE
        )
        
        # 解析LLM返回的JSON
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        print(f"LLM处理失败: {e}")
        # 如果LLM处理失败，返回原始条目
        return [
            {
                "title": e["title"],
                "link": e["link"],
                "summary": e["summary"],
                "category": "其他",
                "importance": 3,
                "source": e["source"]
            }
            for e in entries
        ]
