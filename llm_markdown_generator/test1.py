import os
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai import LLMConfig
from crawl4ai.content_filter_strategy import LLMContentFilter


async def test_llm_filter():
    # 创建一个需要智能过滤的HTML源
    url = "https://wiki.smartbi.com.cn/pages/viewpage.action?smt_poid=23&pageId=111891997"

    browser_config = BrowserConfig(
        headless=True,
        verbose=True
    )

    # run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
    run_config = CrawlerRunConfig(cache_mode=CacheMode.ENABLED)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # 首先获取原始HTML
        result = await crawler.arun(url, config=run_config)
        html = result.cleaned_html

        # 使用针对性指令初始化LLM过滤器
        filter = LLMContentFilter(
            llm_config=LLMConfig(provider="glm-4.7",base_url="https://open.bigmodel.cn/api/paas/v4/chat/completions", api_token="cd72ca69e2b944cebf6523b0750f0c36.0EA6Wo4y6agqsSj7"),
            instruction="""
            Focus on extracting the core educational content about Python classes.
            Include:
            - Key concepts and their explanations
            - Important code examples
            - Essential technical details
            Exclude:
            - Navigation elements
            - Sidebars
            - Footer content
            - Version information
            - Any non-essential UI elements

            Format the output as clean markdown with proper code blocks and headers.
            """,
            verbose=True
        )

        # filter = LLMContentFilter(
        #     llm_config=LLMConfig(provider="glm-4.7",base_url="https://open.bigmodel.cn/api/paas/v4/chat/completions", api_token="cd72ca69e2b944cebf6523b0750f0c36.0EA6Wo4y6agqsSj7"),
        #     chunk_token_threshold=2 ** 12 * 2,  # 2048 * 2
        #     ignore_cache=True,
        #     instruction="""
        #     Extract the main educational content while preserving its original wording and substance completely. Your task is to:
        #
        #     1. Maintain the exact language and terminology used in the main content
        #     2. Keep all technical explanations, examples, and educational content intact
        #     3. Preserve the original flow and structure of the core content
        #     4. Remove only clearly irrelevant elements like:
        #     - Navigation menus
        #     - Advertisement sections
        #     - Cookie notices
        #     - Footers with site information
        #     - Sidebars with external links
        #     - Any UI elements that don't contribute to learning
        #
        #     The goal is to create a clean markdown version that reads exactly like the original article,
        #     keeping all valuable content but free from distracting elements. Imagine you're creating
        #     a perfect reading experience where nothing valuable is lost, but all noise is removed.
        #     """,
        #     verbose=True
        # )

        # 应用过滤
        filtered_content = filter.filter_content(html)

        # 显示结果
        print("\nFiltered Content Length:", len(filtered_content))
        print("\nFirst 500 chars of filtered content:")
        if filtered_content:
            print(filtered_content[0][:500])

        # 将markdown版本保存到磁盘
        with open("filtered_content.md", "w", encoding="utf-8") as f:
            f.write("\n".join(filtered_content))

        # 显示token使用情况
        filter.show_usage()


if __name__ == "__main__":
    asyncio.run(test_llm_filter())