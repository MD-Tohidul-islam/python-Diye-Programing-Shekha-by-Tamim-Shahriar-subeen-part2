import re
s = 'Bangladesh is our homeland'
match1 =re.search('B.+h',s)
print(match1.group())
match2 = re.search('B.+?h',s)
print(match2.group())
match3 = re.search('B\w+h',s)
print(match2.group())


