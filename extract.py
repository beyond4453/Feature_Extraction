# extracting the normal features 
# extracting the text features


import pandas as pd


def str_strip(data) : 
    data = data.str.replace('u\'','\'')
    data = data.str.replace('?','')
    data = data.str.replace('"','')
    data = data.str.replace('.','')
    data = data.str.replace(',','')
    data = data.str.replace('/',' ')
    data = data.str.replace('(','')
    data = data.str.replace(')','')
    data = data.str.replace('[','')
    data = data.str.replace(']','')
    data = data.str.replace('&','')
    data = data.str.replace('\'','')
    data = data.str.replace('!','')
    data = data.str.replace('-','')
    data = data.str.replace(';','')
    return data

def extract_normal_features(path_in, path_out): 
    m = pd.read_csv(path_in)

    # calculate the features
    # question_id :
    question_id = m['question_id']
    question_id.to_csv(path_out+'/qid.txt')

    # vote :
    vote = m['answer_voted']
    vote.to_csv(path_out+'/vote.txt')

    # feature1 : length of the answer_content 
    #answer_content = m[['answer_content','user_id']]
    answer_content = m['answer_content']
    # f1 : length of the answer_content
    f1 = answer_content.str.len()
    f1.to_csv(path_out+'/f1.txt')
    #print answer_content


    # feature2 : length of the user_introduction
    user_intro = m['user_intro']
    #print user_intro
    f2 = user_intro.str.len()
    f2.to_csv(path_out+'/f2.txt')
    #print f2


    # feature3 : length of the question_content
    question_content = m['question_content']
    f3 = question_content.str.len()
    #print f3
    f3.to_csv(path_out+'/f3.txt')


    # feature4: user's experience years
    user_exp = m['user_exp']
    f4 = m['user_exp']
    f4 = f4.str.extract('([0-9]*)')
    f4.to_csv(path_out+'/f4.txt')
    #print f4

    # feature5 : length of the user's edu
    user_edu = m['user_edu']
    f5 = user_edu.str.len()
    f5.to_csv(path_out+'/f5.txt')
    #print f5


    # feature6 : number of topics of user's interest
    user_interest = m['user_interest']
    f6 = user_interest.str.len()
    f6.to_csv(path_out+'/f6.txt')
    #print f6


    # feature7 : number of the people user followed
    user_followed = m['user_followed']
    f7 = user_followed.str.len()
    f7.to_csv(path_out+'/f7.txt')
    #print f7

    # feature8 : number of the question tags
    question_tags = m['question_tags']
    f8 = question_tags.str.len()
    f8.to_csv(path_out+'/f8.txt')
    #print f8


    # feature9 : number of saved lives
    saved_lives = m['user_saved']
    f9 = saved_lives
    f9.to_csv(path_out+'/f9.txt')
    #print f9


    # feature10 : number of recieved thanks
    recieved_thanks = m['user_thanks']
    #recieved_thanks = str(recieved_thanks)
    f10 = recieved_thanks.str.replace(',','')
    f10.to_csv(path_out+'/f10.txt')
    #print f10


    # feature11 : number of agrees
    recieved_agrees = m['user_agrees']
    f11 = recieved_agrees.str.replace(',','')
    f11.to_csv(path_out+'/f11.txt')
    #print f11


    # feature12 : nuber of helped people
    helped = m['user_helped']
    f12 = helped.str.replace(',','')
    f12.to_csv(path_out+'/f12.txt')
    #print f12


    # feature13 : number of doctor recommend
    recommend = m['user_recommends']
    f13 = recommend.str.len()
    f13.to_csv(path_out+'/f13.txt')
    #print f13

    # feature14 : total length of the recommends
    # recommend_str = m['user_recommends']
    # recommend_str = ','.join(str(v) for v in recommend_str)
    # f14 = recommend_str.to_string
    # print f14
    #f14.to_csv('f14.txt')


# Extracting for the TEXT FEATRUES
def extract_text_features(path_in, path_lda):
    
    m = pd.read_csv(path_in)

    # Process with the question_content
    qc = m['question_content']
    #qc = str_strip(qc)
    #print qc
    qc.to_csv(path_lda+'/question_content.txt', encoding='utf-8')

    # Process with the answer_content
    ac = m['answer_content']
    #ac = str_strip(ac)
    ac.to_csv(path_lda+'/answer_content.txt', encoding='utf-8')

    # Process with the user_recommends
    ur = m['user_recommends'].astype(str)
    #ur = str_strip(ur)
    ur.to_csv(path_lda+'/user_recommends.txt', encoding='utf-8')

    # Process with question_tags
    qt = m['question_tags'].astype(str)
    #qt = str_strip(qt)
    #print qt
    qt.to_csv(path_lda+'/question_tag.txt', encoding='utf-8')

    # Process with user_interest
    ut = m['user_interest'].astype(str)
    #ut = str_strip(ut)
    ut.to_csv(path_lda+'/user_interest.txt', encoding='utf-8')

    # Proecess with user_specialty
    us = m['user_specialty'].astype(str)
    #us = str_strip(us)
    us.to_csv(path_lda+'/user_specialty.txt', encoding='utf-8')
    
    
