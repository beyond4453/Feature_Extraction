
from pandas import Series, DataFrame
import pandas as pd
import json
import numpy as np
import string


f1 = open('INIT/a_source.json')
f2 = open('INIT/q_source.json')
f3 = open('INIT/u_source.json')
f4 = open('INIT/qtag_source.json')

answer = [json.loads(line.strip().strip(',')) for line in f1]
#print answer[0]
#answer_frame 
answer_frame = DataFrame(answer)
answer_frame = answer_frame.drop_duplicates('answer_id')
#print answer_frame #3194 x 5

question = [json.loads(line.strip().strip(',')) for line in f2]
#print question[0]
question_frame = DataFrame(question)
question_frame = question_frame.drop_duplicates('question_id')
#print question_frame  # 898 x 2


user = [json.loads(line.strip().strip(',')) for line in f3]
user_frame = DataFrame(user)
user_frame = user_frame.drop_duplicates('user_id')
#print user_frame    # 3169 x 14


qtag = [json.loads(line.strip().strip(',')) for line in f4]
qtag_frame = DataFrame(qtag)
qtag_frame = qtag_frame.drop_duplicates('question_id')
#print qtag_frame      # 898 x 2




# Generate the source data
m1 = pd.merge(answer_frame, user_frame, how = 'outer')
#print m1    # 3194 x 18

m2 = pd.merge(qtag_frame, question_frame, how = 'outer')
#print m2     # 898 x 3 

# Generate 
m = pd.merge(m1, m2, how = 'outer')
print m      # 3195 x 20
m.to_json('total.json')





# calculate the features

# feature1 : length of the answer_content 
#answer_content = m[['answer_content','user_id']]
answer_content = m['answer_content']
# f1 : length of the answer_content
f1 = answer_content.str.len()
f1.to_csv('FEATURES/f1.txt')
#print answer_content


# feature2 : length of the user_introduction
user_intro = m['user_intro']
#print user_intro
f2 = user_intro.str.len()
f2.to_csv('FEATURES/f2.txt')
#print f2



# feature3 : length of the question_content
question_content = m['question_content']
f3 = question_content.str.len()
#print f3
f3.to_csv('FEATURES/f3.txt')


# feature4: user's experience years
user_exp = m['user_exp']
f4 = m['user_exp']
f4.to_csv('FEATURES/f4_ini.txt')
#print f4

# feature5 : length of the user's edu
user_edu = m['user_edu']
f5 = user_edu.str.len()
f5.to_csv('FEATURES/f5.txt')
#print f5


# feature6 : number of topics of user's interest
user_interest = m['user_interest']
f6 = user_interest.str.len()
f6.to_csv('FEATURES/f6.txt')
#print f6


# feature7 : number of the people user followed
user_followed = m['user_followed']
f7 = user_followed.str.len()
f7.to_csv('FEATURES/f7.txt')
#print f7

# feature8 : number of the question tags
question_tags = m['question_tags']
f8 = question_tags.str.len()
f8.to_csv('FEATURES/f8.txt')
#print f8


# feature9 : number of saved lives
saved_lives = m['user_saved']
f9 = saved_lives
f9.to_csv('FEATURES/f9.txt')
#print f9


# feature10 : number of recieved thanks
recieved_thanks = m['user_thanks']
#recieved_thanks = str(recieved_thanks)
f10 = recieved_thanks.str.replace(',','')
f10.to_csv('FEATURES/f10.txt')
#print f10


# feature11 : number of agrees
recieved_agrees = m['user_agrees']
f11 = recieved_agrees.str.replace(',','')
f11.to_csv('FEATURES/f11.txt')
#print f11


# feature12 : nuber of helped people
helped = m['user_helped']
f12 = helped.str.replace(',','')
f12.to_csv('FEATURES/f12.txt')
#print f12


# feature13 : number of doctor recommend
recommend = m['user_recommends']
f13 = recommend.str.len()
f13.to_csv('FEATURES/f13.txt')
#print f13

