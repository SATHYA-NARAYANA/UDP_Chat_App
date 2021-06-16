import os
import socket
import threading
os.system("clear")
os.system("tput setaf 5")
print("***********************  UDP  CHAT APP ******************")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "192.168.43.113"
port = 1234

sendip = input("\n\n\n\t Please Enter Receiver IP:")
sendport = 1234

s.bind((ip, port))

def send():
    while True:
        x = input("")
        s.sendto(x.encode(), (sendip, sendport))
        if (("bye" in x) or ("exit" in x)):
            os._exit(1)

def receive():
    while True:
        x = s.recvfrom(1024)
        print("\n\n\n\t"+"{} :".format(sendip) + x[0].decode())

send = threading.Thread( target=send)
receive = threading.Thread( target=receive)

send.start()
receive.start()
