import socket
import pickle
from random import randint


def connection(port):
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 8000))
        sock.listen(1)
        c, a = sock.accept()
        c.send(str(encode(str(port), 3)).encode())
        print(str(encode(str(port), 3)))


def encode(data: str, key: int) -> bytes:
    encode_text = ""
    for i in data:
        encode_text += alphabet[(alphabet.index(i) + key) % len(alphabet)]
    return encode_text.encode()


alphabet = [chr(i) for i in range(65536)]  # Алфавит
text = "Gaudeāmus igĭtur, Juvĕnes dum sumus!"
HOST = '127.0.0.1'
PORT = 9090

connection(PORT)

with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()

    if int(addr[1]) > 2000:
        g, p, A = pickle.loads(conn.recv(1024))
        print("recv done")
        if g in range(1, 1024 + 1) and p in range(1, 1024 + 1) and A in range(0, 1024 + 1):
            b = randint(1, 64)
            B = g ** b % p
            K = A ** b % p
            conn.send(pickle.dumps(B))
            print("send done")
            print(f"p, g, A, b = {(g, p, A, b)}\nK = {K}")
            conn.send(encode(data=text, key=K))
        else:
            print("Ключ вне утверждённого диапазона значений")
    else:
        print("Порт вне утверждённого диапазона значений")

    conn.close()
