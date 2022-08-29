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
# print(a)

#############   6
# import json


# dict='{"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}'
# with open("nwefile6.json","w") as file:
#     a=json.loads(dict)
# print(a)
###########   7
import json
f = open("log_events.log", "r")
content = f.read()
splitcontent = content.splitlines()
# print(splitcontent)
a={}
for line in splitcontent :
    pipesplit = line.split()
    list1=list(pipesplit)
    key=""
    value=""
    i=0
    while i<len(list1):
        if i<=0:
            key=key+list1[i]
        else:
            value=value+list1[i]+(" ")
        i=i+1
    a[key]=value
print(a)
with open("newfile7.json","w") as file:
    json.dump(a,file,indent="")

################  8
# import json


# forkey=["name","Designation","Age","salary"]
# detalist=[
# ["neelam","programer","24","2400"],
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"]]
# empytdict={}
# emp1={}
# emp2={}
# emp3={}
# emp4={}
# i=0
# while i<=len(forkey):
#     j=i
#     while j<len(detalist):
#         a=detalist[0][j]
#         emp1[forkey[i]]=a
#         b=detalist[1][j]
#         emp2[forkey[i]]=b
#         c=detalist[2][j]
#         emp3[forkey[i]]=c
#         d=detalist[3][j]
#         emp4[forkey[i]]=d
#         if j==i:
#             break
#         j=j+1
#     i=i+1
# empytdict["emp1"]=emp1
# empytdict["emp2"]=emp2
# empytdict["emp3"]=emp3
# empytdict["emp4"]=emp4
# #print(empytdict)
# with open("newfile8.json","w") as file:
#     json.dump(empytdict,file,indent="")

###############    9
# a={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }
##############
# import json


# a={"mona":"kumari"}
# with open("monakumari.py","w")as file:
#     json.dump(a,file)





