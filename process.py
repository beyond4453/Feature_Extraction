# Process with the Text features to remove the stop words and 
# Generate the source data used by LDA && OVER_LAP

import nltk
from nltk.corpus import stopwords
#nltk.download()

#PATH_IN = 'DIVIDE/match/best_answer_features/TEXT_FEATURES/'
#PATH_OUT = 'DIVIDE/match/best_answer_features/LDA/'
#PATH_OUT = 'DIVIDE/match/best_answer_features/OVER_LAP/'

def remove_stop_words(fin, fout) :
    for line in fin:
        word_list = line.split(',')[1].strip().split(' ')
        filtered_words = [word for word in word_list if word not in stopwords.words('english')]
        print filtered_words
        fout.write(' '.join(filtered_words))
        fout.write('\n')

def process_text_features(PATH_IN, PATH_OUT) :
    f_in1 = open(PATH_IN+'question_content.txt','r')
    f_out1 = open(PATH_OUT+'question_content_pro.txt','w')

    f_in2 = open(PATH_IN+'answer_content.txt','r')
    f_out2 = open(PATH_OUT+'answer_content_pro.txt','w')

    f_in3 = open(PATH_IN+'user_interest.txt','r')
    f_out3 = open(PATH_OUT+'user_interest_pro.txt','w')

    f_in4 = open(PATH_IN+'question_tag.txt','r')
    f_out4 = open(PATH_OUT+'question_tag_pro.txt','w')

    f_in5 = open(PATH_IN+'user_recommends.txt','r')
    f_out5 = open(PATH_OUT+'user_recommends_pro.txt', 'w')

    f_in6 = open(PATH_IN+'user_specialty.txt', 'r')
    f_out6 = open(PATH_OUT+'user_specialty_pro.txt', 'w')

    remove_stop_words(f_in1, f_out1)
    remove_stop_words(f_in2, f_out2)
    remove_stop_words(f_in3, f_out3)
    remove_stop_words(f_in4, f_out4)
    remove_stop_words(f_in5, f_out5)
    remove_stop_words(f_in6, f_out6)

    f_in1.close()
    f_out1.close()
    f_in2.close()
    f_out2.close()
    f_in3.close()
    f_out3.close()
    f_in4.close()
    f_out4.close()
    f_in5.close()
    f_out5.close()
    f_in6.close()
    f_out6.close()

