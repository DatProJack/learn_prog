choice=raw_input("Type s for sum and m for multiplacation: ")
num=int(raw_input("Give me a number: "))
answer=0
if(choice=="s"):
    for i in range(0,num+1):
        answer=answer+i
else:
    answer=1
    for i in range(1,num+1):
        answer=answer*i
print(answer)
