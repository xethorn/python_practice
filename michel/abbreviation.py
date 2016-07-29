'''This program takes a string and returns an abbeviation'''


class Abbrev():
    def __init__(self, string):
        self.string = string.upper()

    @property
    def initials(self):
        initials = []
        for word in self.string.split(' '):
            word = word.strip()
            if word: 
                initials.append(word)
        return ''.join(initials)
    
