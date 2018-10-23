# -*- coding: utf-8 -*-
"""
Created on Tue Aug 07 12:41:57 2018

@author: Jijnasa
"""
import csv
ag = 0
su = 0.0
print('-------------------------2nd----------------')
with open('patientdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    for i in range(6):
        row = next(csv_reader)
        print(row)

    print("--------------3rd----------------------")
with open('patientdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    row = next(csv_reader)
    for row in csv_reader:
        if row[2]=='Male':
            row[2] = 0
        else:
            row[2] = 1
        print(row)
    print("----------------4th------------------------")
with open('patientdata.csv') as csv_file:
    reader = csv.reader(csv_file)
    r = next(reader)
    for r in reader:
        if r[4]=='TRUE':
            r[4] = 1
        else:
            r[4] = 0
        print(r)
    print("--------------5th--------------------------")
with open('patientdata.csv') as csv_file:
    reader = csv.reader(csv_file)
    r = next(reader)
    s = 0
    for r in reader:
        if r[1] == '':
            r[1] = 0
        s += int(r[1])
    s = s//10
    print(s)
with open('patientdata.csv') as csv_file:
    reader = csv.reader(csv_file)
    for r in reader:
        if r[1] == '':
            r[1] = s
        print(r)
with open('patientdata.csv') as csv_file:
    reader = csv.reader(csv_file)
    r = next(reader)
    for r in reader:
        if r[3] == '':
            ag = r[1]
with open('patientdata.csv') as csv_file:
    reader = csv.reader(csv_file)
    r = next(reader)
    
    c = 0
    for r in reader:
        if r[1] == ag and r[3]!='':
            su += float(r[3])
            c+=1
    su = su/c
l = []
with open('patientdata.csv') as csv_file:
    reader = csv.reader(csv_file)
    read = next(reader)
    for read in reader:
        if read[3] == '':
            read[3]=su
        print(read)
        l.append(read)
with open('patientdata_man.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(l)

    #print(su)
        #print(s)
              