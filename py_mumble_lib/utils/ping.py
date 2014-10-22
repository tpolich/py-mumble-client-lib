__author__ = 'Tim'

from struct import *
import socket
import time


def ping(host, port=64738, ident=0, timeout=3, printout=True):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)

    ping_data = pack("!iq", 0, ident)

    send_time = time.time()
    sock.sendto(ping_data, (host, port))

    buf = ""
    #response message is 24 bytes long
    while len(buf) < 24:
        buf += sock.recv(24 - len(buf))

    ping = (time.time() - send_time) * 1000
    r = unpack("!bbbbqiii", buf)

    if printout:
        print "Version: %d.%d.%d.%d" % (r[0], r[1], r[2], r[3])
        if ident != 0:
            print "Ident: %s" % r[4]

        print "Connected Users: %d" % r[5]
        print "Maximum Users: %d" % r[6]
        print "Allowed Bandwidth: %dkbit/s" % r[7]
        print "Ping: %.1fms" % ping

    return r