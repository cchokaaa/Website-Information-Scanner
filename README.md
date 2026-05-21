# Website Information Scanner

## 中文介绍

Website Information Scanner 是一个使用 Python 开发的网站信息收集工具。

### 功能列表

| 功能 | 说明 |
|------|------|
| IP 查询 | 域名解析为 IP 地址 |
| 网站标题获取 | 提取网页 title 标签内容 |
| HTTP 状态检测 | 获取 HTTP 响应状态码 |
| 服务器类型识别 | 从响应头获取 Server 信息 |
| HTTPS 检测 | 检查是否启用 HTTPS |
| DNS 查询 | 查询 A、AAAA、MX、NS、TXT、CNAME 记录 |
| Whois 查询 | 获取域名注册信息 |
| 端口扫描 | 扫描常用端口并识别服务 |
| GeoIP 地理位置 | IP 地址归属地查询 |

## English Introduction

Website Information Scanner is a Python-based website information gathering tool.

### Features

| Feature | Description |
|---------|-------------|
| IP Lookup | Resolve domain to IP address |
| Website Title | Extract page title tag content |
| HTTP Status | Get HTTP response status code |
| Server Identification | Get server info from response headers |
| HTTPS Detection | Check HTTPS availability |
| DNS Lookup | Query A, AAAA, MX, NS, TXT, CNAME records |
| Whois Lookup | Get domain registration info |
| Port Scanning | Scan common ports and identify services |
| GeoIP Geolocation | IP address geolocation lookup |

## 如何使用 / How to Use

```bash
# Install dependencies / 安装依赖
pip install -r requirements.txt

# Run the program / 运行程序
python main.py

# Enter website to scan / 输入要查询的网站
Enter website: baidu.com
```

### 中文显示问题 / Chinese Display Fix

If Chinese title shows garbled characters, set terminal encoding before running:

如果中文标题显示乱码，请在运行前设置终端编码：

```bash
# Linux/Mac
export LANG=zh_CN.UTF-8
python main.py

# Windows CMD
chcp 65001
python main.py

# Windows PowerShell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
python main.py
```

## 更新日志 / Changelog

### 第二次更新 (2026-05-21) / Second Update (2026-05-21)

#### 新增功能 / New Features

- **GeoIP 地理位置查询** / **GeoIP Module** - `scanner/geoip.py` - 查询 IP 归属地、国家、城市、ISP、AS 编号等 / Query IP geolocation including country, city, ISP, AS number
- **DNS 查询模块** / **DNS Lookup Module** - `scanner/dns_lookup.py` - 查询 A、AAAA、MX、NS、TXT、CNAME 记录 / Query A, AAAA, MX, NS, TXT, CNAME records
- **Whois 查询模块** / **Whois Lookup Module** - `scanner/whois_lookup.py` - 获取域名注册信息、注册商、日期、名称服务器 / Get domain registration info, registrar, dates, name servers
- **端口扫描模块** / **Port Scanner Module** - `scanner/port_scanner.py` - 多线程扫描 20 个常用端口，自动识别服务 / Multi-threaded scanning of 20 common ports with service identification

#### 代码优化 / Code Improvements

- 所有代码文件添加完整的中英文注释 / All code files added complete Chinese and English comments
- 所有模块添加模块级文档字符串 / All modules added module-level docstrings
- 所有函数添加参数和返回值说明 / All functions added parameter and return value documentation

### 第一次更新 (2026-05-20) / First Update (2026-05-20)

#### 原有功能 / Original Features

| 功能 / Feature | 说明 / Description |
|----------------|---------------------|
| IP 查询 / IP Lookup | 域名解析为 IP 地址 / Resolve domain to IP address |
| 网站标题获取 / Website Title | 提取网页 title 标签内容 / Extract page title tag content |
| HTTP 状态检测 / HTTP Status | 获取 HTTP 响应状态码 / Get HTTP response status code |
| 服务器类型识别 / Server Identification | 从响应头获取 Server 信息 / Get server info from response headers |
| HTTPS 检测 / HTTPS Detection | 检查是否启用 HTTPS / Check HTTPS availability |

## 项目结构 / Project Structure

```
.
├── main.py                 # Main entry point / 主入口
├── requirements.txt        # Dependencies list / 依赖列表
├── LICENSE                # MIT License / MIT 许可证
├── README.md              # Documentation / 说明文档
├── .gitignore             # Git ignore rules / Git 忽略规则
└── scanner/
    ├── ip_lookup.py        # IP address lookup / IP 地址查询
    ├── web_info.py         # Website info retrieval / 网站信息获取
    ├── dns_lookup.py       # DNS record lookup / DNS 记录查询
    ├── whois_lookup.py     # Whois info lookup / Whois 信息查询
    ├── port_scanner.py     # Port scanning / 端口扫描
    └── geoip.py            # IP geolocation / IP 地理位置
```

## 依赖 / Dependencies

```
requests>=2.25.0
beautifulsoup4>=4.9.0
dnspython>=2.0.0
python-whois>=0.9.0
ipwhois>=1.3.0
```

## 注意事项 / Notes

1. Some features require network connection / 部分功能需要网络连接
2. Port scanning only scans common ports by default / 端口扫描仅扫描常用端口
3. Whois results depend on registry data availability / Whois 查询结果受注册局数据限制
