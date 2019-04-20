#!/usr/bin/python

import socket,sys,os
from threading import Thread
if len(sys.argv) != 2:
    print "use:",sys.argv[0],"IP"
    print "for example ./test.py /root/ip.txt"

def getBanner(ip,port):
    socket.setdefaulttimeout(2)
    s=socket.socket()
    try:
        s.connect((ip,21))
        result=s.recv(1024)   
        s.close()
        return result
    except:
        pass

def checkVulns(ip,port):
    banner=getBanner(ip,port)
    if (banner):
        if("2.3.4" in banner):
            print ip,"vulnerable"
        else:
            print ip,"unvulnerable"
    else:
        print ip,"not get banner"
        
def main():
    filename=str(sys.argv[1]).strip()
    if not os.path.exists(filename):
            print"not exist"
            sys.exit()

    f=open(filename,"r")
    for i in f.readlines():
        ip=i.strip("\n")
        port=21
        t=Thread(target=checkVulns,args=(ip,port))
        t.start()
    f.close()
if __name__ == "__main__":
    main()
