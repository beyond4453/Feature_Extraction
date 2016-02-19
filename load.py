
from pandas import Series, DataFrame
import pandas as pd
import json
import numpy as np
import string

PATH_IN = 'INIT/'
PATH_OUT = 'TOTAL/'

def str_strip(data) :
    data = data.str.replace('\n','')
    data = data.str.replace('\r','')
    data = data.str.replace(',',' ')
    data = data.str.replace('.','')
    data = data.str.replace('"','')
    data = data.str.lower()   
    return data  
   
f1 = open(PATH_IN + 'a_source.json')
f2 = open(PATH_IN + 'q_source.json')
f3 = open(PATH_IN + 'u_source.json')
f4 = open(PATH_IN + 'qtag_source.json')

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
m = m.sort(['question_id','answer_voted'], ascending=[1,0])
m = m.drop('user_address', axis=1)
m = m.drop('user_name', axis=1)
m = m.reset_index(drop=True) 

# modify the string in dataframe m
m['answer_content'] = str_strip(m['answer_content'])
m['question_content'] = str_strip(m['question_content'])
m['user_edu'] = str_strip(m['user_edu'])
m['user_specialty'] = str_strip(m['user_specialty'])
m['user_interest'] = str_strip(m['user_interest'].astype(str))
m['user_intro'] = str_strip(m['user_intro'])
m['question_tags'] = str_strip(m['question_tags'].astype(str))
m['user_recommends'] = str_strip(m['user_recommends'].astype(str))
print m      # 3195 x 20

#m.to_json(PATH_OUT + 'total01.json')
m.to_csv(PATH_OUT + 'total01.csv', encoding='utf-8', index = False)

