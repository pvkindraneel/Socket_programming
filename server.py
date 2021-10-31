import socket
import threading

Header = 64
Port = 5050
Server = socket.gethostbyname(socket.gethostname())
ADDR = (Server, Port)
Format = 'utf-8'
Diss_conn = "!Disconnect"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New connection] {addr} connected.")
    connected = True
    while connected:
        msg_len = conn.recv(Header).decode(Format)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(Format)
            if msg == Diss_conn:
                connected = False
            print(f"[{addr}]  {msg}")
            conn.send("msg Recviced".encode(Format))




def start():
    server.listen()
    print(f"[listeing server] server is listening on {Server}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active connection]  {threading.active_count() - 1}")



print("[Strating] srver is staring....!")
start()
