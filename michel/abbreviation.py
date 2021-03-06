'''This program takes a string and returns an abbeviation'''


class Abbrev():
    def __init__(self, string):
        self.string = string

    def initials(self):
        initials = []
        count = 0
        self.string = self.string.upper()
        # Putting the first letter of the string into the list
        initials.append(self.string[0])

        for letter in self.string:
            # Checking every letter for a space
            # and assigning the next value to a list
            if self.string[count] == ' ':
                initials.append(' '+self.string[count+1])
            count += 1
        return ''.join(initials)
