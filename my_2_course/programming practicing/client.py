import socket
import threading


def send_message(sock, data):
    sock.send(data.encode())


def receive_message(sock, chrs):
    data = sock.recv(chrs).decode()
    return data


def receiving():
    while True:
        data = sock.receive_message(1024)
        with block:
            print(data)


socket.socket.send_message = send_message
socket.socket.receive_message = receive_message

block = threading.Lock()
sock = socket.socket()
sock.setblocking(1)

host_inp = str(input('Введите хост: '))
port_inp = int(input('Введите порт: '))

host, port = host_inp, port_inp
print(f"Подключение к порту {port}")
sock.connect((host, port))
print("Успешно подключено к серверу")

threading.Thread(target=receiving, daemon=True).start()
while True:
    msg = input()
    sock.send_message(msg)
    if msg == "exit":
        break

print("Отключение от сервера")
sock.close()
