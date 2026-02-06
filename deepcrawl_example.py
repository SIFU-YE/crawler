import asyncio
import time

from crawl4ai import CrawlerRunConfig, AsyncWebCrawler, CacheMode
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy, BestFirstCrawlingStrategy
from crawl4ai.deep_crawling.filters import (
    FilterChain,
    URLPatternFilter,
    DomainFilter,
    ContentTypeFilter,
    ContentRelevanceFilter,
    SEOFilter,
)
from crawl4ai.deep_crawling.scorers import (
    KeywordRelevanceScorer,
)


# 1️⃣ 基础深度爬取设置
async def basic_deep_crawl():
    """
    第一部分: 基础深度爬取设置 - 演示简单的两级深度爬取。

    本函数展示：
    - 如何设置 BFSDeepCrawlStrategy（广度优先搜索）
    - 设置深度和域名参数
    - 处理结果以显示层级结构
    """
    print("\n===== 基础深度爬取设置 =====")

    # 使用广度优先搜索策略配置2级深度爬取
    # max_depth=2 表示：初始页面（深度0）+ 2个额外层级
    # include_external=False 表示：只爬取同一域名内的链接
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=2, include_external=False),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True,  # 爬取过程中显示进度
    )

    async with AsyncWebCrawler() as crawler:
        start_time = time.perf_counter()
        results = await crawler.arun(url="https://wiki.smartbi.com.cn/pages/viewpage.action?smt_poid=23&pageId=111891997", config=config)

        # 按深度分组结果以可视化爬取树
        pages_by_depth = {}
        for result in results:
            depth = result.metadata.get("depth", 0)
            if depth not in pages_by_depth:
                pages_by_depth[depth] = []
            pages_by_depth[depth].append(result.url)

        print(f"✅ 总共爬取了 {len(results)} 个页面")

        # 按深度显示爬取结构
        for depth, urls in sorted(pages_by_depth.items()):
            print(f"\nDepth {depth}: {len(urls)} pages")
            # 显示每个深度的前3个URL作为示例
            for url in urls[:3]:
                print(f"  → {url}")
            if len(urls) > 3:
                print(f"  ... 还有 {len(urls) - 3} 个")

        print(
            f"\n✅ 性能: {len(results)} 个页面用时 {time.perf_counter() - start_time:.2f} 秒"
        )

# 2️⃣ 流式 vs 非流式执行
async def stream_vs_nonstream():
    """
    第二部分: 演示流式和非流式执行之间的区别。

    非流式：等待所有结果完成后再处理
    流式：结果可用时立即处理
    """
    print("\n===== 流式 vs 非流式执行 =====")

    # 两个示例的通用配置
    base_config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=1, include_external=False),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=False,
    )

    async with AsyncWebCrawler() as crawler:
        # 非流式模式
        print("\n📊 非流式模式:")
        print("  在此模式下，所有结果被收集完成后才返回。")

        non_stream_config = base_config.clone()
        non_stream_config.stream = False

        start_time = time.perf_counter()
        results = await crawler.arun(
            url="https://docs.crawl4ai.com", config=non_stream_config
        )

        print(f"  ✅ 一次性接收所有 {len(results)} 个结果")
        print(f"  ✅ 总耗时: {time.perf_counter() - start_time:.2f} 秒")

        # 流式模式
        print("\n📊 流式模式:")
        print("  在此模式下，结果可用时立即处理。")

        stream_config = base_config.clone()
        stream_config.stream = True

        start_time = time.perf_counter()
        result_count = 0
        first_result_time = None

        async for result in await crawler.arun(
            url="https://docs.crawl4ai.com", config=stream_config
        ):
            result_count += 1
            if result_count == 1:
                first_result_time = time.perf_counter() - start_time
                print(
                    f"  ✅ 第一个结果在 {first_result_time:.2f} 秒后接收: {result.url}"
                )
            elif result_count % 5 == 0:  # 为简洁起见，每5个结果显示一次
                print(f"  → 结果 #{result_count}: {result.url}")

        print(f"  ✅ 总计: {result_count} 个结果")
        print(f"  ✅ 第一个结果: {first_result_time:.2f} 秒")
        print(f"  ✅ 所有结果: {time.perf_counter() - start_time:.2f} 秒")
        print("\n🔍 关键要点: 流式允许立即处理结果")

