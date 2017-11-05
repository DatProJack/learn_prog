check=int(raw_input("Checking for : "))
bing=0
lis=[1,2,3,4,5,6,7,8,9,0,12,13,15,65,34,37,97,64,53,45]
for i in range(0,len(lis)):
    if(lis[i]==check):
        bing=1
        print "Yes,",check," is part of the set."
        break
if bing==0:
    print check,"is not part of the set."
