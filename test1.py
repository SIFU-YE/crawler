from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 目标页面URL
BASE_URL = "https://wiki.smartbi.com.cn"
TARGET_URL = "https://wiki.smartbi.com.cn/pages/viewpage.action?smt_poid=43&pageId=111882223"
TARGET_UL_ID = "child_ul111753103-0"

def init_driver():
    """初始化Chrome浏览器驱动"""
    try:
        chrome_options = webdriver.ChromeOptions()
        # 禁用图片加载以提高速度
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        # 禁用GPU加速，解决部分渲染问题
        chrome_options.add_argument("--disable-gpu")
        # 模拟正常浏览器窗口
        chrome_options.add_argument("--window-size=1280,720")
        # 添加用户代理
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

        # 初始化驱动
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        logger.info("浏览器驱动初始化成功")
        return driver
    except Exception as e:
        logger.error(f"初始化浏览器驱动失败: {str(e)}", exc_info=True)
        return None

def load_page(driver, url):
    """加载目标页面并等待关键元素出现"""
    try:
        logger.info(f"访问页面: {url}")
        driver.get(url)
        
        # 初始等待，确保页面开始加载
        time.sleep(2)
        
        # 显式等待目标元素加载完成
        wait = WebDriverWait(driver, 20)
        wait.until(
            EC.presence_of_element_located((By.ID, TARGET_UL_ID))
        )
        logger.info("页面加载完成，找到目标目录元素")
        return True
    except Exception as e:
        logger.error(f"页面加载失败: {str(e)}")
        # 保存页面源码供调试
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        logger.info("页面源码已保存至page_source.html")
        return False

def expand_all_menus(driver):
    """展开所有可展开的子菜单"""
    expanded_count = 0
    
    while True:
        try:
            # 查找所有未展开的菜单按钮
            expand_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((
                    By.CSS_SELECTOR, ".aui-iconfont-chevron-right"
                ))
            )
            
            if not expand_buttons:
                logger.info("没有更多可展开的菜单")
                break
                
            # 点击第一个找到的展开按钮
            button = expand_buttons[0]
            driver.execute_script("arguments[0].click();", button)
            expanded_count += 1
            logger.info(f"已展开第 {expanded_count} 个子菜单")
            
            # 等待菜单展开
            time.sleep(1)
            
        except Exception as e:
            logger.info(f"所有可展开的菜单已处理完毕: {str(e)}")
            break
            
    logger.info(f"共展开了 {expanded_count} 个子菜单")
    return expanded_count

def parse_directory(element, level=0):
    """递归解析目录结构并返回解析结果"""
    items = []
    items_found = 0
    
    # 查找当前层级下的所有li标签
    for li in element.find_all('li', recursive=False):
        try:
            # 定位内容链接
            content_div = li.find('div', class_='plugin_pagetree_children_content')
            if not content_div:
                continue
                
            span_tag = content_div.find('span', class_='plugin_pagetree_children_span')
            if not span_tag:
                continue
                
            a_tag = span_tag.find('a', href=True)
            if not a_tag:
                continue
                
            # 提取标题和链接
            title = a_tag.get_text(strip=True)
            href = a_tag['href']
            
            # 处理相对路径
            if href.startswith('/'):
                full_url = f"{BASE_URL}{href}"
            elif href.startswith('http'):
                full_url = href
            else:
                full_url = f"{BASE_URL}/{href}"
            
            # 按层级缩进显示
            indent = "  " * level
            print(f"{indent}- {title}")
            print(f"{indent}  链接: {full_url}\n")
            
            # 存储解析结果
            item = {
                'title': title,
                'url': full_url,
                'level': level,
                'children': []
            }
            items.append(item)
            items_found += 1
            
            # 查找子目录并递归解析
            children_div = li.find('div', class_='plugin_pagetree_children_container')
            if children_div:
                sub_ul = children_div.find('ul', class_='plugin_pagetree_children_list')
                if sub_ul:
                    sub_items, sub_count = parse_directory(sub_ul, level + 1)
                    item['children'] = sub_items
                    items_found += sub_count
                    
        except Exception as e:
            logger.warning(f"解析目录项时出错: {str(e)}")
            continue
    
    return items, items_found

def save_page_source(driver, filename="page_source.html"):
    """保存页面源码供调试"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        logger.info(f"页面源码已保存至{filename}")
    except Exception as e:
        logger.error(f"保存页面源码失败: {str(e)}")

def main():
    """主函数，协调各个步骤"""
    driver = None
    try:
        # 初始化浏览器
        driver = init_driver()
        if not driver:
            logger.error("无法初始化浏览器，程序退出")
            return
            
        # 加载页面
        if not load_page(driver, TARGET_URL):
            driver.quit()
            return
            
        # 等待目录结构加载完成
        time.sleep(3)
        
        # 展开所有可展开的子菜单
        logger.info("开始展开所有子菜单...")
        expand_all_menus(driver)
        
        # 等待所有内容加载完成
        time.sleep(2)
        
        # 获取页面源码并解析
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        root_ul = soup.find('ul', id=TARGET_UL_ID)
        
        if root_ul:
            print("\n===== 产品文档目录结构 =====")
            items, items_count = parse_directory(root_ul)
            if items_count == 0:
                print("警告: 未提取到任何目录项，可能是页面结构变化或访问限制")
                save_page_source(driver)
        else:
            print("未找到目标目录结构")
            save_page_source(driver)

    except Exception as e:
        logger.error(f"执行过程出错: {str(e)}", exc_info=True)
        if driver:
            save_page_source(driver)

    finally:
        # 确保浏览器关闭
        if driver:
            logger.info("关闭浏览器")
            driver.quit()

if __name__ == "__main__":
    main()
