from utility import Utility

if __name__ == "__main__":
    utility = Utility()
    utility.send_socket_msg("Hello world !!")
    utility.send_socket_msg("Hello everyone")
    utility.send_socket_msg(utility.Dis_con)
