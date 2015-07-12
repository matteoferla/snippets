__author__ = 'Matteo'

import os.path, os,glob, time, csv, re
#print "last modified: %s" % time.ctime(os.path.getmtime(file))
#print "created: %s" % time.ctime(os.path.getctime(file))

class photo:
    def __init__(self,file):
        self.time=os.path.getctime(file)
        self.long_name=file
        if file.find('bd_bokeh') >0:
            self.bk='prom'
        elif file.find('Night View 3') >0:
            self.bk='NYC'
        elif file.find('plane - Copy') >0:
            self.bk='C17'
        elif file.find('crest') >0:
            self.bk='crest'
        else:
            self.bk='UNKNOW'
        try:
            self.name=re.match('DSC\d+',file).group(0)
        except AttributeError:
            self.name='UNKNOWN'

    def __str__(self):
        return self.name+' made on '+str(time.ctime(self.time))+' with bk '+self.bk

class album:
    def __init__(self,path):
        self.data=[]
        os.chdir(path)
        for file in sorted(glob.glob("*.jpg")):
            f=photo(file)
            self.append(f)

    def __add__(self, other):
        self.data.append(other)

    def append(self,other):
        self.data.append(other)

    def __len__(self):
        return len(self.data)

    def csv(self,rowhead):
        return [[rowhead, x.name,x.time,x.bk] for x in self.data]



soldball=album("D:\\High Res")
print(len(soldball))
unsoldball=album("D:\\choose_raw")
print(len(unsoldball))

with open('D:\\data.csv', 'w') as csvfile:
    data = csv.writer(csvfile)
    data.writerows(unsoldball.csv('unsold'))
    data.writerows(soldball.csv('sold'))

