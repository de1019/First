# import socket module
from socket import *
import sys  # In order to terminate the program


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    # Fill in start
    serverSocket.bind(('', port))
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # added "serverSocket.accept()" here
        try:
            message = connectionSocket.recv(2048).decode()  # added "connectionSocket.recv(2048).decode()" here
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()  # added ".read()" here
            f.close()  # Added "f.close()" here

            # Send one HTTP header line into socket
            # Fill in start
            goodConnect = 'HTTP/1.1 200 OK\r\n\r\n'
            connectionSocket.send(goodConnect.encode())
            # Fill in end

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            # Send response message for file not found (404)
            # Fill in start
            badConnect = 'HTTP/1.1 404 FILE NOT FOUND\r\n'
            connectionSocket.send(badConnect.encode())
            # Fill in end

            # Close client socket
            # Fill in start\
            closeConnect = 'Connection: close\r\n'
            connectionSocket.send(closeConnect.encode())
            # Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
