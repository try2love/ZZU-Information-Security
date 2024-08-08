import socket
import time

while True:
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.sendto(b'ask for time' , ("10.2.1.3" ,5005))
    
    data, addr=s.recvfrom(1024)
    
    print(data.decode())
    s.close( )
    time.sleep(1)
