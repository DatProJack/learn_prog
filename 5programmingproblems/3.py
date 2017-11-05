fibb=[0,1]
upto = int(raw_input("Print fibbonochi numbers up to: "))
for x in range(0,upto):
    print fibb[0]
    fibb[0]=fibb[0]+fibb[1]
    fibb.reverse()
