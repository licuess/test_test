from json import load
from urllib.request import urlopen

my_ip = urlopen("http://ip.42.pl/raw").read()
print("ip.42.pl: %s" % my_ip)

my_ip = load(urlopen("http://jsonip.com"))["ip"]
print("jsonip.com: %s" % my_ip)

my_ip = load(urlopen("http://httpbin.org/ip"))["origin"]
print("httpbin.org: %s" % my_ip)

my_ip = load(urlopen("https://api.ipify.org/?format=json"))["ip"]
print("api.ipify.org: %s" % my_ip)