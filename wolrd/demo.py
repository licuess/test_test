from requests import request

# info = request("GET", url="http://ip.42.pl/raw")
# info = request("GET", url="http://myip.ipip.net")
info = request("GET", url="http://ipinfo.io/ip")
print([info.text])