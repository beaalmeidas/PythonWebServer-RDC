from socket import *
import sys
import os
from dotenv import load_dotenv

load_dotenv()


# Creating the TCP socket (connection-oriented)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
#Fill in start
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
#Fill in end

while True:
    # Estabelece a conexão
    print('\nReady to serve...')
    connectionSocket, addr = serverSocket.accept()
    """
        - connectionSocket: new socket created by the OS for communication with that specific client
    """

    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        message = 

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