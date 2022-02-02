import socket
import threading

def user_pool(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            string = data.decode("utf-8")
            conn.send(data)
            print(string)
        except:
            break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.8.106", 8082))
s.listen()

while True:
    conn, addr = s.accept()

    threading.Thread(target=user_pool, args=(conn, addr)).start()
