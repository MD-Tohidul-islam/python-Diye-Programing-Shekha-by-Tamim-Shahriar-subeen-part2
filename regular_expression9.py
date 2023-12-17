with open('regular_expression_file.txt','r') as f:
    text = f.read()

print(text)
import re
match1 = re.findall(r'^.*?$',text,re.MULTILINE)
print(match1)