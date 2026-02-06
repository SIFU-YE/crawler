

from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy
# 核心导入：crawl4ai 0.8.0 专属LLMConfig
from crawl4ai import LLMConfig
from dotenv import load_dotenv
import os
import asyncio

# 加载环境变量（读取智谱密钥/模型）
load_dotenv()
ZHIPU_API_KEY = "cd72ca69e2b944cebf6523b0750f0c36.0EA6Wo4y6agqsSj7"
ZHIPU_MODEL ="ZHIPU_MODEL/glm-4-flash"
# 智谱OpenAI兼容接口地址（固定，切勿修改）
ZHIPU_BASE_URL = "https://open.bigmodel.cn/api/paas/v4/"

# 自定义智谱清洗提示词（可按需求修改规则）
CLEAN_PROMPT = """
请你作为专业网页内容清洗师，处理爬取的原始内容，严格遵守：
1. 彻底删除广告、导航、侧边栏、评论区、相关推荐等所有冗余信息；
2. 仅保留核心有效内容，保留标题、段落、列表的原始逻辑结构；
3. 用Markdown格式化清洗后的内容，标题分级、段落分行，删除无效空行；
4. 只输出清洗后的纯净内容，不添加任何额外解释、备注。
"""

async def crawl_and_clean_with_zhipu(url: str):
    """爬取网页+智谱大模型清洗（最终修正版，适配crawl4ai 0.8.0）"""
    async with AsyncWebCrawler(verbose=True) as crawler:
        try:
            # 核心修正：LLMConfig用llm_model指定模型（替代原model，解决报错）
            zhipu_llm_config = LLMConfig(
                llm_model=ZHIPU_MODEL,      # 【唯一修改点】model → llm_model
                base_url=ZHIPU_BASE_URL,    # 智谱接口地址（不变）
                api_key=ZHIPU_API_KEY,      # 智谱API密钥（不变）
                temperature=0.1,            # 清洗内容建议0.0-0.3，输出更稳定
                max_tokens=8192,            # 最大输出token，长页面可调大
                request_timeout=30,         # LLM请求超时时间，避免卡顿
            )

            # 配置LLM清洗策略，传入封装好的LLMConfig
            llm_strategy = LLMExtractionStrategy(
                llm_config=zhipu_llm_config,
                prompt=CLEAN_PROMPT
            )

            # 执行爬取+清洗
            result = await crawler.arun(
                url=url,
                extraction_strategy=llm_strategy,
                # 爬虫基础配置（按需调整）
                bypass_cache=True,
                render_js=False,  # 动态页面改True，静态页面保持False更高效
                wait_for_navigation=True,
                timeout=60,
                # 自定义UA，降低反爬概率
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
            )

            # 输出结果+保存到本地
            print("="*100)
            print("✅ 爬取+清洗成功！智谱清洗后的内容：\n")
            print(result.extracted_content)
            print("="*100)

            # 保存清洗后的内容到Markdown文件
            with open("智谱清洗后的网页内容.md", "w", encoding="utf-8") as f:
                f.write(result.extracted_content)
            print("📄 内容已保存至：智谱清洗后的网页内容.md")

            return result.extracted_content

        except Exception as e:
            print(f"❌ 爬取/清洗失败，错误详情：{str(e)}")
            return None

# 测试主函数
if __name__ == "__main__":
    # 替换为你的目标URL（静态/动态页面均可）
    TARGET_URL = "https://www.infoq.cn/article/2025-09-python-crawl4ai-practice"
    asyncio.run(crawl_and_clean_with_zhipu(TARGET_URL))