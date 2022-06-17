from socket import *
serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

serverSocket.listen(3)
print ('The server is ready to receive on port : '+str(serverPort))
while True:
     connectionSocket, addr = serverSocket.accept()
     
     print('Connection established.....')
     decimal = connectionSocket.recv(1024).decode()
     decimalNumber = decimal.upper()
     n = int(decimalNumber)

     binaryNumber = bin(n)
     hexadecimal = hex(n)
     octadecimal = oct(n)
     
     connectionSocket.send(binaryNumber.encode())
     connectionSocket.send(hexadecimal.encode())
     connectionSocket.send(octadecimal.encode())

     # for binary stuff
     ReceivedBinaryNumber = connectionSocket.recv(1024).decode()
     bn = ReceivedBinaryNumber.upper()
     intBinary = int(bn)
     result = int(str(intBinary),2)
     connectionSocket.send(repr(result).encode())

     # for hexadecimal stuff
     ReceivedHexaNumber = connectionSocket.recv(1024).decode()
     hn = ReceivedHexaNumber.upper()
     intHexa = int(hn)
     hres = int(str(intHexa),6)

     connectionSocket.send(repr(hres).encode())
     connectionSocket.close()