'''
# feature14 : total length of the recommends
recommend_str = m['user_recommends']
#recommend_str = ','.join(str(v) for v in recommend_str)
f14 = recommend_str.to_string
print f14
#f14.to_csv('f14.txt')
'''

# Generate data used by the LDA

# Process with the question_content
qc = m['question_content']
qc = qc.str.replace('\n','')
qc = qc.str.replace('?','')
qc = qc.str.replace('"','')
qc = qc.str.replace('.','')
qc = qc.str.replace(',','')
qc = qc.str.replace('/',' ')
qc = qc.str.replace('(','')
qc = qc.str.replace(')','')
qc = qc.str.replace('&','')
qc = qc.str.replace('\'','')
qc = qc.str.replace('!','')
qc = qc.str.replace('-','')
qc = qc.str.replace(';','')
qc = qc.str.lower()
qc.to_csv('LDA/question_content.txt', encoding='utf-8')


# Process with the answer_content
ac = m['answer_content']
ac = ac.str.replace('\n','')
ac = ac.str.replace('?','')
ac = ac.str.replace('"','')
ac = ac.str.replace('.','')
ac = ac.str.replace(',','')
ac = ac.str.replace('/',' ')
ac = ac.str.replace('(','')
ac = ac.str.replace(')','')
ac = ac.str.replace('&','')
ac = ac.str.replace('\'','')
ac = ac.str.replace('!','')
ac = ac.str.replace('-','')
ac = ac.str.replace(';','')
ac = ac.str.lower()
ac.to_csv('LDA/answer_content.txt', encoding='utf-8')

# Process with the user_recommends
ur = m['user_recommends'].astype(str)
ur = ur.str.replace('\n','')
ur = ur.str.replace('?','')
ur = ur.str.replace('"','')
ur = ur.str.replace('.','')
ur = ur.str.replace(',','')
ur = ur.str.replace('/',' ')
ur = ur.str.replace('(','')
ur = ur.str.replace(')','')
ur = ur.str.replace('&','')
ur = ur.str.replace('\'','')
ur = ur.str.replace('!','')
ur = ur.str.replace('-','')
ur = ur.str.replace(';','')
ur = ur.str.replace('[','')
ur = ur.str.replace(']','')
ur = ur.str.replace('#','')
ur = ur.str.lower()
ur.to_csv('LDA/user_recommends.txt', encoding='utf-8')


# Process with question_tags
qt = m['question_tags'].astype(str)
qt = qt.str.replace('\n','')
qt = qt.str.replace('[','')
qt = qt.str.replace(']','')
qt = qt.str.replace('"','')
qt = qt.str.replace(',','')
qt = qt.str.replace('u\'','')
qt = qt.str.replace('\'','')
qt = qt.str.replace('-','')
qt = qt.str.replace('&','')
qt = qt.str.replace('/', ' ')
qt = qt.str.lower()
#print qt
qt.to_csv('LDA/question_tag.txt', encoding='utf-8')



# Process with user_interest
ut = m['user_interest'].astype(str)
ut = ut.str.replace('\n','')
ut = ut.str.replace('"','')
ut = ut.str.replace('[','')
ut = ut.str.replace(']','')
ut = ut.str.replace(',','')
ut = ut.str.replace('u\'','')
ut = ut.str.replace('\'','')
ut = ut.str.replace('/', ' ')
ut = ut.str.replace('-','')
ut = ut.str.replace('&','')
ut = ut.str.replace('(','')
ut = ut.str.replace(')','')
ut = ut.str.lower()
ut.to_csv('LDA/user_interest.txt', encoding='utf-8')

# Proecess with user_specialty
us = m['user_specialty'].astype(str)
us = us.str.replace('\n','')
us = us.str.replace('"','')
us = us.str.replace('[','')
us = us.str.replace(']','')
us = us.str.replace(',','')
us = us.str.replace('u\'','')
us = us.str.replace('\'','')
us = us.str.replace('/', ' ')
us = us.str.replace('-','')
us = us.str.replace('&','')
us = us.str.replace('(','')
us = us.str.replace(')','')
us = us.str.lower()
us.to_csv('LDA/user_specialty.txt', encoding='utf-8')










