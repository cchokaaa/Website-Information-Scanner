"""
Website Information Module / 网站信息模块
Fetch website metadata and server information
获取网站元数据和服务器信息
"""

import requests
from bs4 import BeautifulSoup


def get_website_info(url):
    """
    Get website information including title, server, status code
    获取网站信息，包括标题、服务器、状态码等
    
    Args:
        url (str): Website URL / 网站 URL
        
    Returns:
        dict: Website information dictionary / 网站信息字典
    """
    try:
        # Add protocol prefix if missing / 如果缺少协议前缀则添加
        if not url.startswith("http"):
            url = "https://" + url

        # Send HTTP GET request with proper encoding / 发送 HTTP GET 请求
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        
        # Auto-detect encoding / 自动检测编码
        response.encoding = response.apparent_encoding
        
        # Parse HTML with BeautifulSoup / 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title / 提取标题
        title = "No Title"
        if soup.title:
            title_text = soup.title.get_text(strip=True)
            if title_text:
                title = title_text
        
        # Get server type from headers / 从响应头获取服务器类型
        server = response.headers.get("Server", "Unknown")
        
        # Check HTTPS status / 检查 HTTPS 状态
        https_status = "Enabled" if url.startswith("https") else "Disabled"

        return {
            "title": title,
            "status_code": response.status_code,
            "server": server,
            "https": https_status
        }

    except Exception as e:
        return {"error": str(e)}
