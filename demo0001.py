'''
hlist = [1,2,3,"fan","haha","樊"]
hlist.append("f")
hlist2 = hlist.copy()
num = hlist.count("abc")
hlist.extend("xu")
num = hlist.index("樊")
hlist.insert(0,"第一位")

print(hlist)
'''



for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,"\t",end="")
    print("")

