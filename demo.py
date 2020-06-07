from requests import request
import re

info = request("GET", url="http://ip.42.pl/raw")
print(info.content)
# info = request("GET", url="http://myip.ipip.net")
# info = request("GET", url="http://ipinfo.io/ip")
ip_addr = re.findall(r'\d+.\d+.\d+.\d+.', info.text)
print(ip_addr)
