#!/usr/bin/python
#coding:utf-8
import nmap 
from optparse import OptionParser
from threading import Thread
import sys,time

def osscan(ip):
    nm=nmap.PortScanner()
    try:
        results=nm.scan(hosts=ip,arguments='-O')
        os=results['scan']['ip']['osmatch'][0]['name']
        time.sleep(0.1)
        print ip,os
    except:
        pass
def main():
    parser=OptionParser('usage:%prog -i <target host> -n <network>')
    parser.add_option('-i',type='string',dest='tgtIP',help='ip')
    parser.add_option('-n',type='string',dest='tgtNetwork',help='network')
    (options,args)=parser.parse_args()
    
    tgtIP=options.tgtIP
    tgtNetwork=options.tgtNetwork
    if (tgtIP == None and tgtNetwork == None):
        print parser.usage
        sys.exit()

    if tgtIP:
        ip=str(tgtIP).strip()
        osscan(ip)

    if tgtNetwork:
        prefix=tgtNetwork.split(".")[0]+"."+tgtNetwork.split(".")[1]+"."+tgtNetwork.split(".")[2]+"."
        for i in range(1,255):
            ip=prefix+str(i)
            t=Thread(target=osscan,args=(ip,))
            t.start()
if __name__=="__main__":
    main()
