#try put right input in forst instances

inp=input()
lst=[a for a in inp.split(' ')]
d={}

# actual code begins

for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

#final one

for i in d.keys():
    print(i+": "+str(d[i]))
# Thats the answer
