# f=open('test.txt')
# print(f.read())
# f.close()

import csv
with open('test.csv','w+') as f:
    w=csv.writer(f)
    w.writerow(['name','age','education'])
