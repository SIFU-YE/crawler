import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def main():
    browser_config = BrowserConfig(
        headless=True,  # 是否无头模式，True：不打卡浏览器
        viewport_width=1280,  # 视口宽度
        viewport_height=720,  # 视口高度
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        # 用户代理
    )  # 浏览器配置
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.DISABLED,  # 禁用缓存模式，获取最新内容
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=BM25ContentFilter(
                bm25_threshold=0.2,
            ),
            options={
                ""
                "ignore_links": True,  # 是否在最终markdown中移除所有超链接
                "ignore_images": True,  # 是否在最终markdown中移除所有图片
            }
        )
    )  # 爬虫运行配置

    async with AsyncWebCrawler(config=browser_config) as crawler:
        try:
            result = await crawler.arun(
                url="https://wiki.smartbi.com.cn/pages/viewpage.action?smt_poid=23&pageId=111891696",
                config=run_config
            )
        except Exception as e:
            print(f"错误：{e}")
        with open(f"2.2.3result-{len(result.markdown.fit_markdown)}.md", "w", encoding="utf-8") as f:
            f.write(result.markdown.fit_markdown)
        print(f"内容长度：{len(result.markdown.fit_markdown)}")
        print(f"已保存在：{f.name}")


if __name__ == "__main__":
    asyncio.run(main())
