from py_mumble_lib import Mumble_pb2

__author__ = 'Tim'


def DefaultVersionMessage():
    v = Mumble_pb2.Version()
    v.version =1
    v.release =".1"
    v.os = "mumble_py_lib"
    v.os_version=".1"
    return v