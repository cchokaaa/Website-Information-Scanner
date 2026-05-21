"""
Whois Lookup Module / Whois 查询模块
Query domain registration information
查询域名注册信息
"""

import whois


def get_whois_info(domain):
    """
    Get Whois registration information for a domain
    获取域名的 Whois 注册信息
    
    Args:
        domain (str): Domain name / 域名
        
    Returns:
        dict: Whois information dictionary / Whois 信息字典
    """
    try:
        # Clean domain name / 清理域名
        # Remove protocol prefixes / 移除协议前缀
        domain = domain.replace('https://', '').replace('http://', '').replace('www.', '')
        if '/' in domain:
            domain = domain.split('/')[0]
        
        # Query Whois database / 查询 Whois 数据库
        w = whois.whois(domain)
        
        info = {}
        
        # Domain name / 域名
        if w.domain_name:
            info['Domain Name'] = w.domain_name if isinstance(w.domain_name, str) else ', '.join(w.domain_name)
        
        # Registrar / 注册商
        if w.registrar:
            info['Registrar'] = w.registrar
        
        # Creation date / 创建日期
        if w.creation_date:
            date = w.creation_date if isinstance(w.creation_date, str) else w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
            info['Creation Date'] = str(date)[:19] if date else 'N/A'
        
        # Expiration date / 过期日期
        if w.expiration_date:
            date = w.expiration_date if isinstance(w.expiration_date, str) else w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date
            info['Expiration Date'] = str(date)[:19] if date else 'N/A'
        
        # Updated date / 更新日期
        if w.updated_date:
            date = w.updated_date if isinstance(w.updated_date, str) else w.updated_date[0] if isinstance(w.updated_date, list) else w.updated_date
            info['Updated Date'] = str(date)[:19] if date else 'N/A'
        
        # Name servers / 名称服务器
        if w.name_servers:
            info['Name Servers'] = w.name_servers if isinstance(w.name_servers, list) else w.name_servers
        
        # Domain status / 域名状态
        if w.status:
            info['Status'] = w.status if isinstance(w.status, str) else ', '.join(w.status)
        
        # Registrar email / 注册商邮箱
        if w.emails:
            info['Registrar Email'] = w.emails[0] if isinstance(w.emails, list) else w.emails
        
        # Country / 国家
        if w.country:
            info['Country'] = w.country
        
        return info if info else {"error": "No Whois data found"}
        
    except whois.parser.PywhoisError:
        return {"error": "Domain not found in Whois database"}
    except Exception as e:
        return {"error": f"Whois lookup failed: {str(e)}"}
