import re
match = re.search('bangla','bangladesh')
print(match)
print(match.group())
print(re.search('desh','bangladesh').group())
match1 = re.search('des','bangladesh')
print(match1.group())
match2 = re.search('dest','bangladesh')
#print(match2.group())