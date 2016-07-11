from  abbreviation import *
from datetime import datetime

obj = abbrev('steven garcia is a student at holberton school')
for item in obj.initials():
    print item,
print datetime.now().time().strftime('%H:%M:%S')
