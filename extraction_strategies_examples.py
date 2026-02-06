"""
演示不同提取策略的示例，包含多种输入格式。
本示例展示了如何：
1. 使用不同的输入格式（markdown、HTML、fit_markdown）
2. 使用基于JSON的提取器（CSS和XPath）
3. 使用基于LLM的提取和不同输入格式
4. 正确配置浏览器和爬虫设置
"""

import asyncio
import os

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai import LLMConfig
from crawl4ai import (
    LLMExtractionStrategy,
    JsonCssExtractionStrategy,
    JsonXPathExtractionStrategy,
)
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def run_extraction(crawler: AsyncWebCrawler, url: str, strategy, name: str):
    """运行提取的辅助函数，使用正确的配置"""
    try:
        # 配置爬虫运行设置
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            extraction_strategy=strategy,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter()  # 用于支持fit_markdown
            ),
        )

        # 运行爬虫
        result = await crawler.arun(url=url, config=config)

        if result.success:
            print(f"\n=== {name} Results ===")
            print(f"Extracted Content: {result.extracted_content}")
            print(f"Raw Markdown Length: {len(result.markdown.raw_markdown)}")
            print(
                f"Citations Markdown Length: {len(result.markdown.markdown_with_citations)}"
            )
        else:
            print(f"Error in {name}: Crawl failed")

    except Exception as e:
        print(f"Error in {name}: {str(e)}")


async def main():
    # 示例URL（请替换为实际URL）
    url = "https://wiki.smartbi.com.cn/pages/viewpage.action?smt_poid=23&pageId=111891997"

    # 配置浏览器设置
    browser_config = BrowserConfig(headless=True, verbose=True)

    # 初始化提取策略

    # 1. 使用不同输入格式的LLM提取
    markdown_strategy = LLMExtractionStrategy(
        llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY")),
        instruction="Extract product information including name, price, and description",
    )

    html_strategy = LLMExtractionStrategy(
        input_format="html",
        llm_config=LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY")),
        instruction="Extract product information from HTML including structured data",
    )

    fit_markdown_strategy = LLMExtractionStrategy(
        input_format="fit_markdown",
        llm_config=LLMConfig(provider="openai/gpt-4o-mini",api_token=os.getenv("OPENAI_API_KEY")),
        instruction="Extract product information from cleaned markdown",
    )

    # 2. JSON CSS提取（自动使用HTML输入）
    css_schema = {
        "baseSelector": ".product",
        "fields": [
            {"name": "title", "selector": "h1.product-title", "type": "text"},
            {"name": "price", "selector": ".price", "type": "text"},
            {"name": "description", "selector": ".description", "type": "text"},
        ],
    }
    css_strategy = JsonCssExtractionStrategy(schema=css_schema)

    # 3. JSON XPath提取（自动使用HTML输入）
    xpath_schema = {
        "baseSelector": "//div[@class='product']",
        "fields": [
            {
                "name": "title",
                "selector": ".//h1[@class='product-title']/text()",
                "type": "text",
            },
            {
                "name": "price",
                "selector": ".//span[@class='price']/text()",
                "type": "text",
            },
            {
                "name": "description",
                "selector": ".//div[@class='description']/text()",
                "type": "text",
            },
        ],
    }
    xpath_strategy = JsonXPathExtractionStrategy(schema=xpath_schema)

    # 使用上下文管理器进行正确的资源处理
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # 运行所有策略
        await run_extraction(crawler, url, markdown_strategy, "Markdown LLM")
        await run_extraction(crawler, url, html_strategy, "HTML LLM")
        await run_extraction(crawler, url, fit_markdown_strategy, "Fit Markdown LLM")
        await run_extraction(crawler, url, css_strategy, "CSS Extraction")
        await run_extraction(crawler, url, xpath_strategy, "XPath Extraction")


if __name__ == "__main__":
    asyncio.run(main())
