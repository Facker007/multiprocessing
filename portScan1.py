#!/usr/bin/python
# coding:utf-8

import socket

def portScan(ip,port):
    try:
        c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c.connect((ip,port))
        print "%s 's TCP port %d is open" %(ip,port)
    except:
        print "%s 's TCP port %d is closed" %(ip,port)

    finally:
        c.close()
def main():
    ip="10.140.98.59"
    port=445
    portScan(ip,port)
if __name__=="__main__":
    main()
