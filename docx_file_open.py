import docx
f= docx.Document('saimum.docx')
all_para = f.paragraphs
for para in all_para:
    print(para.text)
    print('..............')