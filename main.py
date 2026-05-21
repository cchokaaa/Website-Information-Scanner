"""
Website Information Scanner / 网站信息扫描器
Main entry point for the scanner application
扫描器应用的主入口
"""

from scanner.ip_lookup import get_ip
from scanner.web_info import get_website_info
from scanner.dns_lookup import get_dns_records
from scanner.whois_lookup import get_whois_info
from scanner.port_scanner import scan_ports
from scanner.geoip import get_geo_info


def print_section(title):
    """
    Print a section header with decorative border
    打印带装饰边框的分节标题
    
    Args:
        title (str): Section title / 分节标题
    """
    print(f"\n{'='*50}")
    print(f"  {title}")
    print('='*50)


def main():
    """
    Main function / 主函数
    Interactive website information scanning
    交互式网站信息扫描
    """
    # Get user input / 获取用户输入
    domain = input("Enter website: ").strip()
    
    if not domain:
        print("Error: Please enter a domain")
        return
    
    # ========== Basic Information Section / 基础信息部分 ==========
    print_section("Basic Information")
    
    # Get IP address / 获取 IP 地址
    ip = get_ip(domain)
    print(f"IP Address: {ip}")
    
    # Get website info / 获取网站信息
    info = get_website_info(domain)
    if "error" not in info:
        print(f"Title: {info.get('title', 'N/A')}")
        print(f"HTTP Status: {info.get('status_code', 'N/A')}")
        print(f"Server: {info.get('server', 'N/A')}")
        print(f"HTTPS: {info.get('https', 'N/A')}")
    else:
        print(info["error"])
    
    # ========== GeoIP Section / 地理位置部分 ==========
    if ip and not ip.startswith("Error"):
        print_section("GeoIP Information")
        geo_info = get_geo_info(ip)
        if "error" not in geo_info:
            for key, value in geo_info.items():
                if isinstance(value, list):
                    # Handle list values (e.g., DNS names) / 处理列表值（如 DNS 名称）
                    print(f"{key}:")
                    for v in value:
                        print(f"  - {v}")
                else:
                    print(f"{key}: {value}")
        else:
            print(geo_info["error"])
    
    # ========== DNS Records Section / DNS 记录部分 ==========
    print_section("DNS Records")
    
    dns_info = get_dns_records(domain)
    if "error" not in dns_info:
        for record_type, values in dns_info.items():
            if values:
                print(f"\n{record_type} Records:")
                for v in values:
                    print(f"  - {v}")
    else:
        print(dns_info["error"])
    
    # ========== Whois Information Section / Whois 信息部分 ==========
    print_section("Whois Information")
    
    whois_info = get_whois_info(domain)
    if "error" not in whois_info:
        for key, value in whois_info.items():
            print(f"{key}: {value}")
    else:
        print(whois_info["error"])
    
    # ========== Port Scan Section / 端口扫描部分 ==========
    print_section("Port Scan Results")
    
    port_info = scan_ports(domain)
    if "error" not in port_info:
        print(f"Host: {port_info['host']}")
        print(f"Scanned Ports: {port_info['total_scanned']}")
        print(f"Open Ports Found: {port_info['open_count']}")
        if port_info['open_ports']:
            print("\nOpen Ports:")
            for p in port_info['open_ports']:
                print(f"  - {p['port']}/tcp  {p['service']}")
        else:
            print("\nNo open ports found (from common ports list)")
    else:
        print(port_info["error"])
    
    # End of scan / 扫描结束
    print("\n" + "="*50)


if __name__ == "__main__":
    main()
