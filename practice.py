# def inputting():
#     h=input()
#     user=h.split()
#     for i in range(len(user)):
#         user[i]=int(user[i])
#     return user


# def counting(l):
#     count={}
#     p=[1,2,3,4,5,6,7,8,9,10]
#     for j in range(len(p)):
#         for k in l:
        
#             if j==k:
#                 count[j]=count[j]+1
#             else:
#                 count[j]=1
#     return count








# d=counting(inputting())
# for key,value in d.items():
#     print(f"{key}: {value}")


# s=[{"author":"Clive Barker","isbn":"0743417321","title":"Cabal","year":"1988"},{"author":"Iain M. Banks","isbn":"0061053562","title":"The Player of Games","year":"1988"},{"author":"Terry Pratchett","isbn":"0061020664","title":"Wyrd Sisters","year":"1988"},{"author":"James Ellroy","isbn":"0099366614","title":"The Big Nowhere","year":"1988"},{"author":"Nelson DeMille","isbn":"0751531189","title":"The Charm School","year":"1988"},{"author":"Neal Stephenson","isbn":"0553573861","title":"Zodiac","year":"1988"},{"author":"Sue Grafton","isbn":"0312939035","title":"E Is for Evidence","year":"1988"}]
# g=s.count()
# g=len(s)
# for i in range(g):
#     print([s[i]["author"],s[i]["title"],s[i]["isbn"],s[i]["year"]])

def maximum(s):
    f={}
    for i in s:
        if i in f:
            f[i]+=1
        else:
            f[i]=1

# maximum=max(f,key=f.get)
# print(maximum)
    for key,value in f.items():
    # print ("% d : % d",(key, value))
        if value % 2 !=0:
            return(key)
        
    return(0)



n=input()
s=input().split()
print(maximum(s))

    
