import socket


Header = 64
Port = 5050
Server = socket.gethostbyname(socket.gethostname())
ADDR = (Server, Port)
Format = 'utf-8'
Diss_conn = "!Disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


def send(msg):
    message = msg.encode(Format)
    msg_len = len(message)
    send_lenght = str(msg_len).encode(Format)
    send_lenght += b' ' * (Header - len(send_lenght))
    print(send_lenght)
    print(message)
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048))


send("Hello world !!")
send("Hello everyone")
send(Diss_conn)