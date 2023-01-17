import socket 
import sys 
import hashlib
import time
import datetime

args = sys.argv
c = str.encode

if len(args) >= 4:
    #Creating socket and arguments
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    arg1 = sys.argv[1]
    arg2 = int(sys.argv[2])
    arg3 = sys.argv[3]
    
    receivedTime = datetime.datetime.now()
    bytesSending = c(arg3)
    addressPort = (arg1, arg2)
    
    #sent Message to server
    UDPClientSocket.sendto(bytesSending, addressPort)
    receivedMsg = UDPClientSocket.recvfrom(1024)
    time1 = time.time()
    
    #Checksum calculated and Printed
    checksum = hashlib.md5(arg3.encode()).hexdigest()
    print("Checksum sent:", checksum)
  
  #returned message from server
    message = receivedMsg[0].decode()
    print(message)
    time2 = time.time()
    rtt = str(time2 - time1);
    print("Rtt: " + rtt + "US ")