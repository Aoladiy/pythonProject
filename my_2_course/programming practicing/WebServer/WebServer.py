import datetime
import socket
import os
import threading

settings = open("settings.txt", "r").read().split()

working_dir = os.getcwd()

server = socket.socket()

try:
    server.bind(('', int(settings[0])))
    print(f"Using port {settings[0]}")
except OSError:
    server.bind(('', 8080))
    print("Using port 8080")

server.listen(1)


def f(conn, addr):
    try:
        request = conn.recv(int(settings[2])).decode().split('\n')
        try:
            method, url, protocol = request[0].split(' ')
        except:
            return 0
        url = os.path.join(working_dir, url[1:])
        print(url)
        code = "404 Not Found"
        body = ""

        if os.path.isdir(url):
            url = os.path.join(url, "index1.html")
            print('123', url)

        if os.path.isfile(url):
            code = "200 OK"
            print('321', url)
            body = open(url, 'r').read()
            # body = codecs.open(url, 'r', "utf_8_sig").read()
        time = datetime.datetime.now()
        response = f"HTTP/1.1 {code}\n" + "Server: my_server_0.1\n" + """Date: {time.strftime("%a, %d %b %Y %H:%M:%S")}
        Server: SelfMadeServer v0.0.1
        Content-Length: {len(HtmlVar)}
        Content-Type: text/html
        Connection: close""" + "\n\n" + body

        conn.send(response.encode())
        with open("loggs.txt", "a") as loggs:
            loggs.write(f"{time} + {addr} + {url} +{code}" + "\n")
        conn.close()
        print('Connection closed\n')
        return 0
    except UnicodeDecodeError:
        return 0


while True:
    conn, addr = server.accept()
    print(addr)

    threading.Thread(target=f, args=[conn, addr]).run()
