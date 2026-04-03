import feedparser
from concurrent.futures import ThreadPoolExecutor
from config import DATA_SOURCES, MAX_WORKERS

def fetch_rss_feed(url):
    """抓取RSS源并解析"""
    try:
        feed = feedparser.parse(url)
        if feed.bozo == 0:
            return feed.entries
        else:
            print(f"解析RSS失败: {feed.bozo_exception}")
            return []
    except Exception as e:
        print(f"抓取RSS失败: {e}")
        return []

def fetch_all_feeds():
    """并行抓取所有数据源"""
    all_entries = []
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(lambda source: fetch_rss_feed(source["url"]), DATA_SOURCES))
    
    for i, entries in enumerate(results):
        source_name = DATA_SOURCES[i]["name"]
        for entry in entries:
            entry["source"] = source_name
        all_entries.extend(entries)
    
    return all_entries
