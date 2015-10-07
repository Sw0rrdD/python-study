import socket

target_host = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

<<<<<<< HEAD
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n") 

=======
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")
>>>>>>> 018a0ca66b48ddfa9d4c5dfcb4f9dc246228ebf7

response = client.recv(4096)

print response
