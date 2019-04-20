#!/usr/bin/python

import os,time
from scapy.all import *
from threading import Thread
from optparse import OptionParser

def sweep(ip):
    try:
        pakt=Ether(dst="ff:ff:ff:ff:ff:ff",src="00:0c:29:52:84:4f")/ARP(hwsrc="00:0c:29:52:84:4f",psrc="10.140.98.238",hwdst="00:00:00:00:00:00",pdst=ip)
        result=srp1(pakt,timeout=1,verbose=0)
        if result:
            time.sleep(0.1)
            print ip,"zai"
            return
    except:
        return
def main():
    usage="Usage: %prog -f <filename> -i <ip address>"
    parser=OptionParser(usage=usage)
    parser.add_option("-f","--file",type="string",dest="filename",help="specify the IP address file")
    parser.add_option("-i","--ip",type="string",dest="address",help="specify the IP address")
    (options,args)=parser.parse_args()
    filename=options.filename
    address=options.address
    if (filename==None and address==None):
        print "ip or "
        sys.exit()
    if filename:
        if not os.path.exists(filename):
            print "asd"
            sys.exit()
        f=open(filename,"r")
        for i in f:
            ip=i.strip("\n")

            t=Thread(target=sweep,args=(ip,))
            t.start()
    if address:
        prefix=address.split(".")[0]+"."+address.split(".")[1]+"."+address.split(".")[2]+"."
        for i in range(1,255):
            ip=prefix+str(i)
            t=Thread(target=sweep,args=(ip,))
            t.start()
if __name__ =="__main__":
    main()
