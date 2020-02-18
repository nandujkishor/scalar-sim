import socket
import select
import sys
from _thread import *
import random
import time

# c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip = input()
# port = int(input())
# ip, port = '127.0.0.1', 7788
# c.connect((ip, port))

def send_message(c):
    msg = "EVENT " + str(t)
    c.send(msg.encode('ascii'))
    # print("Sending message to "+c.getpeername()[0]+" from "+s.getpeername()[0])

def int_event():
    global t
    t += 1
    print("Internal event (Time: "+str(t)+")")

def ext_event(ip, port):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((ip, port))
    global t
    t += 1
    print("Send event (Time: "+str(t)+")")

    send_message(c)

def ext_event_run():
    global cport
    cport = peers[random.randrange(len(peers))]
    ext_event("localhost", cport)

def incoming_ext_event(nt):
    global t
    t = max(t, nt) + 1
    print("Receive event (Time: "+str(t)+")")

def events():
    while(1):
        k = random.randrange(2)
        if k: int_event()
        else: ext_event_run()
        time.sleep(random.randint(1, 3))

t = 0

s = socket.socket()
print("Please enter the server port ")
port = int(sys.argv[1])
s.bind(('', port))
s.listen(10)
print("socket binded to "+str(port))

peers = []

for peer in sys.argv[2:]:
    if peer == sys.argv[1]: continue
    peers.append(int(peer))

time.sleep(5)

start_new_thread(events, ())
while(1):
    c, addr = s.accept()
    nt = c.recv(2048).decode().split()[1]
    incoming_ext_event(int(nt))

s.close()