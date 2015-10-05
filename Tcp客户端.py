import socket

target_host = "www.baidu.com"
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

<<<<<<< HEAD
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n") 
=======
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")
>>>>>>> a187d5e012d50fc02b6694a6f55a8c4468934192

response = client.recv(4096)

print response