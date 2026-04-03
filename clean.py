from datetime import datetime, timedelta
from config import CUTOFF_DAYS

def clean_entries(entries):
    """清洗和去重条目"""
    # 去重（基于标题）
    seen_titles = set()
    unique_entries = []
    
    # 过滤过去24小时的条目
    cutoff_time = datetime.now() - timedelta(days=CUTOFF_DAYS)
    
    for entry in entries:
        # 检查发布时间
        if "published_parsed" in entry:
            pub_time = datetime(*entry["published_parsed"][:6])
            if pub_time < cutoff_time:
                continue
        
        # 去重
        title = entry.get("title", "").strip()
        if title and title not in seen_titles:
            seen_titles.add(title)
            unique_entries.append({
                "title": title,
                "link": entry.get("link", ""),
                "summary": entry.get("summary", ""),
                "source": entry.get("source", ""),
                "published": entry.get("published", "")
            })
    
    return unique_entries
