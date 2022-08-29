# a=['deepa','mona','deepak','karuna']
# d=[]
# m=[]
# k=[]
# i=0
# while i<len(a):
#     if a[i][0]=='d':
#         d.append(a[i])
#     elif a[i][0]=='m':
#         m.append(a[i])
#     elif a[i][0]=='k':
#         k.append(a[i])
#     i=i+1
# print(d)
# print(m)
# print(k)

from os import write
from re import X


x=open("monakumari.txt","w")
x.write("mona")
c=x.close()

