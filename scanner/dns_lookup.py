"""
DNS Lookup Module / DNS 查询模块
Query various DNS records for a domain
查询域名的各种 DNS 记录
"""

import socket
import subprocess
import re


def get_dns_records(domain):
    """
    Get DNS records for a domain (A, AAAA, MX, NS, TXT, CNAME)
    获取域名的 DNS 记录（A、AAAA、MX、NS、TXT、CNAME）
    
    Args:
        domain (str): Domain name / 域名
        
    Returns:
        dict: DNS records dictionary / DNS 记录字典
    """
    records = {}
    
    # Record types to query / 要查询的记录类型
    record_types = ['A', 'MX', 'NS', 'TXT', 'CNAME']
    
    for record_type in record_types:
        try:
            # Use nslookup command / 使用 nslookup 命令
            cmd = f'nslookup -type={record_type} {domain}'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            output = result.stdout
            
            if record_type == 'A':
                # Parse IP addresses / 解析 IP 地址
                ips = []
                lines = output.split('\n')
                for i, line in enumerate(lines):
                    if 'Addresses:' in line or 'Address:' in line:
                        # Get IP after the label / 获取标签后的 IP
                        parts = line.split(':', 1)
                        if len(parts) > 1:
                            ip = parts[1].strip()
                            if ip and ip != domain and not ip.startswith('#'):
                                ips.append(ip)
                        # Also check next lines for additional IPs / 也检查后续行的 IP
                        for j in range(i+1, len(lines)):
                            next_line = lines[j].strip()
                            if next_line and not next_line.startswith('#') and not '=' in next_line:
                                if re.match(r'^\d+\.\d+\.\d+\.\d+$', next_line):
                                    ips.append(next_line)
                # Filter out DNS server IPs / 过滤掉 DNS 服务器 IP
                dns_server_ips = ['114.114.114.114', '8.8.8.8', '1.1.1.1', '8.8.4.4', '1.0.0.1']
                ips = [ip for ip in ips if ip not in dns_server_ips]
                records['A'] = list(set(ips)) if ips else []
                
            elif record_type == 'MX':
                # Parse mail servers / 解析邮件服务器
                mxs = []
                for line in output.split('\n'):
                    if 'mail exchanger' in line.lower():
                        mxs.append(line.strip())
                records['MX'] = mxs if mxs else []
                
            elif record_type == 'NS':
                # Parse name servers / 解析名称服务器
                nss = []
                for line in output.split('\n'):
                    if 'nameserver' in line.lower():
                        parts = line.split('=')
                        if len(parts) > 1:
                            nss.append(parts[1].strip())
                        else:
                            parts = line.split('nameserver')
                            if len(parts) > 1:
                                nss.append(parts[1].strip())
                records['NS'] = nss if nss else []
                
            elif record_type == 'TXT':
                # Parse TXT records / 解析 TXT 记录
                txts = []
                for line in output.split('\n'):
                    if 'text =' in line.lower() or 'text:' in line.lower():
                        parts = line.split('=', 1) if '=' in line else line.split(':', 1)
                        if len(parts) > 1:
                            txt = parts[1].strip().strip('"')
                            if txt:
                                txts.append(txt)
                records['TXT'] = txts if txts else []
                
            elif record_type == 'CNAME':
                # Parse CNAME records / 解析 CNAME 记录
                cnames = []
                for line in output.split('\n'):
                    if 'canonical name' in line.lower():
                        parts = line.split('=')
                        if len(parts) > 1:
                            cnames.append(parts[1].strip())
                records['CNAME'] = cnames if cnames else []
                
        except subprocess.TimeoutExpired:
            records[record_type] = [f"Error: Timeout"]
        except Exception as e:
            records[record_type] = [f"Error: {str(e)}"]
    
    return records
