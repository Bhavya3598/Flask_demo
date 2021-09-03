
def maximum(s):
    f={}
    for i in s:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    for key,value in f.items():
    # print ("% d : % d",(key, value))
        if value % 2 !=0:
            return(key)
        
    return(0)



n=input()
s=input().split()
print(maximum(s))

    
