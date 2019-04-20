#!/usr/bin/python

import socket,sys,os
from threading import Thread
from optparse import OptionParser
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
    usage="Usage: %prog -f <filename> -i <ip address>"
    parser=OptionParser(usage=usage)
    parser.add_option("-f","--file",type="string",dest="filename",help="IP filename")
    parser.add_option("-i","--ip",type="string",dest="address",help="IP")
    (options,args)=parser.parse_args()
    
    filename=options.filename
    address=options.address
    if (filename==None and address==None):
        print"put ip or ip file"
        sys.exit()
    if filename:
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
    if address:
        prefix=address.split(".")[0]+"."+address.split(".")[1]+"."+address.split(".")[2]+"."
        for i in range(1,255):
            ip=prefix+str(i)
            port=21
            t=Thread(target=checkVulns,args=(ip,port))
            t.start()
if __name__ == "__main__":
    main()
