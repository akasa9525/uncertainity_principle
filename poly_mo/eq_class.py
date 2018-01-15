# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:45:47 2017

@author: Aditya
"""


import csv 
dic = {}

count = {}
tcount = {}

fd = open("eq_class_trans.txt").read().strip().split("\n")
       

for i in fd:
    count[i] = 0
    tcount[i] = 0

f= open("eq_class_eq.txt").read().strip().split("\n")



#df_eq_trans = pd.read_csv("eq_class_trans.txt", sep='\n')
#df_eq_trans['read_count'] = 0
#df_eq_trans['t_count'] = 0
#df_eq_trans['w_avg'] = 0

#f = open("eq_class_eq.txt")

#print(f)
for line in f:
    #print(line)
    line = line.strip().split("\t");
    #print (line)
    #print(line[0],line[-1])
    last = line[-1]
    first = line[0]
    for i in line[1:-1]:
        #print(i)
        #print(df_eq_trans['Transcript_id'][int(i)])
        #print(i)
        #print(last,first)
        #print (df_eq_trans['read_count'][int(i)])
        #print (df_eq_trans[df_eq_trans['Transcript_id']=='ENST00000375898'])
        count[fd[int(i)]] += 1
        tcount[fd[int(i)]] += int(first)
        #df_eq_trans['read_count'][int(i)] = df_eq_trans['read_count'][int(i)] + int(last)
        #df_eq_trans['t_count'][int(i)] = df_eq_trans['t_count'][int(i)] + (int(last)*int(first))
        #print (df_eq_trans[df_eq_trans['Transcript_id']=='ENST00000375898'])
    #break


#qwer = open('rcount.txt', 'w')
#qwer1 = open('tcount.txt', 'w')
#qwer = open('rcount.txt', 'w')

with open('num_times.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in count.items():
       writer.writerow([key, value])


with open('tcount_new.csv', 'wb') as csv_file1:
    writer = csv.writer(csv_file1)
    for key, value in tcount.items():
       writer.writerow([key, value])

csv_file.close()
csv_file1.close()
