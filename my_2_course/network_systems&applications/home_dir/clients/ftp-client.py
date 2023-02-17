import socket
import os

HOST = 'localhost'
PORT = 9090

while True:
    try:
        request = input('ftp>')
        try:
            if request.split()[0] == 'cpcs':
                request = request.split()
                request[1] = os.path.join(os.getcwd(), request[1])
                request = ' '.join(request)
            elif request.split()[0] == 'cpsc':
                if len(request.split()) == 2:
                    request = request.split()
                    request.append(os.getcwd())
                    request = ' '.join(request)
                elif len(request.split()) == 3:
                    request = request.split()
                    request[2] = os.path.join(os.getcwd(), request[2])
                    request = ' '.join(request)
        except:
            continue
    except:
        break

    sock = socket.socket()

    try:
        sock.connect((HOST, PORT))
    except:
        break

    if request == '':
        continue

    sock.send(request.encode())

    try:
        response = sock.recv(1024).decode()
    except:
        break

    if response == 'exit' or response == 'cstop':
        break

    print(response)

    sock.close()
