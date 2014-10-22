from py_mumble_lib import Mumble_pb2
import py_mumble_lib as pym

import threading

class go:

    def __init__(self, x):
        self.x = x


    def worker(self):
        a = Mumble_pb2.Authenticate()
        a.username = "test_user" + str(self.x)
        a.celt_versions.append(-2147483632)
        g = pym.Client(a, "mumble.tpolich.net");

    def go(self):
        threading.Thread(target=self.worker).start()

for x in range(1, 2):
    g = go(x)
    g.go()



#pinger.ping("mumble.tpolich.net")