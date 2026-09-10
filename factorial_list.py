factlist=[]
for n in range(7):
    f=1
    i=1
    while(i<n):
        f=f*i
        i+=1
    factlist.append(f)
print(factlist)