import socket
import pickle
from random import randint
import os


def connection():
    with socket.socket() as s:
        s.connect(('127.0.0.1', 8000))
        var = decode(data=s.recv(1024), _key=3).split("$")[1]
        print(var)
        return int(var)


def is_primitive_root(g: int, mod: int) -> bool:
    lst = []
    for i in range(mod):
        if (g % mod % mod) not in lst:
            lst.append(g % mod % mod)
        else:
            return False
    return True


def is_prime(number: int | float) -> bool:
    k = 0
    for i in range(2, int(number // 2 + 1)):
        if number % i == 0:
            k += 1
    if k <= 0:
        return True
    return False


def decode(data: bytes, _key: int):
    encode_text = ""
    for i in data.decode():
        encode_text += alphabet[(alphabet.index(i) - _key) % len(alphabet)]
    return encode_text


alphabet = [chr(i) for i in range(65536)]
HOST = '127.0.0.1'
PORT = connection()  # 8080

while True:
    if os.stat("keys.txt").st_size > 0:
        p, g, a, K = open("keys.txt", "r").read().split(";")
        p, g, a, K = int(p), int(g), int(a), int(K)
        break
    else:
        p, g, a = randint(1, 1024), randint(1, 1024), randint(1, 1024)
        print(p, g, a)
        if all([is_prime(p), is_prime((p - 1) / 2), is_prime(g), is_primitive_root(g, p)]):
            break

A = g ** a % p

with socket.socket() as sock:
    sock.connect((HOST, PORT))
    sock.send(pickle.dumps((p, g, A)))

    B = pickle.loads(sock.recv(1024))
    if os.stat("keys.txt").st_size == 0:
        K = B ** a % p
        open("keys.txt", "w").write(str(p) + ";" + str(g) + ";" + str(a) + ";" + str(K))
    print(f"p, g, B, a = {(p, g, B, a)}\nK = {K}")
    print(decode(data=sock.recv(1024), _key=K))
    sock.close()
