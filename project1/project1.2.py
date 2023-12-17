import re
text = 'book at subeen.com, book At subeen.com, book (at) subeen dot com,book [at] subeen [dot] com'
result = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+','@',text,flags=re.I)
print(result)
final_result = re.sub(r'\s+[\(\[]*\s*dot[\)\]]*\s+','.',result,flags=re.I)
print(final_result)

