s=input().split(",")

l=[]
for i in s:
    
    i=int(i)
    l.append(i)
mi=min(l)
l2=[]
for i in l:
    if(i==mi):
        continue
    else:
        l2.append(i)
if(len(l2)!=0):
    print(min(l2))
else:
    print("No Gifts Available")