# divide the total.csv into 
# best_answer.csv
# second_answer.csv
# third_answer.cs

import pandas as pd
import numpy as np
import operator
import re

# Run these code the first time 
#fin = open('Total.csv','r')
#fout1 = open('DIVIDE/best_answer.csv', 'w')
#fout2 = open('DIVIDE/nonbest_answer.csv', 'w')

# Run these code the seconde time 
#fin = open('DIVIDE/nonbest_answer.csv', 'r')
#fout1 = open('DIVIDE/second_answer.csv', 'w')
#fout2 = open('DIVIDE/nonsecond_answer.csv', 'w')

# Run these code the third time 
fin = open('DIVIDE/nonsecond_answer.csv', 'r')
fout1 = open('DIVIDE/third_answer.csv', 'w')
fout2 = open('DIVIDE/nonthird_answer.csv', 'w')


# read the title
line = fin.readline().strip()
fout1.write(line + '\n')
fout2.write(line + '\n')
#print line

line = fin.readline()
info = line.strip().split(',')
qid = info[3]
#print line
#print qid
fout1.write(line)

line = fin.readline()

while line:
    
    info = line.strip().split(',')
    qid_next = info[3]
    print qid_next
    # Same question different answers
    if qid_next == qid :
        fout2.write(line)
    else :
    # another question start update qid & fout1
        qid = info[3]
        fout1.write(line)
    line = fin.readline()     
        

fout1.close()
fout2.close()
fin.close()


#data = pd.read_csv('total.csv')
#data = pd.read_json('total.json')


