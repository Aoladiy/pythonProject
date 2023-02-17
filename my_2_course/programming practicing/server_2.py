import socket
import threading

port1 = 8082


def server(host='localhost', port=port1):
    try:
        print("Запуск сервера")
        with socket.socket() as s:

            s.bind((host, port))
            print("Начало прослушивания порта")
            s.listen()
            print("Подключение клиента")
            while True:
                conn, addr = s.accept()
                thread = threading.Thread(target=echo, args=[conn])
                thread.start()
                print("Поток создан")



    except KeyboardInterrupt:
        exit(0)


def echo(conn):
    while True:
        print("Приём данных у клиента")
        data = conn.recv(1024)

        if not data:
            break
        print("Отправка данных клиенту")
        conn.send(data)
    conn.close()
    print("Отключение клиента")
    conn.close()
    print("Отключение сервера")



if __name__ == '__main__':
    server()
