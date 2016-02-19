import pandas as pd
import numpy as np
import operator
import re


PATH_IN = 'DIVIDE/match/'
PATH_OUT = 'DIVIDE/non-match/'

best = pd.read_csv(PATH_IN + 'best_answer.csv')
second = pd.read_csv(PATH_IN + 'second_answer.csv')
third = pd.read_csv(PATH_IN + 'third_answer.csv')

moved = pd.read_csv(PATH_OUT + 'best_answer_moved.csv')

moved_qc = moved['question_content']
moved_qt = moved['question_tags']

best['question_content'] = moved_qc
second['question_content'] = moved_qc
third['question_content'] = moved_qc

best['question_tags'] = moved_qt
second['question_tags'] = moved_qt
third['question_tags'] = moved_qt

best.to_csv(PATH_OUT + 'non_match_best.csv', encoding='utf-8', index = False)
second.to_csv(PATH_OUT + 'non_match_second.csv', encoding='utf-8', index = False)
third.to_csv(PATH_OUT + 'non_match_third.csv', encoding='utf-8', index = False)


