#!/usr/bin/python
import sys,time
from threading import Thread
from scapy.all import *
def host_scan(ip):
    try:
        pkt=IP(dst=ip)/TCP(dport=56789,flags='A')
        result=sr1(pkt,timeout=1,verbose=0)
        if int(result[TCP].flags)==4:
            time.sleep(0.1)
            print ip,"zai"
        return
    except:
        return 
def main():
    if len(sys.argv) != 2:
        print "sad"
        sys.exit()
    address=str(sys.argv[1]).strip()
    prefix=address.split(".")[0]+"."+address.split(".")[1]+"."+address.split(".")[2]+"."
    for i in range(1,255):
        ip=prefix+str(i)
        t=Thread(target=host_scan,args=(ip,))
        t.start()
if __name__=="__main__":
    main()
