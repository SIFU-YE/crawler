import xml.etree.ElementTree as ET
import asyncio
import re
import os
from crawl4ai import AsyncWebCrawler
from crawl4ai import BrowserConfig, CrawlerRunConfig
from crawl4ai import DefaultMarkdownGenerator
from crawl4ai import PruningContentFilter
from crawl4ai import CacheMode


# 解析指定的sitemap xml文件获取所有URL
def get_urls_from_sitemap(sitemap_path):
    urls = []
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        # 命名空间处理
        namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        # 提取所有loc标签内容
        for url in root.findall("ns:url", namespace):
            loc = url.find("ns:loc", namespace)
            if loc is not None and loc.text:
                urls.append(loc.text.strip())
        print(f"从 {sitemap_path} 中提取到 {len(urls)} 个URL")
    except Exception as e:
        print(f"解析 {sitemap_path} 出错: {e}")
    return urls


# 处理文件名，移除特殊字符
def sanitize_filename(title):
    if not title:
        return "untitled"
    # 移除不能用于文件名的特殊字符
    return re.sub(r'[\\/*?:"<>|]', "", title)[:100]  # 限制最大长度


# 新增：过滤包含指定关键字的行
def filter_markdown_content(content, keywords):
    """
    过滤掉包含指定关键字的行
    :param content: 原始markdown内容
    :param keywords: 需要过滤的关键字列表
    :return: 过滤后的内容
    """
    if not content:
        return ""
    
    # 按行分割内容，保留换行符以便恢复格式
    lines = content.splitlines(keepends=True)
    filtered_lines = []
    
    for line in lines:
        # 检查当前行是否包含任何关键字
        contains_keyword = any(keyword in line for keyword in keywords)
        if not contains_keyword:
            filtered_lines.append(line)
    
    # 合并过滤后的行
    filtered_content = ''.join(filtered_lines)
    return filtered_content


# 新增：添加信号量参数用于控制并发
async def crawl_and_save(crawler, url, index, total, save_dir, semaphore):
    """爬取单个URL并保存到指定目录下的markdown文件"""
    # 定义需要过滤的关键字列表
    keywords = [
        # 原有关键字
        "你还没有登录", "此页面正在由", "如果您无法使用此", "跳到banner的尾部",
        "回到标题开始", "转至元数据结尾", "已解决评论", "Page View Statistics", "AI搜索", "AI 思考中", "Copyright © ", "询问 Learn 询问 Learn", "使用英语阅读",
        # 新增关键字/文本
        "Facebook", "x.com", "共享", "LinkedIn",
        "访问此页面需要授权。 可以尝试登录或更改目录。",
        "访问此页面需要授权。 可以尝试更改目录。",
        "## 反馈",
        "此页面是否有帮助？",
        "需要有关本主题的帮助？",
        "想要尝试使用 Ask Learn 阐明或指导你完成本主题？",
        "询问 Learn 询问 Learn",
        "##  其他资源",
        "1月27日 11时 - 1月27日 11时",
        "欢迎加入我们，参加这场顶级的SQL与Microsoft Fabric活动。 使用代码 FABLEARN 节省 200 美元。",
        "立即注册",
        "* Last updated",
        "- Smartbi Api Doc"
    ]
    
    # 通过信号量控制并发数
    async with semaphore:
        # ========== 关键修改：添加1秒间隔 ==========
        await asyncio.sleep(1)
        
        # 确保保存目录存在
        os.makedirs(save_dir, exist_ok=True)
        
        try:
            run_config = CrawlerRunConfig(
                cache_mode=CacheMode.DISABLED,
                markdown_generator=DefaultMarkdownGenerator(
                    content_filter=PruningContentFilter(
                        threshold=0.6,
                        threshold_type="fixed"
                    ),
                    options={
                        "ignore_links": True,  # 改为False以保留链接文本
                        "ignore_images": False,  # 忽略图片减少干扰
                    }
                )
            )

            print(f"\n正在爬取 {index}/{total}: {url}")
            result = await crawler.arun(url=url, config=run_config)

            # 尝试获取页面标题作为文件名
            title = result.metadata.get("title", f"page_{hash(url)}")
            filename = f"{sanitize_filename(title)}.md"
            file_path = os.path.join(save_dir, filename)

            # ========== 关键修改：过滤内容 ==========
            # 获取原始markdown内容并过滤
            raw_content = result.markdown.fit_markdown
            filtered_content = filter_markdown_content(raw_content, keywords)

            # 保存过滤后的内容
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(filtered_content)

            print(f"✅ 已完成并保存: {file_path}")
            print(f"   原始内容长度: {len(raw_content)} 字符")
            print(f"   过滤后内容长度: {len(filtered_content)} 字符")

            return True

        except Exception as e:
            print(f"❌ 爬取 {url} 时出错: {str(e)}")
            return False


# 获取当前目录下所有以sitemap_开头的xml文件
def get_sitemap_files():
    sitemap_files = []
    for file in os.listdir("."):
        if file.startswith("sitemap_") and file.endswith(".xml"):
            sitemap_files.append(file)
    return sitemap_files


async def main():
    # 配置浏览器
    browser_config = BrowserConfig(
        headless=True,
        viewport_width=1280,
        viewport_height=720,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        text_mode=True,
    )

    # 获取所有以sitemap_开头的xml文件
    sitemap_files = get_sitemap_files()
    
    if not sitemap_files:
        print("没有找到任何以sitemap_开头的XML文件，程序退出")
        return

    print(f"找到 {len(sitemap_files)} 个sitemap文件待处理：{sitemap_files}")

    # 创建爬虫实例
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # 遍历每个sitemap文件
        for sitemap_file in sitemap_files:
            print(f"\n========== 开始处理文件: {sitemap_file} ==========")
            
            # 获取当前sitemap文件的URL列表
            urls = get_urls_from_sitemap(sitemap_file)
            
            if not urls:
                print(f"{sitemap_file} 中未提取到任何URL，跳过该文件")
                continue
            
            # 创建对应的保存目录（去掉.xml后缀）
            save_dir = os.path.splitext(sitemap_file)[0]
            total = len(urls)
            
            # 核心修改1：创建信号量，控制最大并发数（可根据需要调整，建议5-10）
            semaphore = asyncio.Semaphore(9)
            
            # 核心修改2：创建所有爬取任务
            tasks = []
            for i, url in enumerate(urls, 1):
                task = asyncio.create_task(
                    crawl_and_save(crawler, url, i, total, save_dir, semaphore)
                )
                tasks.append(task)
            
            # 核心修改3：批量执行所有任务并等待完成
            results = await asyncio.gather(*tasks)
            
            # 统计成功数量
            success_count = sum(results)
            print(f"\n{sitemap_file} 处理完成！成功 {success_count}/{total} 个URL")


if __name__ == "__main__":
    asyncio.run(main())