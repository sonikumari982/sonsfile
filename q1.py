name=input("enter the name")
b=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
"q","r","s","t","u","v","w","x","y","z"]
i=0
position=[]
while i<len(name):
    j=0
    while j<len(b):
        if name[i]==b[j]:
            position.append(j)
        j=j+1
    i=i+1
print(position)
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     if i in d2:
#         d2[i]=d2[i]+d1[i]
#     # else:
#     #     d2[i]=d1[i]
    
# print(d2)
# a=16
# b="soni"
# c=str(a)+b
# print(c)
