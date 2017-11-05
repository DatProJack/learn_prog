listt=[1,2,3,5,6,8,9]
summ=0
global summ
for x in range(0,len(listt)):
    summ=summ+listt[x]
print summ, "1"

x=0
summ=0
while x<len(listt):
    summ=summ+listt[x]
    x+=1
print summ, "2"





def add(listname):
    if len(listname)==0:
        return 0
    else:
        y=listname[0]
        listname.pop(0)
        return y+add(listname)
print add(listt) , "3"
