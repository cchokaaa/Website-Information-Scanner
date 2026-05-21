"""
GeoIP Module / GeoIP 模块
IP geolocation lookup based on IP address
通过 IP 地址查询地理位置信息
"""

import requests


def get_geo_info(ip_address):
    """
    Get geolocation information for an IP address
    获取 IP 地址的地理位置信息
    
    Args:
        ip_address (str): IP address to look up / 要查询的 IP 地址
        
    Returns:
        dict: Geolocation information / 地理位置信息字典
    """
    try:
        # Use ip-api.com free API / 使用 ip-api.com 免费 API
        response = requests.get(f'http://ip-api.com/json/{ip_address}', timeout=10)
        data = response.json()
        
        if data['status'] == 'success':
            info = {}
            
            # Country / 国家
            if data.get('country'):
                info['Country'] = data['country']
            
            # Region / 地区/省
            if data.get('regionName'):
                info['Region'] = data['regionName']
            
            # City / 城市
            if data.get('city'):
                info['City'] = data['city']
            
            # ISP / 互联网服务提供商
            if data.get('isp'):
                info['ISP'] = data['isp']
            
            # Organization / 组织
            if data.get('org'):
                info['Organization'] = data['org']
            
            # AS Number / AS 编号
            if data.get('as'):
                info['AS'] = data['as']
            
            # Timezone / 时区
            if data.get('timezone'):
                info['Timezone'] = data['timezone']
            
            # Coordinates / 坐标
            if data.get('lat') and data.get('lon'):
                info['Coordinates'] = f"{data['lat']}, {data['lon']}"
            
            return info if info else {"error": "No geolocation data found"}
        else:
            return {"error": data.get('message', 'Query failed')}
    
    except requests.RequestException as e:
        return {"error": f"GeoIP lookup failed: {str(e)}"}
    except Exception as e:
        return {"error": f"GeoIP lookup failed: {str(e)}"}


def get_geo_from_domain(domain):
    """
    Get geolocation information from domain name
    从域名获取地理位置信息
    
    Args:
        domain (str): Domain name / 域名
        
    Returns:
        dict: Geolocation information / 地理位置信息字典
    """
    import socket
    
    try:
        # Resolve domain to IP / 将域名解析为 IP
        ip_address = socket.gethostbyname(domain.replace('https://', '').replace('http://', '').split('/')[0])
        
        # Get geolocation / 获取地理位置
        return get_geo_info(ip_address)
    
    except socket.gaierror:
        return {"error": "Could not resolve domain"}
