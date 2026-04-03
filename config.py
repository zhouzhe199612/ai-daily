# 数据源配置
DATA_SOURCES = [
    {
        "name": "GitHub Trending",
        "url": "https://rsshub.app/github/trending/ai"
    },
    {
        "name": "36氪AI频道",
        "url": "https://rsshub.app/36kr/channel/ai"
    },
    {
        "name": "人人都是产品经理AI标签",
        "url": "https://rsshub.app/woshipm/tag/ai"
    },
    {
        "name": "Product Hunt AI/ML",
        "url": "https://rsshub.app/producthunt/category/ai-ml"
    }
]

# LLM配置
LLM_MODEL = "gpt-4o-mini"
LLM_TEMPERATURE = 0.3

# 抓取配置
MAX_WORKERS = 4
CUTOFF_DAYS = 1
