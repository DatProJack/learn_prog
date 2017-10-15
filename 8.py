import time
t1 = time.clock()
upto=int(raw_input("Print prime's upto: "))
primes=[2]
check=1
for num in range(2,upto+1):
    check=1
    for x in range(0,len(primes)-1):`
        if(num%primes[x]==0):
            check=0
    if(check==1):
        primes.append(num)
        print(len(primes)-1," + ",num)
t0=time.clock()
time=t0-t1
print(time)
