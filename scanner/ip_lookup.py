"""
IP Lookup Module / IP 查询模块
Domain to IP address resolution
域名到 IP 地址解析
"""

import socket


def get_ip(domain):
    """
    Resolve domain name to IP address
    将域名解析为 IP 地址
    
    Args:
        domain (str): Domain name to resolve / 要解析的域名
        
    Returns:
        str: IP address or error message / IP 地址或错误信息
    """
    try:
        # Use socket to resolve domain / 使用 socket 解析域名
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        return f"Error: {e}"
