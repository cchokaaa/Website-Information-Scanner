"""
Port Scanner Module / 端口扫描模块
Scan common ports on a target host
扫描目标主机的常用端口
"""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


# Common ports and their services / 常用端口及其服务
COMMON_PORTS = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    465: 'SMTPS',
    587: 'SMTP',
    993: 'IMAPS',
    995: 'POP3S',
    3306: 'MySQL',
    3389: 'RDP',
    5432: 'PostgreSQL',
    6379: 'Redis',
    8080: 'HTTP-Proxy',
    8443: 'HTTPS-Alt',
    27017: 'MongoDB',
}


def scan_port(host, port, timeout=2):
    """
    Scan a single port on a host
    扫描主机的单个端口
    
    Args:
        host (str): Target host IP / 目标主机 IP
        port (int): Port number / 端口号
        timeout (int): Connection timeout in seconds / 连接超时时间（秒）
        
    Returns:
        bool: True if port is open, False otherwise / 端口开放返回 True，否则返回 False
    """
    try:
        # Create TCP socket / 创建 TCP 套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Try to connect / 尝试连接
        result = sock.connect_ex((host, port))
        sock.close()
        
        # connect_ex returns 0 if successful / connect_ex 成功返回 0
        return result == 0
    except:
        return False


def scan_ports(domain, ports=None, max_workers=50, timeout=2):
    """
    Scan multiple ports on a domain
    扫描域名的多个端口
    
    Args:
        domain (str): Target domain / 目标域名
        ports (list/range/str, optional): Ports to scan / 要扫描的端口
        max_workers (int): Maximum concurrent threads / 最大并发线程数
        timeout (int): Connection timeout / 连接超时
        
    Returns:
        dict: Scan results / 扫描结果
    """
    try:
        # Resolve domain to IP / 将域名解析为 IP
        ip = socket.gethostbyname(domain.replace('https://', '').replace('http://', '').replace('www.', '').split('/')[0])
    except socket.gaierror:
        return {"error": "Could not resolve domain"}
    
    # Default to common ports / 默认扫描常用端口
    if ports is None:
        ports = list(COMMON_PORTS.keys())
    elif isinstance(ports, str):
        # Support range format: "1-1000" / 支持范围格式：1-1000
        if '-' in ports:
            start, end = ports.split('-')
            ports = range(int(start), int(end) + 1)
        # Support comma-separated format: "80,443,8080" / 支持逗号分隔格式
        else:
            ports = [int(p) for p in ports.split(',')]
    
    open_ports = []
    
    # Use thread pool for concurrent scanning / 使用线程池并发扫描
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_port = {executor.submit(scan_port, ip, port, timeout): port for port in ports}
        
        for future in as_completed(future_to_port):
            port = future_to_port[future]
            try:
                if future.result():
                    # Get service name / 获取服务名称
                    service = COMMON_PORTS.get(port, 'Unknown')
                    open_ports.append({'port': port, 'service': service})
            except Exception:
                pass
    
    # Sort by port number / 按端口号排序
    open_ports.sort(key=lambda x: x['port'])
    
    return {
        'host': ip,
        'open_ports': open_ports,
        'total_scanned': len(ports),
        'open_count': len(open_ports)
    }
