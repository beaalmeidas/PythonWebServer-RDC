from socket import * 
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Creating the TCP socket for the connection
serverSocket = socket(AF_INET, SOCK_STREAM) 

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
print(f"\n--- Server running at http://{HOST}:{PORT}\n")
print(f"\n--- Test connection at http://{HOST}:{PORT}/index.html\n")

try:
    while True: 
        print('Ready to serve...') 
        connectionSocket, addr = serverSocket.accept()
        # - connectionSocket: new socket created by the OS for communication with that specific client
        # - addr: address of the client; a tuple containing their IP and port

        try: 
            # Getting the http requisition from the client
            message = connectionSocket.recv(1024).decode()

            filename = message.split()[1]
            f = open(filename[1:]) 
            outputdata = f.read()
            f.close()

            # Sending the http status to the client
            response = "HTTP/1.1 200 OK\r\n\r\n" + outputdata
            connectionSocket.sendall(response.encode())

            connectionSocket.close()
        except IOError:
            response = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
            connectionSocket.close()

except KeyboardInterrupt:
    print("\nEnding server...")

finally:
    serverSocket.close()
    sys.exit()