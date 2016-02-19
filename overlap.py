import re
from itertools import izip

def unique(a):
    return list(set(a))

def intersect(a,b):
    return list(set(a)&set(b))

def union(a,b):
    return list(set(a) | set(b))



# Run this code for best_answer_features
# PATH_IN = 'DIVIDE/match/best_answer_features/OVER_LAP/'
# PATH_OUT = 'DIVIDE/match/best_answer_features/OVER_LAP/'
# PATH_FEATURES = 'DIVIDE/match/best_answer_features/'

def extract_overlap_features(PATH_IN, PATH_OUT, PATH_FEATURES) :
    fin_1 = open(PATH_IN + 'answer_content_pro.txt','r')
    fin_2 = open(PATH_IN + 'question_content_pro.txt','r')
    fin_3 = open(PATH_IN + 'user_interest_pro.txt')

    fout_1 = open(PATH_OUT + 'q_a_overlap.txt','w')
    fout_2 = open(PATH_OUT + 'q_u_overlap.txt','w')
    fout_3 = open(PATH_OUT + 'a_u_overlap.txt','w')

    f15 = open(PATH_FEATURES + 'f15.txt', 'w')
    f16 = open(PATH_FEATURES + 'f16.txt', 'w')
    f17 = open(PATH_FEATURES + 'f17.txt', 'w')

    count = 0

    for line1, line2, line3 in izip(fin_1, fin_2, fin_3):
        word_list1 = line1.strip().split(' ')
        word_list2 = line2.strip().split(' ')
        word_list3 = line3.strip().split(' ')

        over_lap1 = intersect(word_list1, word_list2)
        over_lap2 = intersect(word_list1, word_list3)
        over_lap3 = intersect(word_list2, word_list3)

        len1 = len(over_lap1)
        len2 = len(over_lap2)
        len3 = len(over_lap3)

        print over_lap1
        fout_1.write(str(count)+',')
        fout_1.write(' '.join(over_lap1))
        fout_1.write(','+str(len1)+'\n')

        fout_2.write(str(count)+',')
        fout_2.write(' '.join(over_lap2))
        fout_2.write(','+str(len2)+'\n')

        fout_3.write(str(count)+',')
        fout_3.write(' '.join(over_lap3))
        fout_3.write(','+str(len3)+'\n')


        f15.write(str(count)+','+str(len1)+'\n')
        f16.write(str(count)+','+str(len2)+'\n')
        f17.write(str(count)+','+str(len3)+'\n')

        count = count + 1

    fin_1.close()
    fin_2.close()
    fin_3.close()

    fout_1.close()
    fout_2.close()
    fout_3.close()

    f15.close()
    f16.close()
    f17.close()



