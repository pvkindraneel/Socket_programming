from utility import Utility

if __name__ == "__main__":
    print("[Starting] server is staring....!")
    utility = Utility()
    socketserver = utility.socket_server_connection()
