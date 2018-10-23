from __future__ import division
import csv
import math
print('--------------Symmetric-Measures-----------------')
#Correlation
print('-----------------Correlation------------------')
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        corr = ((row_9*row_1) - (row_5*row_7))/math.sqrt(row_5*row_6*row_7*row_8)
        l.append(corr)
        print(corr)
    #print(l)
    d = dict(zip(li, l))
    #print(d)
    print('------------------rankings-------------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))
print('--------------------Odds Ratio---------------------')
 #Odds Ratio 
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ora = (row_1*row_4)/(row_2*row_3)
        l.append(ora)
        print(ora)
    d = dict(zip(li, l))
    #print(d)
    print('---------------Rankings-----------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))
print('--------------------Kappa---------------------')
#kappa
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ka = ((row_9*row_1)+(row_9*row_4)-(row_5*row_7)-(row_6*row_8))/((row_9*row_9)-(row_5*row_7)-(row_6*row_8))
        print(ka)
        l.append(ka)
    d = dict(zip(li, l))
    #print(d)
    print('---------------Rankings-----------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))
print('--------------------Interest---------------------')
#interest
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        inte = (row_9*row_1)/(row_5*row_7)
        l.append(inte)
        print(inte)
    d = dict(zip(li, l))
    #print(d)
    print('---------------Rankings-----------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))
print('--------------------Cosine---------------------')
#cosine
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        cosi = row_1/math.sqrt(row_5*row_7)
        l.append(cosi)
        print(cosi)
    d = dict(zip(li, l))
    #print(d)
    print('---------------Rankings-----------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))
print('--------------------Piatetsky-Shapiro---------------------')
#Piatetsky-Shapiro
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ps = (row_1/row_9)-((row_5*row_7)/(row_9*row_9))
        l.append(ps)
        print(ps)
    d = dict(zip(li, l))
    #print(d)
    print('---------------Rankings-----------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))
print('--------------------Collective-Strength---------------------')
#Collective_Strength
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ps = ((row_1+row_4)/((row_5*row_7)+(row_6*row_8)))*((row_9-(row_5*row_7)-(row_6*row_8))/(row_9-row_1-row_4))
        print(ps)
        l.append(ps)
    d = dict(zip(li, l))
    #print(d)
    print('---------------Rankings-----------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))
print('--------------------Jaccard---------------------')
#Jaccard
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ja = (row_1)/(row_5+row_7-row_1)
        print(ja)
        l.append(ja)
    d = dict(zip(li, l))
    #print(d)
    print('---------------Rankings-----------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))
print('--------------------All-Confidence---------------------')
#all_confidence
l=[]
li = ["E1","E","E3","E4","E5","E6","E7","E8","E9","E10"]
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ac = min((row_1/row_5),(row_1/row_7))
        print(ac)
        l.append(ac)
    d = dict(zip(li, l))
    #print(d)
    print('---------------Rankings-----------------')
    for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
        print("%s: %s" % (key, value))