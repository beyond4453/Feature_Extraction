# Process with the Text features to remove the stop words and 
# Generate the source data used by LDA && OVER_LAP

import re
import nltk
import sys
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer

#nltk.download()


def remove_stop_words(fin, fout) :
    for line in fin:
        word_list = line.split(',')[1].strip().split(' ')
        filtered_words = [word for word in word_list if word not in stopwords.words('english')]
        print filtered_words
        fout.write(' '.join(filtered_words))
        fout.write('\n')

# do text - preprocessing 
# get tokens / remove stopwords / do stemming 
def text_processing(FIN, FOUT) :
    for line in FIN :
        stemmed = []

        # do some strip to get tokens 
        word_str = line.split(',')[1]
        word_str = word_str.replace('u\'', '\'')
        word_str = word_str.replace("'", "")
        word_str = re.sub(r"\W+", " ", word_str)
        word_list = word_str.strip().split(' ')
        
        # remove the stop words from tokens 
        filtered = [word for word in word_list if word not in stopwords.words('english')]
        print filtered
        # do stemming on the word 
        for word in filtered :
            #stemmed.append(PorterStemmer().stem(word))
            stemmed.append(SnowballStemmer("english").stem(word))
        FOUT.write(' '.join(stemmed))
        FOUT.write('\n')

    return 

def process_text_features(PATH_IN, PATH_OUT) :
    
    reload(sys)
    sys.setdefaultencoding('utf8')

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

    text_processing(f_in1, f_out1)
    text_processing(f_in2, f_out2)
    text_processing(f_in3, f_out3)
    text_processing(f_in4, f_out4)
    text_processing(f_in5, f_out5)
    text_processing(f_in6, f_out6)

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

