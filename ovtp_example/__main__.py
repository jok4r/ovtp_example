from ovtp_example import Client
from ovtp_example import Server
import sys


def main():
    if len(sys.argv) < 2:
        print('Usage:')
        print('python3 -m ovtp_example server')
        print('\nOR\n')
        print('python3 -m ovtp_example client [server_ip]')
        return
    if sys.argv[1] == 'client':
        client = Client(sys.argv[2])
        client.run()
    elif sys.argv[1] == 'server':
        server = Server()
        server.run()
    else:
        print("Error! Unknown run mode")


main()
