import asyncio
import re
from crawl4ai import AsyncWebCrawler
from crawl4ai import BrowserConfig, CrawlerRunConfig
from crawl4ai import DefaultMarkdownGenerator
from crawl4ai import PruningContentFilter
from crawl4ai import CacheMode


# 处理URL作为文件名，移除特殊字符并缩短长度
def sanitize_url_filename(url):
    if not url:
        return "untitled"
    # 1. 移除URL协议头（http://, https://）
    url_without_protocol = re.sub(r'^https?://', '', url)
    # 2. 移除不能用于文件名的特殊字符，替换为下划线
    sanitized = re.sub(r'[\\/*?:"<>|/:.]', "_", url_without_protocol)
    # 3. 限制最大长度（Windows文件名最大255字符，这里留有余量）
    max_length = 200
    if len(sanitized) > max_length:
        # 保留开头和结尾特征，中间截断
        sanitized = sanitized[:150] + "_" + sanitized[-49:]
    return sanitized


# 过滤无关内容的函数
def filter_unwanted_content(content):
    """
    过滤掉不需要的内容，保留链接名称等有效文本
    """
    if not content:
        return ""
    
    # 1. 移除指定的目标文本：利用大语言模型进行问题搜索
    target_text = "利用大语言模型进行问题搜索"
    content = content.replace(target_text, "")
    
    # 2. 移除JSON格式的无关数据（匹配 {"key": value, ...} 格式）
    json_pattern = r'\{[^}]*"serverDuration"[^}]*\}'
    content = re.sub(json_pattern, "", content, flags=re.DOTALL)
    
    # 3. 移除其他可能的JSON格式元数据
    meta_json_pattern = r'\{[^{}]*"requestCorrelationId"[^{}]*\}'
    content = re.sub(meta_json_pattern, "", content, flags=re.DOTALL)
    
    # 4. 移除多余的空白行和空格
    content = re.sub(r'\n\s*\n', '\n', content)  # 移除空行
    content = content.strip()
    
    return content


async def crawl_and_save_single_url(crawler, url):
    """爬取单个URL并保存为markdown文件"""
    try:
        run_config = CrawlerRunConfig(
            cache_mode=CacheMode.DISABLED,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter(
                    threshold=0.1,
                    threshold_type="fixed"
                ),
                options={
                    "ignore_links": True,  # 改为False以保留链接文本
                    "ignore_images": False,   # 忽略图片减少干扰
                }
            )
        )

        print(f"\n正在爬取: {url}")
        result = await crawler.arun(url=url, config=run_config)

        # 过滤无关内容，只保留有效文本（链接名称）
        cleaned_content = filter_unwanted_content(result.markdown.fit_markdown)

        # 使用URL作为文件名（处理后）
        filename = f"{sanitize_url_filename(url)}.md"

        # 保存过滤后的内容到markdown文件
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cleaned_content)

        print(f"✅ 已完成并保存: {filename}")
        print(f"   过滤后内容长度: {len(cleaned_content)} 字符")

        return True

    except Exception as e:
        print(f"❌ 爬取 {url} 时出错: {str(e)}")
        return False


async def main():
    # ====================== 配置区 ======================
    # 在这里修改你要爬取的单个URL
    TARGET_URL = "https://www.baidu.com/s?ie=UTF-8&wd=linux%E6%9F%A5%E7%9C%8B%E7%B3%BB%E7%BB%9F%E9%85%8D%E7%BD%AE"  # 替换为你要爬取的实际URL
    # ====================================================

    # 配置浏览器
    browser_config = BrowserConfig(
        headless=True,
        viewport_width=1280,
        viewport_height=720,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        text_mode=True,  # 只提取文本模式
    )

    # 创建爬虫实例并爬取
    async with AsyncWebCrawler(config=browser_config) as crawler:
        success = await crawl_and_save_single_url(crawler, TARGET_URL)

    if success:
        print("\n🎉 单个URL爬取完成，文件已保存到当前目录！")
    else:
        print("\n❌ 爬取失败，请检查URL是否正确或网络是否正常！")


if __name__ == "__main__":
    asyncio.run(main())