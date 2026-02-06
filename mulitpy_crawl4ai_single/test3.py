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


# 黑名单配置（不变）
UNWANTED_CONTENT_FEATURES = {
    "class_contains": ["ad", "advert", "advertisement", "banner",
                       "login", "sign", "auth", "user-center"],
    "id_contains": ["login", "ad", "banner", "auth", "sign-in",
                    "log", "nav", "icon"],
    "tags": ["aside", "ul"],  # 该a标签大概率嵌套在此类标签中
    "href_contains": ["pageId"],  # 目标关键词
    # "attributes": ["title"]  # 按需开启
}

# 全局统计（保持不变）
deleted_stats = {
    "class_contains": 0,
    "id_contains": 0,
    "tags": 0,
    "attributes": 0,
    "href_contains": 0,
}


# 获取标签的易读标识（保持不变）
def get_node_identifier(node):
    if not isinstance(node, Tag):
        return "非标签节点"
    identifier = f"<{node.name}>"
    attrs = []
    if node.get("class"):
        class_str = " ".join(node.get("class"))
        attrs.append(f'class="{class_str}"')
    if node.get("id"):
        attrs.append(f'id="{node.get("id")}"')
    if node.get("href"):
        attrs.append(f'href="{node.get("href")[:50]}..."')
    if attrs:
        identifier = f"<{node.name} {' '.join(attrs)}>"
    return identifier


# 原因码转中文（保持不变）
def get_reason_cn(reason_code):
    reason_map = {
        "tags": "标签在黑名单中（精确匹配）",
        "class_contains": "class包含黑名单关键词（模糊匹配）",
        "id_contains": "id包含黑名单关键词（模糊匹配）",
        "attributes": "节点包含黑名单属性（存在判断）",
        "href_contains": "href包含黑名单关键词（模糊匹配）",
    }
    return reason_map.get(reason_code, f"未知原因({reason_code})")


def is_unwanted_node(node):
    """
    仅依据黑名单判断标签是否需要删除，命中任意规则即判定
    所有可匹配类型均为【不区分大小写 + 子串】模糊匹配
    修复：补充属性值合法性判断，避免非字符串值导致匹配异常
    """
    if not isinstance(node, Tag):
        return (False, None)

    # 1. 标签黑名单
    if node.name in UNWANTED_CONTENT_FEATURES["tags"]:
        deleted_stats["tags"] += 1
        return (True, "tags")

    # 2. class黑名单
    node_class = node.get("class", [])
    if node_class:
        class_str = " ".join(node_class).lower()
        for keyword in UNWANTED_CONTENT_FEATURES["class_contains"]:
            if keyword.lower() in class_str:
                deleted_stats["class_contains"] += 1
                return (True, "class_contains")

    # 3. id黑名单
    node_id = node.get("id", "")
    if isinstance(node_id, str) and node_id:  # 修复：判断是否为字符串，避免异常
        target_id = node_id.lower()
        for keyword in UNWANTED_CONTENT_FEATURES["id_contains"]:
            if keyword.lower() in target_id:
                deleted_stats["id_contains"] += 1
                return (True, "id_contains")

    # 4. 属性黑名单（按需开启）
    # for attr in UNWANTED_CONTENT_FEATURES["attributes"]:
    #     if node.has_attr(attr):
    #         deleted_stats["attributes"] += 1
    #         return (True, "attributes")

    # 5. href黑名单：核心模糊匹配
    node_href = node.get("href", "")
    if isinstance(node_href, str) and node_href:  # 修复：判断是否为字符串，避免解析器异常
        target_href = node_href.lower()
        for keyword in UNWANTED_CONTENT_FEATURES["href_contains"]:
            if keyword.lower() in target_href:
                deleted_stats["href_contains"] += 1
                return (True, "href_contains")

    # 未命中任何黑名单，不删除
    return (False, None)


def dfs_clean_node(node):
    """
    深度优先清洗：仅删除当前命中标签，子节点完整保留并提升层级
    核心修复：被提升的子节点必须重新执行清洗，避免漏检！
    """
    if not isinstance(node, Tag):
        return

    # 先判断当前标签是否命中黑名单
    is_unwanted, reason_code = is_unwanted_node(node)
    if is_unwanted and node.parent:
        node_id = get_node_identifier(node)
        reason_cn = get_reason_cn(reason_code)
        print(f"❌ 已删除命中黑名单的标签：{node_id} | 原因：{reason_cn}")

        # 提取子节点并提升层级
        all_children = list(node.contents)
        for child in all_children:
            node.insert_before(child)
        # 删除当前标签本身
        node.decompose()

        # 核心修复：对被提升的所有子节点重新执行深度优先清洗！
        # 解决父节点被删除后，子节点漏检的问题
        for child in all_children:
            dfs_clean_node(child)
        return  # 执行完子节点清洗后，再return

    # 未命中则递归清洗子节点（原有逻辑不变）
    for child in list(node.contents):
        dfs_clean_node(child)


async def two_step_html_cleaning():
    # 重置统计
    global deleted_stats
    deleted_stats = {k: 0 for k in deleted_stats.keys()}

    # 步骤1：爬取原始HTML
    target_url = "https://wiki.smartbi.com.cn/pages/viewpage.action?smt_poid=23&pageId=111891997"
    async with AsyncWebCrawler() as crawler:
        raw_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
        raw_result = await crawler.arun(url=target_url, config=raw_config)
        if not raw_result.success:
            print(f"❌ 爬取原始网页失败：{raw_result.error_message}")
            return
        original_html = raw_result.html
        print("=== 步骤1：成功获取原始HTML，开始执行标签清洗 ===")

    # 步骤2：核心清洗（修复后逻辑）
    soup = BeautifulSoup(original_html, "lxml")
    print("=== 步骤2：正在清洗标签，以下为命中黑名单被删除的标签信息 ===")
    dfs_clean_node(soup.html)

    # 步骤3：二次清洗+保存Markdown（保持不变）
    raw_cleaned_url = f"raw:{str(soup)}"
    async with AsyncWebCrawler() as crawler:
        run_config = CrawlerRunConfig(
            cache_mode=CacheMode.DISABLED,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter(threshold=0.7, threshold_type="fixed"),
                options={"ignore_links": True, "ignore_images": True}
            )
        )
        final_result = await crawler.arun(url=raw_cleaned_url, config=run_config)
        if not final_result.success:
            print(f"\n❌ 二次清洗生成Markdown失败：{final_result.error_message}")
            return

        # 保存Markdown
        print("\n=== 步骤3：二次清洗完成，开始保存Markdown文件 ===")
        md_filename = f"{sanitize_url_filename(target_url)}.md"
        try:
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(final_result.markdown)
            print(f"✅ Markdown文件已成功保存：{md_filename}")

            # 打印清洗统计
            print(f"\n=== 本次标签清洗统计结果 ===")
            total_deleted = sum(deleted_stats.values())
            print(f"累计删除命中黑名单的标签：{total_deleted}个")
            for reason, count in deleted_stats.items():
                if count > 0:
                    print(f"  - {get_reason_cn(reason)}：{count}个")
        except Exception as e:
            print(f"\n❌ Markdown文件保存失败：{str(e)}")


if __name__ == "__main__":
    asyncio.run(two_step_html_cleaning())