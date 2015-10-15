import socket


class TicServer:

    serverIp = "127.0.0.1"

    def __init__(self, port):
        self.serverPort = port

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((TicServer.serverIp, self.serverPort))
        while True:
            data, addr = sock.recvfrom(2048)
            print("data: ", data)


def main():
    server = TicServer(4242)
    server.run()


if __name__ == '__main__':
    main()
