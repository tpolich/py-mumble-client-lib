__author__ = 'Tim'

import Mumble_pb2 as protobuf
from py_mumble_lib.control_channel import message_type as cmt
from py_mumble_lib import control_channel
from py_mumble_lib import voice_channel
import select
import time
import logging as log
import version

class Client:

    PING_RATE = 28

    def __init__(self, authentication_message, host, port=64738, cert=None):
        c = control_channel.ControlChannel(host, port)
        self.control_channel = c

        c.send_message(cmt.VERSION, version.DefaultVersionMessage())
        c.send_message(cmt.AUTHENTICATE, authentication_message)

        self.control_message_handler = control_channel.ControlMessageHandler()
        self.voice_message_handler = voice_channel.VoiceMessageHandler()

        #need to ping after receiving the CryptSetup message to get the server to finish initialization
        self.control_message_handler.register(cmt.CRYPT_SETUP, lambda m: self._ping_if_needed(True))

        def channel_callback(message):
            print "got me a channel"

        self.control_message_handler.register(cmt.CHANNEL_STATE, channel_callback)

        self.last_ping = time.time()

        self._start_read_loop()

    def send_control_message(self):
        #need a blocking queue to add to the message out queue

        m = protobuf.TextMessage()
        m.message = "SUP MY HOMEEEE"
        m.session.extend([55, 51])
        self.control_channel.send_message(cmt.TEXT_MESSAGE, m)

    def _ping_if_needed(self, force=False):
        if time.time() - self.last_ping >= Client.PING_RATE - 1 or force:
            self.last_ping = time.time()
            p = protobuf.Ping()
            p.timestamp = int(time.time())
            self.control_channel.send_message(cmt.PING, p)

    def _start_read_loop(self):
        c = self.control_channel
        vmh = self.voice_message_handler
        cmh = self.control_message_handler

        while True:
            print Client.PING_RATE - (time.time() - self.last_ping)
            (rlist, wlist, elist) = select.select([c.sock], [], [c.sock], Client.PING_RATE - (time.time() - self.last_ping))

            self._ping_if_needed()

            if c.sock in elist:
                c.sock.close()

            if c.sock in rlist:
                (type, message) = c.recv_message()
                if type is cmt.UDP_TUNNEL:
                   vmh.handle(message, True)
                elif type > -1:
                    cmh.handle(type, message)
