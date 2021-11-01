import socket
import threading
import json


class Utility:
    def __init__(self):
        try:
            config_data = json.load(open("config.json"))
            self.header = 64
            self.port = config_data["socket"]["port"]
            self.Format = config_data["socket"]["format"]
            self.socket_server_con = socket.gethostbyname(socket.gethostname())
            self.Dis_con = "!Disconnect"
            self.addr = (self.socket_server_con, self.port)
        except Exception as e:
            print(f"Connection Failed....!!!!! {e}")

    def socket_server_connection(self):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(self.addr)
            server.listen()
            print(f"[listening server] server is listening on {self.socket_server_con}")
            while True:
                conn, addr = server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                print(f"[Active connection]  {threading.active_count() - 1}")
        except Exception as e:
            print(f"socket server connection failed {e}")

    def handle_client(self, conn, addr):
        try:
            print(f"[New connection] {addr} connected.")
            connected = True
            while connected:
                msg_len = conn.recv(self.header).decode(self.Format)
                if msg_len:
                    msg_len = int(msg_len)
                    msg = conn.recv(msg_len).decode(self.Format)
                    if msg == self.Dis_con:
                        connected = False
                    print(f"[{addr}]  {msg}")
                    conn.send("msg Received".encode(self.Format))
        except Exception as e:
            print(f"socket server while handle client failed {e}")

    def send_socket_msg(self, msg):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(self.addr)
            message = msg.encode(self.Format)
            msg_len = len(message)
            send_length = str(msg_len).encode(self.Format)
            send_length += b' ' * (self.header - len(send_length))
            print(send_length)
            print(message)
            client.send(send_length)
            client.send(message)
            print(client.recv(2048))
        except Exception as e:
            print(str(e))
