#!/usr/bin/python
# coding:utf-8
import sys
import socket
from optparse import OptionParser
from threading import Thread
def portScan(ip,port):
    try:
        c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c.connect((ip,port))
        print "%s 's TCP port %d is open" %(ip,port)
    except:
        #print "%s 's TCP port %d is closed" %(ip,port)
        pass
    finally:
        c.close() 
def main():
    parser=OptionParser('usage:%prog -i <target host> -n <network> -p <target port>')
    parser.add_option('-i',type='string',dest='tgtIP',help='a')
    parser.add_option('-n',type='string',dest='tgtNetwork',help='b')
    parser.add_option('-p',type='string',dest='tgtPorts',help='c')
    (options,args)=parser.parse_args()

    tgtIP=options.tgtIP
    tgtNetwork=options.tgtNetwork
    tgtPorts=options.tgtPorts
    if(tgtPorts == None or tgtIP == None and tgtNetwork == None):
        print parser.usage
        exit(0)
    
    tgtPorts=tgtPorts.split(",")
    if tgtIP:
        for p in tgtPorts:
            portScan(tgtIP,int(p))

    if tgtNetwork:
        prefix=tgtNetwork.split(".")[0]+"."+tgtNetwork.split(".")[1]+"."+tgtNetwork.split(".")[2]+"."
        for i in range(1,255):
            try:
                ip=prefix+str(i)
                for p in tgtPorts:
                    t=Thread(target=portScan,args=(ip,int(p)))
                    t.start()
            except KeyboardInterrupt:
                sys.exit()
if __name__=="__main__":
    main()
