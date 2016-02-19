# This is to generate the source file for LDA 
# LDA model can use source file to generate the LDA features

from itertools import izip
import re

#PATH_IN = 'DIVIDE/match/best_answer_features/LDA/'
#PATH_OUT = 'DIVIDE/match/best_answer_features/LDA/'

def lda_source(PATH_IN, PATH_OUT) :

    f1 = open(PATH_IN + 'question_content_pro.txt','r')
    f2 = open(PATH_IN + 'answer_content_pro.txt','r')
    f3 = open(PATH_IN + 'user_interest_pro.txt', 'r')
    f4 = open(PATH_IN + 'question_tag_pro.txt', 'r')

    fout = open(PATH_OUT + 'LDA_SOURCE.txt','w')

    for line1, line2, line3, line4 in izip(f1, f2, f3, f4) :
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
        fout.write(' '+info3)

        info4 = line4.strip()
        print info4
        fout.write(' '+info4 + '\n')

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    fout.close()

    
