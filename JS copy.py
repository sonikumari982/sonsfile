##################
# from fileinput import close
# import json

# dict1 ={"emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },

#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     }
# }

# with open("qu1.json","w") as f:
#     json.dump(dict1,f,indent=4)

# f=open("que.json","w")
# json.dump(dict1,f,indent=4)

# f=close()
###################
# x =  { "name":"John", "age":30, "city":"New York"}

# # parse x:
# y = json.dumps(x)

# # the result is a Python dictionary:
# print(y)
##################
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# the result is a Python dictionary:
# print(y["age"])
###################   1
# from fileinput import close
# import json
# from os import write
# p =  { "name":"John", "age":30, "city":"New York"}
# i=open("newfil1.json","w")
# json.dump(p,i)
# i=close()
##########
# p =  { "name":"John", "age":30, "city":"New York"}
# i=open("newfil.json","w")
# f=json.dumps(p)
# print(f)
# i=close()

###################   2
# from fileinput import close
# import json


# x={
#     "name": "David", 
#     "class": "I", 
#     "age": 6
# }
# with open("newfile2.json","w") as f:
#     json.dump(x,f,indent=4)
#     a=json.dumps(x)
#     print(a)

###############   3
# import json


# dict1 ={"emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },

#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     }
# }
# with open("newfile3.json","w") as file:
#     json.dump(dict1,file,indent=4)
######
# import json


# dict1 ={ "name":"John", "age":30, "city":"New York"}
# with open("newfile4.json","w") as file:
#     a=json.dumps(dict1)
#     print(a)

##############  4
# import json


# dict={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# b=[]
# for i in dict:
#     b.append(i)
# b.sort()
# print(b)
# s={}
# for j in b:
#     for h in dict:
#         if j==h:
#             s[j]=dict[j]
# #print(s)
# with open("newfile4.json","w") as f:
#     json.dump(s,f,indent='')

##################   5
# import json


# a='{ "name":"John", "age":30, "city":"New York",5j:"hary"}'
# with open("newfile5.json","w") as f:
#     b=json.dumps(a)
# print(b)

#############   6
# import json


# dict='{"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}'
# with open("nwefile6.json","w") as file:
#     a=json.loads(dict)
# print(a)

######################
# a=input("enter name")
# c=a[-1]#+b
# f=len(a)-1
# h=c+a[1:f]+a[0:1]
# print(h)
##############
# from ast import Delete


# a=[1,2,3,4]
# b=[5,6,7,8,9,10,11,12,13]
# b[1:5]=[]
# print(f"this is {b}",max(b),min(b))
# a=15
# b=20
# print("bada hai")if a<b:else:print("chota hai")
# a=[(0,0),(0,1),(1,0),(1,2),(2,1),(2,2)]
# b=[]
# i=1
# while i<len(a)-1:
#     b.append(a[i])
#     i=i+1
# print(b)
#############3
from urllib import request


file=request.get("")