# 3️⃣ 介绍过滤器与评分器
async def filters_and_scorers():
    """
    第三部分: 演示使用过滤器和评分器进行更有针对性的爬取。

    本函数逐步添加：
    1. 单个URL模式过滤器
    2. 链中的多个过滤器
    3. 用于页面优先级排序的评分器
    """
    print("\n===== 过滤器与评分器 =====")

    async with AsyncWebCrawler() as crawler:
        # 单个过滤器示例
        print("\n📊 示例 1: 单个URL模式过滤器")
        print("  只爬取URL中包含'core'的页面")

        # 创建一个只允许包含'guide'的URL的过滤器
        url_filter = URLPatternFilter(patterns=["*core*"])

        config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=1,
                include_external=False,
                filter_chain=FilterChain([url_filter]),  # 单个过滤器
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            cache_mode=CacheMode.BYPASS,
            verbose=True,
        )

        results = await crawler.arun(url="https://docs.crawl4ai.com", config=config)

        print(f"  ✅ 爬取了 {len(results)} 个匹配 '*core*' 的页面")
        for result in results[:3]:  # 显示前3个结果
            print(f"  → {result.url}")
        if len(results) > 3:
            print(f"  ... 还有 {len(results) - 3} 个")

        # 多个过滤器示例
        print("\n📊 示例 2: 链中的多个过滤器")
        print("  只爬取满足以下条件的页面：")
        print("  1. URL中包含'2024'")
        print("  2. 来自'techcrunch.com'")
        print("  3. 内容类型为 text/html 或 application/javascript")

        # 创建过滤器链
        filter_chain = FilterChain(
            [
                URLPatternFilter(patterns=["*2024*"]),
                DomainFilter(
                    allowed_domains=["techcrunch.com"],
                    blocked_domains=["guce.techcrunch.com", "oidc.techcrunch.com"],
                ),
                ContentTypeFilter(
                    allowed_types=["text/html", "application/javascript"]
                ),
            ]
        )

        config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=1, include_external=False, filter_chain=filter_chain
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            verbose=True,
        )

        results = await crawler.arun(url="https://techcrunch.com", config=config)

        print(f"  ✅ 应用所有过滤器后爬取了 {len(results)} 个页面")
        for result in results[:3]:
            print(f"  → {result.url}")
        if len(results) > 3:
            print(f"  ... 还有 {len(results) - 3} 个")

        # 评分器示例
        print("\n📊 示例 3: 使用关键词相关性评分器")
        print(
            "根据与以下关键词的相关性对页面评分：'crawl', 'example', 'async', 'configuration','javascript','css'"
        )

        # 创建关键词相关性评分器
        keyword_scorer = KeywordRelevanceScorer(
            keywords=["crawl", "example", "async", "configuration","javascript","css"], weight=1
        )

        config = CrawlerRunConfig(
            deep_crawl_strategy=BestFirstCrawlingStrategy(  
                max_depth=1, include_external=False, url_scorer=keyword_scorer
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            cache_mode=CacheMode.BYPASS,
            verbose=True,
            stream=True,
        )

        results = []
        async for result in await crawler.arun(
            url="https://docs.crawl4ai.com", config=config
        ):
            results.append(result)
            score = result.metadata.get("score")
            print(f"  → Score: {score:.2f} | {result.url}")

        print(f"  ✅ 爬虫根据相关性评分优先处理了 {len(results)} 个页面")
        print("  🔍 注意: BestFirstCrawlingStrategy 优先访问评分最高的页面")

# 4️⃣ 高级过滤器
async def advanced_filters():
    """
    第四部分: 演示专业爬取的高级过滤技术。

    本函数涵盖：
    - SEO过滤器
    - 文本相关性过滤
    - 组合高级过滤器
    """
    print("\n===== ADVANCED FILTERS =====")

    async with AsyncWebCrawler() as crawler:
        # SEO FILTER EXAMPLE
        print("\n📊 EXAMPLE 1: SEO FILTERS")
        print(
            "Quantitative SEO quality assessment filter based searching keywords in the head section"
        )

        seo_filter = SEOFilter(
            threshold=0.5, keywords=["dynamic", "interaction", "javascript"]
        )

        config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=1, filter_chain=FilterChain([seo_filter])
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            verbose=True,
            cache_mode=CacheMode.BYPASS,
        )

        results = await crawler.arun(url="https://docs.crawl4ai.com", config=config)

        print(f"  ✅ Found {len(results)} pages with relevant keywords")
        for result in results:
            print(f"  → {result.url}")

        # ADVANCED TEXT RELEVANCY FILTER
        print("\n📊 EXAMPLE 2: ADVANCED TEXT RELEVANCY FILTER")

        # More sophisticated content relevance filter
        relevance_filter = ContentRelevanceFilter(
            query="Interact with the web using your authentic digital identity",
            threshold=0.7,
        )

        config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=1, filter_chain=FilterChain([relevance_filter])
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            verbose=True,
            cache_mode=CacheMode.BYPASS,
        )

        results = await crawler.arun(url="https://docs.crawl4ai.com", config=config)

        print(f"  ✅ 找到 {len(results)} 个页面")
        for result in results:
            relevance_score = result.metadata.get("relevance_score", 0)
            print(f"  → 评分: {relevance_score:.2f} | {result.url}")

