import socket
import os

working_dir = os.getcwd()

server = socket.socket()

try:
    server.bind(('', 80))
    print("Using port 80")
except OSError:
    server.bind(('', 8080))
    print("Using port 8080")

server.listen(1)

while True:
    conn, addr = server.accept()
    print(addr)
    request = conn.recv(10240).decode().split('\n')

method, url, protocol = request[0].split(' ')
url = os.path.join(working_dir, url[1:])

print(url)

code = "404 Not Found"
body = ""

if os.path.isdir(url):
    url = os.path.join(url, "index.html")

if os.path.isfile(url):
    code = "200 OK"
    body = open(url, 'r').read()

response = f"HTTP/1.1 {code}\n"
response += "Server: my_server_0.1\n"
response += "\n\n"
response += body
conn.send(response.encode())
conn.close()
print('Connection closed\n')