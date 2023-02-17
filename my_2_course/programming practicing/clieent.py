import socket

import server_2


def user(host='localhost', port=server_2.port1):
    try:
        with socket.socket() as s:
            print("Соединение с сервером")
            s.connect((host, port))
            while True:
                inp = input("Ввод: ")
                if inp == "exit":
                    s.close()
                    print("Разрыв соединения с сервером")
                    break
                print("Отправка данных серверу")
                s.send(inp.encode())
                print("Прием данных от сервера")
                data = s.recv(1024)
                print('Вывод: ', data.decode())

    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    user()
