from py_mumble_lib import Mumble_pb2
from struct import *

__author__ = 'Tim'


def DefaultVersionMessage():
    v = Mumble_pb2.Version()
    #version int for 1.2.4 in binary
    v.version = int("00000000000000010000001000000010", 2)
    v.release = ".1"
    v.os = "mumble_py_lib"
    v.os_version=".1"
    return v