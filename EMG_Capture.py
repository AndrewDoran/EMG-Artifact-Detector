import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 12347))
threshold_trigger = 0

while True:
    message = sock.recv(2048)
    parsed = json.loads(message)
    if parsed["data"][4] == 1.0:
        threshold_trigger += 1
        if threshold_trigger % 2 == 1:
            print ("stop") 
            #stop 
        else:
            print ("start")
            #start

        for i in range(0, 13):
            sock.recv(2048)
    
