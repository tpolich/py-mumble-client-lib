__author__ = 'Tim'

from struct import *
import sys

class VoiceMessageHandler:

    def __init__(self):
        self.handlers = 5

    def handle(self, udp_package, tcp_tunneled=False):
        if tcp_tunneled:
            self.process(udp_package)
        else:
            raise "Haven't implemented non-tunneled audio."

    def _decrypt(self):
        return None

    def process(self, udp_package):
        header = unpack("!B", udp_package[0])[0]

        udp_type = header >> 5
        target = header & 0b00011111

        print udp_type
        print header >> 5
        print target

#1pigpelt2