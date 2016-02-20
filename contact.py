import re
from itertools import izip


PATH_HOME = 'MATCH/BEST/'
PATH_NORMAL = 'MATCH/BEST/NORMAL/'
PATH_LDA = 'MATCH/BEST/LDA/'
PATH_SENTENCE = 'MATCH/BEST/SENTENCE_VECTOR/'

#PATH_HOME = 'MATCH/SECOND/'
#PATH_NORMAL = 'MATCH/SECOND/NORMAL/'
#PATH_LDA = 'MATCH/SECOND/LDA/'
#PATH_SENTENCE = 'MATCH/SECOND/SENTENCE_VECTOR/'



#PATH_HOME = 'MATCH/THIRD/'
#PATH_NORMAL = 'MATCH/THIRD/NORMAL/'
#PATH_LDA = 'MATCH/THIRD/LDA/'
#PATH_SENTENCE = 'MATCH/THIRD/SENTENCE_VECTOR/'


f_in1 = open(PATH_NORMAL + 'Normal_Features.txt','r') 
f_in2 = open(PATH_LDA + 'model-final.theta','r') 
f_in3 = open(PATH_SENTENCE + 'M_B.txt.vec','r')
f_out = open(PATH_HOME + 'match_best.csv', 'w')



line1 = f_in1.readline()
line3 = f_in3.readline()

'''
line3 = f_in3.readline()
data3 = line3.strip().split(' ')[1:]
info3 = ' '.join(data3)
print data3
print info3
print type(data3)
print type(info3)
'''

#print line3[6:]
#line1 = f_in1.readline()
#print type(line1)
#line1 = line1.replace(',',' ')
#print line1

#print line1
#print line1
#print line2
#print line3


for line1, line2, line3 in izip(f_in1, f_in2, f_in3):
    data3 = line3.strip().split(' ')[1:]
    info3 = ' '.join(data3)
    f_out.write(info3 + ' ')
    data2 = line2.strip()
    f_out.write(data2 + ' ')
    data1 = line1.strip().replace(',',' ')
    #data1 = data1.replace(',',' ')
    f_out.write(data1+'\n')
   

print 'Done'    


f_in1.close()
f_in2.close()
f_in3.close()
f_out.close()
