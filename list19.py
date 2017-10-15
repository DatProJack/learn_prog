lista=["Hello","World","in","a","frame"]
print("**********")
for x in range(0,len(lista)):
    y=5-len(lista[x])
    spaces=" "*y
    print "*",lista[x],spaces,"*"
print("**********")
