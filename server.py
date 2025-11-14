from socket import *
import sys
import os
from dotenv import load_dotenv

load_dotenv()


# Creating the TCP socket (connection-oriented)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

while True:
    # Establishing the connection
    print('\nReady to serve...')
    connectionSocket, addr = serverSocket.accept()
    # - connectionSocket: new socket created by the OS for communication with that specific client
    # - addr: address of the client; a tuple containing their IP and port

    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        # Receiving the message from the client (HTTP requisition)
        message = connectionSocket.recv(1024).decode('utf-8')

        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end
        # Envia a linha de status do cabeçalho HTTP
        #Fill in start
        #Fill in end
        # Envia o conteúdo do arquivo ao cliente
        for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        # Fecha a conexão com o cliente
        connectionSocket.close()
    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        #Fill in start
        #Fill in end
        # Fecha o socket do cliente
        #Fill in start
        #Fill in end
serverSocket.close()
sys.exit() # Encerra o programa