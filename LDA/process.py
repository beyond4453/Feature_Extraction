import re
import nltk
from nltk.corpus import stopwords

#nltk.download()
f_in1 = open('question_content.txt','r')
f_out1 = open('question_content_pro.txt','w')
f_in2 = open('answer_content.txt','r')
f_out2 = open('answer_content_pro.txt','w')
f_in3 = open('user_interest.txt','r')
f_out3 = open('user_interest_pro.txt','w')


for line in f_in1:
    word_list = line.split(',')[1].strip().split(' ')
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    print filtered_words
    f_out1.write(' '.join(filtered_words))
    f_out1.write('\n')

for line in f_in2:
    word_list = line.split(',')[1].strip().split(' ')
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    print filtered_words
    f_out2.write(' '.join(filtered_words))
    f_out2.write('\n')

for line in f_in3:
    word_list = line.split(',')[1].strip().split(' ')
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    print filtered_words
    f_out3.write(' '.join(filtered_words))
    f_out3.write('\n')


f_in1.close()
f_out1.close()
f_in2.close()
f_out2.close()
f_in3.close()
f_out3.close()



