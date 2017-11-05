between=[0,0,0,0,0,0,0,0]
for x in range(1,6562):
    for y in range(0,7):
        between[y]=(x/3**y)%3
    e="1"
    for i in range(2,10):
        if(between[i-2]==0):
            b="-"
        if(between[i-2]==1):
            b="+"
        if(between[i-2]==2):
            b=""
        e=e+b+`i`

    ad=eval(e)
    if(ad==100):
        print e,"=",ad
