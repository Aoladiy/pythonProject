import os
import socket
import server


def user(host='localhost', port=server.port1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(">>> Соединение с сервером")
            s.connect((host, port))
            login = input("Your login: ")

            with open('logins', 'r') as logins:
                logins_data = logins.read()

            if login not in logins_data:
                with open('logins', 'a') as logins:
                    logins.write(login)
                try:
                    os.mkdir(login)
                except:
                    pass

            while True:
                if login == "":
                    inp = input("myftp@shell$ ")
                    login = "client"
                else:
                    inp = input(f"{login}@shell$ ")

                if inp == "exit":
                    s.close()
                    print(">>> Разрыв соединения с сервером")
                    break

                print(">>> Отправка данных серверу")
                print('test2', inp)
                s.send(inp.encode())

                wway = os.getcwd()

                if inp.split()[0] == "copy2client":
                    way = os.path.join(wway, login)
                    way2 = os.path.join(way, inp.split("\\")[-1])
                    print('way2', way2)
                    with open(way2, "wb") as f:
                        f.write(s.recv(1024))

                    print(">>> Прием данных от сервера")
                    data = s.recv(1024)
                    print(data.decode())
                    continue

                if inp.split()[0] == "copy2server":
                    way1 = os.path.join(way, inp.split()[1])
                    file = open(way1, 'rb').read() + """Test Data 2 ...""".encode()
                    s.send(file)

                print(">>> Прием данных от сервера")
                data = s.recv(1024)
                print(data.decode())

    except KeyboardInterrupt:
        exit(0)


def check(host='localhost', port=server.port1):  # Отладка
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(">>> Соединение с сервером")
            s.connect((host, port))
            login = "Check"
            wway = os.getcwd()
            with open('logins', 'r') as logins:
                logins_data = logins.read()

            if login not in logins_data:
                with open('logins', 'a') as logins:
                    logins.write(login)
                try:
                    os.mkdir(login)
                except OSError:
                    pass

            for inp in ['pwd', 'ls', 'mkdir test', f'mkfile {os.path.join("test", "123.txt")}',
                        f'rename {os.path.join("test", "123.txt")} {os.path.join("test", "test.txt")}',
                        f'copy2client {os.path.join("test", "test.txt")}', f'rmfile {os.path.join("test", "test.txt")}',
                        'rmdir test', 'exit']:

                if inp == "exit":
                    s.close()
                    print(">>> Разрыв соединения с сервером")
                    break

                print(">>> Отправка данных серверу")
                print('test2', inp)
                s.send(inp.encode())

                if inp.split()[0] == "copy2client":
                    way = os.path.join(wway, login)
                    way2 = os.path.join(way, inp.split("\\")[-1])
                    print('way2', way2)
                    with open(way2, "wb") as f:
                        f.write(s.recv(1024))

                    print(">>> Прием данных от сервера")
                    data = s.recv(1024)
                    print(data.decode())
                    continue

                if inp.split()[0] == "copy2server":
                    way1 = os.path.join(way, inp.split()[1])
                    file = open(way1, 'rb').read() + """Test Data 2 ...""".encode()
                    s.send(file)

                print(">>> Прием данных от сервера")
                data = s.recv(1024)
                print(data.decode())

    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    user()