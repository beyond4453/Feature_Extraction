from pandas import Series, DataFrame
from extract import *
from process import *
from overlap import *
from lda import *
from normalize import *

FILE = 'non_match_third.csv'
ANSWER_DEGREE = 'THIRD'

MATCH = False
if MATCH is True:
    PATH_IN = 'DIVIDE/MATCH/' + FILE
    PATH_OVERLAP = 'MATCH/' + ANSWER_DEGREE + '/OVERLAP/'
    PATH_NORMAL = 'MATCH/'+ ANSWER_DEGREE + '/NORMAL/'
    PATH_LDA = 'MATCH/' + ANSWER_DEGREE + '/LDA/'
    PATH_TEXT = 'MATCH/'+ ANSWER_DEGREE + '/TEXT/'
else :
    PATH_IN = 'DIVIDE/NON-MATCH/' + FILE
    PATH_OVERLAP = 'NON-MATCH/' + ANSWER_DEGREE +'/OVERLAP/'
    PATH_NORMAL = 'NON-MATCH/' + ANSWER_DEGREE + '/NORMAL/'
    PATH_LDA = 'NON-MATCH/' + ANSWER_DEGREE + '/LDA/'
    PATH_TEXT = 'NON-MATCH/' + ANSWER_DEGREE + '/TEXT/'


# First Step : you need to run the Generate_non_match_data.ipynb
#              to generate non-match instances

# extract.py : 
# extract_normal_features : f1 - f13
extract_normal_features(PATH_IN, PATH_NORMAL)

# extract.py :
# extract_text_features : extract text features
extract_text_features(PATH_IN ,PATH_TEXT)

# process.py : 
# process_text_features : remove stop words from the text
# generate file for overlap.py
# TODO : you need to do more text processing here
process_text_features(PATH_TEXT, PATH_OVERLAP)


# overlap.py : 
# extract_overlap_features : f15 - f17
extract_overlap_features(PATH_OVERLAP, PATH_OVERLAP, PATH_NORMAL)

# lda.py :
# lda_source : contact text to the LDA_SOURCE.txt
lda_source(PATH_OVERLAP, PATH_LDA)

# normalize.py :
# 
normalize(PATH_NORMAL, PATH_NORMAL)

# Then you need to do contact.py
# contact the normal features && LDA features && s2v features


