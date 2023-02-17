import time
import socket
import threading
import os

port1 = 8082


def server(host='localhost', port=port1):
    try:

        if not os.path.isdir(os.path.join(os.getcwd(), "server")):
            os.mkdir(os.path.join(os.getcwd(), "server"))

        if not os.path.isfile(os.path.join(os.getcwd(), "logins")):
            open(os.path.join(os.getcwd(), "logins"), "w").close()

        if not os.path.isfile(os.path.join(os.getcwd(), "logs")):
            open(os.path.join(os.getcwd(), "logs"), "w").close()

        print(">>> Запуск сервера")
        with open('logs', 'a') as log:
            log.write(str(time.localtime()) + " " + ">>> Запуск сервера\n")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.bind((host, port))
            print(">>> Начало прослушивания порта")

            with open('logs', 'a') as log:
                log.write(str(time.localtime()) + " " + ">>> Начало прослушивания порта\n")

            sock.listen()
            print(">>> Подключение клиента")

            with open('logs', 'a') as log:
                log.write(str(time.localtime()) + " " + ">>> Подключение клиента\n")

            while True:
                conn, addr = sock.accept()
                thread = threading.Thread(target=echo, args=[conn])
                thread.start()
                with open('logs', 'a') as log:
                    log.write(str(time.localtime()) + " " + "Поток создан\n")
                print("Поток создан")

    except KeyboardInterrupt:
        exit(0)


def echo(conn):
    while True:

        data = conn.recv(1024)

        if not data:
            break

        request = data.decode()
        response = process(request, conn)

        try:
            response = response.encode()
            conn.send(response)
        except AttributeError:
            conn.send("done".encode())

    conn.close()


def process(req, conn=None):
    with open('logs', 'a') as log:
        log.write(str(time.localtime()) + " " + req + "\n")

    req = req.split()
    wway = os.path.join(os.getcwd(), "server")
    if len(req) == 2:
        req[1] = os.path.join(wway, req[1])
    elif len(req) == 3:
        req[1] = os.path.join(wway, req[1])
        req[2] = os.path.join(wway, req[2])
    if req[0] == 'pwd':
        return os.getcwd()
    elif req[0] == 'ls':
        return '; '.join(os.listdir())
    elif req[0] == 'mkdir' and not os.path.isdir(req[1]):
        os.mkdir(req[1])
    elif req[0] == 'rmdir' and os.path.isdir(req[1]):
        return os.rmdir(req[1])
    elif req[0] == 'rmfile' and os.path.isfile(req[1]):
        return os.remove(req[1])
    elif req[0] == 'mkfile' and not os.path.isfile(req[1]):
        return open(req[1], 'w').close()
    elif req[0] == 'rename' and (os.path.isdir(req[1]) or os.path.isfile(req[1])):
        return os.rename(req[1], req[2])

    elif req[0] == 'copy2client':

        file = open(req[1], 'rb').read() + """Test Data ...""".encode()
        conn.send(file)

    elif req[0] == 'copy2server':
        open(req[1], "wb").write(conn.recv(1024 * 10))

    else:
        with open('logs', 'a') as log:
            log.write(str(time.localtime()) + " " + "bad request\n")
            print('bad request')
        return 'bad request'


if __name__ == '__main__':
    server()
