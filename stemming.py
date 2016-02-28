import re
import nltk
import sys
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

def do_stemming(fin, fout):
    #stemmed = []
    for line in fin :
        #wordlist = line.split(',')[1]
        # wordlist = nltk.word_tokenize(wordlist)
        # remove the stop word
        stemmed = []
        
        word_str = line.split(',')[1]
        word_str = word_str.replace('u\'', "\'")
        word_str = word_str.replace("'", "")
        word_str = re.sub(r"\W+", " ", word_str)
        #print word_str
        
        #wordlist = line.split(',')[1].strip().split(' ')
        wordlist = word_str.strip().split(' ')
        print wordlist
        
        filtered = [word for word in wordlist if word not in stopwords.words("english")]
        # do stemming on the word
        # stemmed = [PorterStemmer().stem(word) for word in filtered]
        for word in filtered :
            stemmed.append(SnowballStemmer('english').stem(word))
            #stemmed.append(PorterStemmer().stem(word))
        fout.write(' '.join(stemmed))
        fout.write('\n')
    return 



if __name__ == "__main__" :
    
    reload(sys)
    sys.setdefaultencoding('utf8')

    PATH_IN = "./MATCH/BEST/TEXT/question_tag.txt"
    PATH_OUT = "./MATCH/BEST/OVERLAP/qt_stemmed.txt"
    
    fin = open(PATH_IN, 'r')
    fout = open(PATH_OUT, 'w')

    do_stemming(fin, fout)
    print "Done" 

    fin.close()
    fout.close()

    


