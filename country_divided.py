with open('all_country.txt','r') as f:
    lines = f.readlines()
    a_country = open('a_country.txt','w')
    b_country = open('b_country.txt','w')
    for line in lines:
        if line[0]=='a'or line[0]=='A':
            a_country.write(line+'\n')
        if line[0] == 'b' or line[0]=='B':
            b_country.write(line+'\n')