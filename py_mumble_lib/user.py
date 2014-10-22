__author__ = 'Tim'

class User:

    def __init__(self, from_message=None):
        if from_message:
            for (fd, value) in from_message.ListFields():
                self[fd] = value