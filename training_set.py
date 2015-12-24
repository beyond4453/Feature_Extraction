# select the qa pair in the souce
# subject to num of answers >= 3


with open('qid_ex.txt', 'r') as f:
    qid_list = [line.strip() for line in f]

with open('uid_ex.txt', 'r') as f1:
    uid_list = [line.strip() for line in f1]


f_in1 = open('answer.json', 'r')
f_in2 = open('question.json', 'r')
f_in3 = open('qtags.json', 'r')
f_in4 = open('user.json', 'r')

f_out1 = open('a_source.json', 'w')
f_out2 = open('q_source.json', 'w')
f_out3 = open('qtag_source.json', 'w')
f_out4 = open('u_source.json', 'w')

for line in f_in1:
    info = line.split('"')
    qid = info[3]
    if qid in qid_list:
        print qid
        f_out1.write(line)

for line in f_in2:
    info = line.split('"')
    qid = info[-2]
    if qid in qid_list:
        print qid
        f_out2.write(line)

for line in f_in3:
    info = line.split('"')
    qid = info[-2]
    if qid in qid_list:
        print qid
        f_out3.write(line)

for line in f_in4:
    info = line.split('"')
    uid = info[3]
    if uid in uid_list:
        print uid
        f_out4.write(line)
        uid_list.remove(uid)

f_in1.close()
f_in2.close()
f_in3.close()
f_in4.close()

f_out1.close()
f_out2.close()
f_out3.close()
f_out4.close()
