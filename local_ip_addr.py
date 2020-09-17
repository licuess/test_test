import socket
from urllib.request import urlopen

# host_name


print(socket.gethostname())

# local_host_ip
print(socket.gethostbyname(socket.gethostname()))

# addr_info
addr_info = socket.getaddrinfo(socket.gethostname(), None)
print(addr_info)

