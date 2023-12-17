import re

text = 'this is line 1. Date is 2017/05/03. And there is another date: 2017-07-01. The third and final date is 2017/08/30.'
pat = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
print(pat)
print(type(pat))
result1 = pat.findall(text)
print(result1)
pat2= re.compile('(\\d{4})[-/](\d{2})[-/](\\d{2})')
result2 = pat2.findall(text)
print(result2)
