#!/usr/bin/python3

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)


while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body><h1>Hello World!+<img src = http://cdn.skim.gs/images/homer-simpson-doughnuts/what-homer-simpson-taught-us-about-doughnuts></h1></body></html>" +
                    "\r\n", 'utf-8'))
    recvSocket.close()
