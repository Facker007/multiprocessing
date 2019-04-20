#!/usr/bin/python
import sys,time
from threading import Thread
from scapy.all import *
from optparse import OptionParser
def port_scan(ip,port):
    try:
        pkt=IP(dst=ip)/TCP(dport=port,flags='S')
        result=sr1(pkt,timeout=1,verbose=0)
        if int(result[TCP].flags)==18:
            time.sleep(0.1)
            print ip,"TCP",port,"zai"
        return
    except:
        return
def main():
    parser=OptionParser('usage: %prog -i <target host> -n <network> -p <target ports>')
    parser.add_option('-i',type='string',dest='tgtIP',help='wqe')
    parser.add_option('-n',type='string',dest='tgtNetwork',help='asd')
    parser.add_option('-p',type='string',dest='tgtPorts',help='qwe')
    (options,args)=parser.parse_args()
    
    tgtIP=options.tgtIP
    tgtNetwork=options.tgtNetwork
    tgtPorts=options.tgtPorts
    if (tgtPorts == None or tgtIP ==None and tgtNetwork == None):
        print parser.usage
        exit(0)
    tgtPorts=tgtPorts.split(",")
    if tgtIp:
        if len(sys.argv) != 3:
            print "asd"
            sys.exit()
    ip=str(sys.argv[1]).strip()
    ports=str(sys.argv[2]).split(",")
    for p in ports:
        port=int(p)
        t=Thread(target=port_scan,args=(ip,port))
        t.start()
if __name__=="__main__":
    main()
