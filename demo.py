from py_mumble_lib import Mumble_pb2
import py_mumble_lib as pym

import threading
from ctypes import *
import os


class go:

    def __init__(self, x):
        self.x = x


    def worker(self):
        a = Mumble_pb2.Authenticate()
        a.username = "test_user" + str(self.x)
        a.opus = True
        g = pym.Client(a, "mumble.tpolich.net")

    def go(self):
        threading.Thread(target=self.worker).start()

#opus = cdll.LoadLibrary("opus.dll")

#print opus
#print opus.opus_decode

#for x in range(1, 2):
#    g = go(x)
#    g.go()



#pinger.ping("mumble.tpolich.net")


from py_mumble_lib.utils import variable_len_int as var_int

var_int.__test()