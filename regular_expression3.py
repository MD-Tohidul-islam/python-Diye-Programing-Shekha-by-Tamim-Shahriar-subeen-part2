import re
s = 'Bangladesh'
match = re.search('.',s)
print(match.group())
match1 =re.search('..',s)
print(match1.group())
match3 = re.search('B.....',s)
print(match3.group())
match4 = re.search('B.n...',s)
print(match4.group())
match5 = re.search('..l',s)
print(match5.group())
match6 = re.search('B..g..',s)
print(match6.group())
b = 'Bangladesh is our homeland'
match7 = re.search('............',b)
print(match7.group())
