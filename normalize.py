
from pandas import Series, DataFrame
import pandas as pd
#import json
import numpy as np
#import string

def normalize(PATH_IN, PATH_OUT) :
    # feature1 : length of the answer_content 
    f1 = pd.read_csv(PATH_IN + 'f1.txt', names = ['index','len_answer_content'])

    # feature2 : length of the user_introduction
    f2 = pd.read_csv(PATH_IN + 'f2.txt', names = ['index','len_user_intro'])
    m = pd.merge(f1, f2, how='outer')
    #print m

    # feature3 : length of the question_content
    f3 = pd.read_csv(PATH_IN + 'f3.txt', names = ['index', 'len_question_content'])
    m = pd.merge(m, f3, how='outer')

    # feature4: user's experience years
    f4 = pd.read_csv(PATH_IN + 'f4.txt', names = ['index','user_exp'])
    m = pd.merge(m, f4, how='outer')
    #print m

    # feature5 : length of the user's edu
    f5 = pd.read_csv(PATH_IN + 'f5.txt', names = ['index','len_user_edu'])
    m = pd.merge(m, f5, how='outer')

    # feature6 : number of topics of user's interest
    f6 = pd.read_csv(PATH_IN + 'f6.txt', names = ['index','num_user_interst'])
    m = pd.merge(m, f6, how='outer')

    # feature7 : number of the people user followed
    f7 = pd.read_csv(PATH_IN + 'f7.txt', names = ['index','num_user_followed'])
    m = pd.merge(m, f7, how='outer')

    # feature8 : number of the question tags
    f8 = pd.read_csv(PATH_IN + 'f8.txt', names = ['index', 'num_question_tags'])
    m = pd.merge(m, f8, how='outer')

    # feature9 : number of saved lives
    f9 = pd.read_csv(PATH_IN + 'f9.txt', names = ['index','num_user_saved'])
    m = pd.merge(m, f9, how='outer')

    # feature10 : number of recieved thanks
    f10 = pd.read_csv(PATH_IN + 'f10.txt', names = ['index','num_user_thanks'])
    m = pd.merge(m, f10, how='outer')

    # feature11 : number of agrees
    f11 = pd.read_csv(PATH_IN + 'f11.txt', names = ['index','num_user_agrees'])
    m = pd.merge(m, f11, how='outer')

    # feature12 : nuber of helped people
    f12 = pd.read_csv(PATH_IN + 'f12.txt', names = ['index','num_user_helped'])
    m = pd.merge(m, f12, how='outer')

    # feature13 : number of doctor recommend
    f13 = pd.read_csv(PATH_IN + 'f13.txt', names = ['index','num_user_recommend'])
    m = pd.merge(m, f13, how='outer')

    #####################################################################
    # feature15 : number of answer_question overlap
    f15 = pd.read_csv(PATH_IN + 'f15.txt', names = ['index', 'answer_question_overlap'])
    m = pd.merge(m, f15, how='outer')


    # feature16 : number of question_user_interest overlap
    f16 = pd.read_csv(PATH_IN + 'f16.txt', names = ['index', 'question_uinterest_overlap'])
    m = pd.merge(m, f16, how= 'outer')

    # feature17 : number of user_interest_answer overlap
    f17 = pd.read_csv(PATH_IN + 'f17.txt', names = ['index', 'uinterest_answer_overlap'])
    m = pd.merge(m, f17, how= 'outer')

    #######################################################################
    Index = m.ix[:,0] 
    M = m.ix[:,1:]

    M = (M - M.min()) / (M.max() - M.min())
    M['index'] = Index


    # question_id :
    # qid = pd.read_csv(PATH_IN + 'qid.txt', names = ['index', 'question_id'])
    # M = pd.merge(M, qid, how = 'outer')

    # number_of_vote
    # vote = pd.read_csv(PATH_IN + 'vote.txt', names = ['index', 'vote'])
    # M = pd.merge(M, vote, how = 'outer')

    M = M.drop('index', axis = 1)
    M = M.fillna(0)
    print M

    M.to_csv(PATH_OUT + 'Normal_Features.txt',  index = False)

    '''
    m_norm = (m-m.mean()) / (m.max() - m.min())
    print m_norm

    print m.max()
    print m.min()
    print m.mean()
    #print m.std()
    '''

    #M_norm.to_csv('Normaliztion.txt',  index = False)




