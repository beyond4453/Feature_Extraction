from itertools import izip
import re


f1 = open('question_content_pro.txt','r')
f2 = open('answer_content_pro.txt','r')
f3 = open('user_interest_pro.txt', 'r')
fout = open('LDA_SOURCE.txt','w')

for line1, line2, line3 in izip(f1, f2, f3) :
    #line1 = f1.readline()
    info1 = line1.strip()
    print info1
    fout.write(info1)

     
    #line2 = f2.readline()
    info2 = line2.strip()
    print info2
    fout.write(' '+info2)

    info3 = line3.strip()
    print info3
    fout.write(' '+info3+'\n')


    
f1.close()
f2.close()
fout.close()
