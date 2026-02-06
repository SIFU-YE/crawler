import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
# 新增：导入CacheMode枚举类，用于设置缓存模式
from crawl4ai import CacheMode

async def crawl_raw_html():
    raw_html = "<html><body><h1>Hello, World!</h1></body></html>"
    raw_html_url = f"raw:{raw_html}"
    # 修改：将bypass_cache=True替换为cache_mode=CacheMode.BYPASS
    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=raw_html_url, config=config)
        if result.success:
            print("Markdown Content from Raw HTML:")
            print(result.markdown)
        else:
            print(f"Failed to crawl raw HTML: {result.error_message}")

asyncio.run(crawl_raw_html())