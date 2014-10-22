__author__ = 'Tim'

from struct import *
import socket
import ssl

from py_mumble_lib.control_channel import message_type as cmt


class ControlChannel:

    HEADER_SIZE = 6

    def __init__(self, host, port, buffer_size=4096):
        to_wrap = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #ssl control channel TLSv1 using AES256-SHA
        self.sock = ssl.wrap_socket(to_wrap, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="SHA+AES")

        self.sock.connect((host,port))
        self.sock.setblocking(0)

        self.header_buffer = memoryview(bytearray(ControlChannel.HEADER_SIZE))
        self.header_count = 0
        self.message_buffer = None
        self.message_count = 0
        self.message_type = -1
        self.message_size = -1

    def send_message(self, type, message):
        if message.IsInitialized():
            s = message.SerializeToString()
            packet = pack("!HI", type, len(s)) + s

            sent = 0
            while sent != len(packet):
                sent += self.sock.send(packet[sent:])
        else:
            raise ValueError("Message is not properly initialized.")

    def recv_message(self):
        #blocks till i get a message
        try:
            if self.header_count != ControlChannel.HEADER_SIZE:

                self.header_count += self.sock.recv_into(self.header_buffer[self.header_count:], nbytes=ControlChannel.HEADER_SIZE - self.header_count)

                if self.header_count == ControlChannel.HEADER_SIZE:
                    (self.message_type, self.message_size) = unpack("!HI", self.header_buffer)

                    self.message_buffer = memoryview(bytearray(self.message_size))

            if self.header_count == ControlChannel.HEADER_SIZE:
                self.message_count += self.sock.recv_into(self.message_buffer[self.message_count:], nbytes=self.message_size - self.message_count)

                if self.message_count == self.message_size:
                    self.message_count = 0
                    self.header_count = 0

                    if self.message_type is cmt.UDP_TUNNEL:
                        return cmt.UDP_TUNNEL, self.message_buffer.tobytes()
                    else:
                        message = cmt.type_to_message(self.message_type)()
                        #todo: see if there is a way to parse from the buffer directly
                        message.ParseFromString(self.message_buffer.tobytes())

                        return self.message_type, message
        except ssl.SSLError as e:
            #becuase I am using ssl just becuase the os says there is data ready doesn't mean i can get any
            return -1, None
        return -1, None


