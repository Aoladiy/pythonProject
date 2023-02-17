import socket
web = socket.socket()
web.connect(('google.com', 80))
msg = """GET / HTTP/1.1
Host: google.com
User-Agent: my_first_web_client

"""
web.send(msg.encode())
response = web.recv(1024).decode()
web.close()
print(response)
