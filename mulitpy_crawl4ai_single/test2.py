import asyncio
import re
from crawl4ai import AsyncWebCrawler, CacheMode, DefaultMarkdownGenerator, PruningContentFilter
from crawl4ai.async_configs import CrawlerRunConfig
from bs4 import BeautifulSoup, Tag


# URL转合法文件名函数（保持不变）
def sanitize_url_filename(url):
    if not url:
        return "crawl_result_untitled"
    url_without_protocol = re.sub(r'^https?://', '', url)
    sanitized = re.sub(r'[\\/*?:"<>|/:.]', "_", url_without_protocol)
    max_length = 200
    if len(sanitized) > max_length:
        sanitized = sanitized[:150] + "_" + sanitized[-49:]
    return sanitized


# 黑名单配置（新增：属性黑名单仅保留title，避免误伤href）
UNWANTED_CONTENT_FEATURES = {
    "class_contains": ["ad", "advert", "advertisement", "banner",
                       "login", "sign", "auth", "user-center"],
    "id_contains": ["login", "ad", "banner", "auth", "sign-in",
                    "log", "nav", "icon"],
    "tags": ["aside", "li"],  # 保留删除li标签的功能
    "attributes": ["title"]  # 仅过滤带title属性的节点，移除href避免误伤<a>
}

# 核心标签白名单：禁止删除的关键内容标签
CORE_TAG_WHITELIST = {"h1", "h2", "h3", "h4", "h5", "h6", "a", "p", "div", "span"}

# 全局统计
deleted_stats = {
    "class_contains": 0,
    "id_contains": 0,
    "tags": 0,
    "attributes": 0,
    "empty_parent": 0
}


def is_unwanted_node(node):
    """
    优化版：判断节点是否无用，优先检查白名单，避免误伤核心标签
    """
    # 第一步：核心标签白名单过滤——白名单内的标签直接判定为有用
    if node.name in CORE_TAG_WHITELIST:
        return (False, None)

    # 第二步：原有黑名单判断（仅对非核心标签生效）
    # 1. 标签黑名单
    if node.name in UNWANTED_CONTENT_FEATURES["tags"]:
        deleted_stats["tags"] += 1
        return (True, "tags")

    # 2. class黑名单
    node_class = node.get("class", [])
    if node_class:
        class_str = " ".join(node_class).lower()
        for keyword in UNWANTED_CONTENT_FEATURES["class_contains"]:
            if keyword in class_str:
                deleted_stats["class_contains"] += 1
                return (True, "class_contains")

    # 3. id黑名单
    node_id = node.get("id", "")
    if node_id:
        for keyword in UNWANTED_CONTENT_FEATURES["id_contains"]:
            if keyword in node_id.lower():
                deleted_stats["id_contains"] += 1
                return (True, "id_contains")

    # 4. 属性黑名单（仅对非核心标签生效）
    for attr in UNWANTED_CONTENT_FEATURES["attributes"]:
        if node.has_attr(attr):
            deleted_stats["attributes"] += 1
            return (True, "attributes")

    return (False, None)


def dfs_clean_node(node):
    """
    优化版：深度优先清洗，排除核心标签的空节点删除
    """
    if not isinstance(node, Tag):  # 仅处理Tag节点，跳过文本/注释节点
        return

    # 步骤1：递归处理所有子节点（避免遍历中节点被删除导致异常）
    for child in list(node.contents):
        dfs_clean_node(child)

    # 步骤2：判断当前节点是否需要删除
    is_unwanted, _ = is_unwanted_node(node)
    if is_unwanted:
        if node.parent:
            node.decompose()
        return

    # 步骤3：空节点判断——核心标签不删除，仅删除非核心标签的空节点
    if node.name not in CORE_TAG_WHITELIST:
        # 有效文本：去除空白后非空
        has_valid_text = bool(node.get_text(strip=True))
        # 有效子节点：存在未被删除的Tag子节点
        has_valid_children = any(isinstance(child, Tag) for child in node.contents)

        if not has_valid_text and not has_valid_children:
            deleted_stats["empty_parent"] += 1
            if node.parent:
                node.decompose()


async def two_step_html_cleaning():
    # 重置统计
    global deleted_stats
    deleted_stats = {k: 0 for k in deleted_stats.keys()}

    # 步骤1：爬取原始HTML（保持不变）
    target_url = "https://wiki.smartbi.com.cn/pages/viewpage.action?smt_poid=23&pageId=111891997"
    async with AsyncWebCrawler() as crawler:
        raw_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
        raw_result = await crawler.arun(url=target_url, config=raw_config)
        if not raw_result.success:
            print(f"爬取原始网页失败：{raw_result.error_message}")
            return
        original_html = raw_result.html
        print("=== 步骤1：获取原始HTML（前300字符预览）===")
        print(original_html[:300] + "..." if len(original_html) > 300 else original_html)

    # 步骤2：深度优先层级清洗（优化版）
    soup = BeautifulSoup(original_html, "lxml")
    print("\n=== 步骤2：开始深度优先层级黑名单清洗 ===")
    print("  - 先递归清洗子节点，再清理空父节点（跳过核心标签）...")

    # 从根节点开始清洗
    dfs_clean_node(soup.html)

    # 打印统计
    print(f"\n  清洗统计：")
    for k, v in deleted_stats.items():
        print(f"  - {k.replace('_', ' ')}：{v} 个")

    # 提取清洗后的HTML
    cleaned_html_1st = str(soup)
    print(f"\n=== 第一次清洗完成（HTML前300字符预览）===")
    print(cleaned_html_1st[:300] + "..." if len(cleaned_html_1st) > 300 else cleaned_html_1st)

    # 步骤3：二次清洗 + 保存Markdown（保持不变）
    raw_cleaned_url = f"raw:{cleaned_html_1st}"
    async with AsyncWebCrawler() as crawler:
        run_config = CrawlerRunConfig(
            cache_mode=CacheMode.DISABLED,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter(threshold=0.1, threshold_type="fixed"),
                options={"ignore_links": True, "ignore_images": False}
            )
        )
        final_result = await crawler.arun(url=raw_cleaned_url, config=run_config)
        if not final_result.success:
            print(f"\n二次清洗失败：{final_result.error_message}")
            return

        # 预览并保存
        print("\n=== 步骤3：二次清洗完成（Markdown预览）===")
        preview_content = final_result.markdown[:500] + "..." if len(
            final_result.markdown) > 500 else final_result.markdown
        print(preview_content)

        md_filename = f"{sanitize_url_filename(target_url)}.md"
        try:
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(final_result.markdown)
            print(f"\n✅ Markdown已保存：{md_filename}")
        except Exception as e:
            print(f"\n❌ 保存失败：{str(e)}")


if __name__ == "__main__":
    asyncio.run(two_step_html_cleaning())