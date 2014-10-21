__author__ = 'Tim'

import Mumble_pb2
import control_channel
import control_message_type as cmt
import select
import time
import logging as log

class Client:

    PING_RATE = 28

    def __init__(self, host, port=64738, username="mumble-jukebox", password=None, cert=None, version_message=None, authentication_message=None):
        c = control_channel.ControlChannel(host, port)
        self.control_channel = c

        c.send_message(cmt.ControlMessageType.VERSION, version_message if version_message is not None else self._defaultVersionMessage())
        c.send_message(cmt.ControlMessageType.AUTHENTICATE, authentication_message if authentication_message is not None else self._defaultAuthMessage())

        self.last_ping = -1

        while True:
            print Client.PING_RATE - (time.time() - self.last_ping)
            (rlist, wlist, elist) = select.select([c.sock], [], [], Client.PING_RATE - (time.time() - self.last_ping))
            print "=====IN_SELECT====="

            self.ping_if_needed()
            print rlist
            if c.sock in rlist:
                m = c.recv_message()
                if m is not None:
                    print type(m).__name__
                    print m



    def ping_if_needed(self, force=False):
        if time.time() - self.last_ping >= Client.PING_RATE - 1 or force:
            log.debug("Sending Ping")
            self.last_ping = time.time()
            self.control_channel.send_message(cmt.ControlMessageType.PING, Mumble_pb2.Ping())
            print "Sent Ping"

    @staticmethod
    def _defaultVersionMessage():
        v = Mumble_pb2.Version()
        v.version =1
        v.release =".1"
        v.os = "mumble_py_lib"
        v.os_version=".1"
        return v

    @staticmethod
    def _defaultAuthMessage():
        a = Mumble_pb2.Authenticate()
        a.username = "test_user"
        return a

    def connect(self):
        print "C"