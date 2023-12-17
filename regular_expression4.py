import re
s = 'Bangladesh is our homeland'
match = re.search('o\w\w',s)
print(match.group())
match1 = re.search('i\w\w',s)
print(match1)
match2 = re.search('B\w+d',s)
print(match2.group())
match4 = re.search('d\w+o',s)
print(match4)