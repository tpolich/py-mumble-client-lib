__author__ = 'Tim'


class ControlMessageHandler:

    def __init__(self):
        self.events = {}

    def register(self, event_type, function):
        if event_type not in self.events:
            self.events[event_type] = []
        self.events[event_type].append(function)

    def unregister(self, event_type, function):
        if event_type in self.events:
            self.events[event_type].remove(function)

    def handle(self, event_type, message):
        if event_type in self.events:
            for handlers in self.events[event_type]:
                handlers(message)
        else:
            print "=====No Handler %s=====" % type(message).__name__
            print message
            print "===================="
