from socket import *
serverName = 'HP-pavillion'
# serverIP = '192.168.128.164'
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
decimalNumber = input('Input a decimal number :')
clientSocket.send(decimalNumber.encode())

# received binary
binaryNumber = clientSocket.recv(1024)
# received hexadecimal
hexadecimal = clientSocket.recv(1024)
# received octadecimal
octadecimal = clientSocket.recv(1024)


print ('Binary :',binaryNumber)
print ('Hexadecimal :',hexadecimal)
print ('Octadecimal :',octadecimal)


bN = input('Input a binary number :')
clientSocket.send(bN.encode())

dN = clientSocket.recv(1024)

print('Decimal :',dN)

clientSocket.close()

