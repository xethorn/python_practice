'''This program takes a string and returns an abbeviation'''


class Abbrev():
    def __init__(self, string):
        self.string = string.upper()

    @property
    def initials(self):
        return ''.join([
            word.strip()[0] for word in self.string.split(' ')
            if word.strip()]