# 5️⃣ 最大页面数和评分阈值
async def max_pages_and_thresholds():
    """
    第五部分: 演示在不同策略中使用 max_pages 和 score_threshold 参数。
    
    本函数展示：
    - 如何限制爬取的页面数量
    - 如何设置评分阈值以实现更有针对性的爬取
    - 比较 BFS、DFS 和 Best-First 策略在这些参数下的表现
    """
    print("\n===== 最大页面数和评分阈值 =====")
    
    from crawl4ai.deep_crawling import DFSDeepCrawlStrategy
    
    async with AsyncWebCrawler() as crawler:
        # 为所有示例定义一个通用的关键词评分器
        keyword_scorer = KeywordRelevanceScorer(
            keywords=["browser", "crawler", "web", "automation"], 
            weight=1.0
        )
        
        # 示例 1: 带最大页面限制的BFS
        print("\n📊 示例 1: 带最大页面限制的BFS策略")
        print("  将爬虫限制为最多5个页面")
        
        bfs_config = CrawlerRunConfig(
            deep_crawl_strategy=BFSDeepCrawlStrategy(
                max_depth=2, 
                include_external=False,
                url_scorer=keyword_scorer,
                max_pages=1  # 只爬取5个页面
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            verbose=True,
            cache_mode=CacheMode.BYPASS,
        )
        
        results = await crawler.arun(url="https://docs.crawl4ai.com", config=bfs_config)
        
        print(f"  ✅ 按照max_pages设置精确爬取了 {len(results)} 个页面")
        for result in results:
            depth = result.metadata.get("depth", 0)
            print(f"  → 深度: {depth} | {result.url}")
            
        # 示例 2: 带评分阈值的DFS
        print("\n📊 示例 2: 带评分阈值的DFS策略")
        print("  只爬取相关性评分高于0.5的页面")
        
        dfs_config = CrawlerRunConfig(
            deep_crawl_strategy=DFSDeepCrawlStrategy(
                max_depth=2,
                include_external=False, 
                url_scorer=keyword_scorer,
                score_threshold=0.7,  # 只处理评分高于0.5的URL
                max_pages=10
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            verbose=True,
            cache_mode=CacheMode.BYPASS,
        )
        
        results = await crawler.arun(url="https://docs.crawl4ai.com", config=dfs_config)
        
        print(f"  ✅ 爬取了 {len(results)} 个评分高于阈值的页面")
        for result in results:
            score = result.metadata.get("score", 0)
            depth = result.metadata.get("depth", 0)
            print(f"  → 深度: {depth} | 评分: {score:.2f} | {result.url}")
            
        # 示例 3: 带双重限制的最佳优先策略
        print("\n📊 示例 3: 带双重限制的最佳优先策略")
        print("  限制为7个评分高于0.3的页面，优先处理评分最高的页面")
        
        bf_config = CrawlerRunConfig(
            deep_crawl_strategy=BestFirstCrawlingStrategy(
                max_depth=2,
                include_external=False,
                url_scorer=keyword_scorer,
                max_pages=7,          # 总共限制为7个页面
            ),
            scraping_strategy=LXMLWebScrapingStrategy(),
            verbose=True,
            cache_mode=CacheMode.BYPASS,
            stream=True,
        )
        
        results = []
        async for result in await crawler.arun(url="https://docs.crawl4ai.com", config=bf_config):
            results.append(result)
            score = result.metadata.get("score", 0)
            depth = result.metadata.get("depth", 0)
            print(f"  → 深度: {depth} | 评分: {score:.2f} | {result.url}")
            
        print(f"  ✅ 爬取了 {len(results)} 个评分高于0.3的高价值页面")
        if results:
            avg_score = sum(r.metadata.get('score', 0) for r in results) / len(results)
            print(f"  ✅ 平均评分: {avg_score:.2f}")
            print("  🔍 注意: BestFirstCrawlingStrategy 优先访问评分最高的页面")

# 6️⃣ 总结与关键要点
async def wrap_up():
    """
    第六部分: 总结与关键要点

    总结本教程中学到的关键概念。
    """
    print("\n===== 完整爬虫示例 =====")
    print("组合过滤器、评分器和流式处理以实现优化的爬取")

    # 创建复杂的过滤器链
    filter_chain = FilterChain(
        [
            DomainFilter(
                allowed_domains=["docs.crawl4ai.com"],
                blocked_domains=["old.docs.crawl4ai.com"],
            ),
            URLPatternFilter(patterns=["*core*", "*advanced*", "*blog*"]),
            ContentTypeFilter(allowed_types=["text/html"]),
        ]
    )

    # 创建组合多种评分策略的复合评分器
    keyword_scorer = KeywordRelevanceScorer(
        keywords=["crawl", "example", "async", "configuration"], weight=0.7
    )
    # 设置配置
    config = CrawlerRunConfig(
        deep_crawl_strategy=BestFirstCrawlingStrategy(
            max_depth=1,
            include_external=False,
            filter_chain=filter_chain,
            url_scorer=keyword_scorer,
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        stream=True,
        verbose=True,
    )

    # 执行爬取
    results = []
    start_time = time.perf_counter()

    async with AsyncWebCrawler() as crawler:
        async for result in await crawler.arun(
            url="https://docs.crawl4ai.com", config=config
        ):
            results.append(result)
            score = result.metadata.get("score", 0)
            depth = result.metadata.get("depth", 0)
            print(f"→ 深度: {depth} | 评分: {score:.2f} | {result.url}")

    duration = time.perf_counter() - start_time

    # 总结结果
    print(f"\n✅ 在 {duration:.2f} 秒内爬取了 {len(results)} 个高价值页面")
    print(
        f"✅ 平均评分: {sum(r.metadata.get('score', 0) for r in results) / len(results):.2f}"
    )

    # 按深度分组
    depth_counts = {}
    for result in results:
        depth = result.metadata.get("depth", 0)
        depth_counts[depth] = depth_counts.get(depth, 0) + 1

    print("\n📊 按深度统计的爬取页面:")
    for depth, count in sorted(depth_counts.items()):
        print(f"  Depth {depth}: {count} pages")


async def run_tutorial():
    """
    按顺序执行所有教程部分。
    """
    print("\n🚀 CRAWL4AI 深度爬取教程 🚀")
    print("======================================")
    print("本教程将带你了解使用Crawl4AI库的深度爬取技术，")
    print("从基础到高级应用。")

    # 定义教程部分 - 在开发期间取消注释以运行特定部分
    tutorial_sections = [
        basic_deep_crawl,
        stream_vs_nonstream,
        filters_and_scorers,
        max_pages_and_thresholds, 
        advanced_filters,
        wrap_up,
    ]

    for section in tutorial_sections:
        await section()

    print("\n🎉 教程完成！🎉")
    print("你现在对使用Crawl4AI进行深度爬取有了全面的理解。")
    print("更多信息请访问 https://docs.crawl4ai.com")

# 直接运行时执行教程
if __name__ == "__main__":
    asyncio.run(run_tutorial())