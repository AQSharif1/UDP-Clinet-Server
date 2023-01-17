import socket 
import sys 
import hashlib
import datetime 

args = sys.argv
c = str.encode;

if len(args) > 1:
    #creating socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    #binding port arg and local IP to ServerSocket
    port = int(args[1])
    localIPAdd = "127.0.0.1"
    UDPServerSocket.bind((localIPAdd, port))
    
    print("Listening on port", port)
    print("Waiting ...")
    while (True):
        #time of received client message
        receivedTime = datetime.datetime.now()
        bytesAddressPair = UDPServerSocket.recvfrom(1024)
        
        #store message and output receive time
        print("*** new message ***")
        print("Received time:", receivedTime)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        
        #get checksum
        checksum = hashlib.md5(message).hexdigest()
        
        #client message 
        
        clientMessage = "Received message:\n{}".format(message.decode())
        print(clientMessage)
        print("Received checksum:", checksum)
        print("Calculated checksum:", checksum)
        print("\nWaiting...")

        UDPServerSocket.sendto(c("server successfully received the message at " + str(receivedTime)), address)
else:
    print("404 ERROR")