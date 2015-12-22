import re

f_in = open('f4_ini.txt','r')
f_out = open('f4.txt','w')

'''
line = f_in.readline()
info = line.strip().split(',')
years = info[1][-6]
print years


'''
for line in f_in:
    info = line.strip().split(',')
    id = info[0]
    years = info[1][:-5]
    #print years

    if years :
        f_out.write(id+','+years+'\n')
    else :
        print id
        f_out.write(id+'\n')


f_in.close()
f_out.close()
