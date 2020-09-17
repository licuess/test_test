import re
from urllib.request import urlopen

"""获取公网IP地址"""
urls = ["http://ip.42.pl/raw", "http://myip.ipip.net", "http://ipinfo.io/ip"]
addrs = [re.findall(r'\d+.\d+.\d+.\d+.', res.read().decode('utf-8'))
         for res in map(urlopen, urls) if res.getcode() == 200]
