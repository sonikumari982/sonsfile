# # # def sum(a,b):
# # #     return(a+b)
# # # def sub (a,b):
# # #     return(a-b)
# # # def function(a,b):
# # #     print(sum(a,b),sub(a,b))
# # # function(6,7)
# # # a="saniya"
# # # print(a[5:6],a[1:5],a[0:1])
# # 3#print(a[-1:-6])
# # # person={
# # #     'name':'jack',
# # #     'age':20,
# # #     'gender':'male',
# # #     4:'organisation'}

# # # result = person['age'] 
# # # x = person.get("gende")
# # # print(person[4])
# # # print(x)
# # # print(result)
# # person={
# #     'name':'jack',
# #     'age':20,
# #     'gender':'male',
# #     4:{'organisation':'navgurukul','place':'dharamsala'}
# #     }
# # print(person['gender'])

# # print(person[4])

# # result = person[4]['place']

# # print(result)
# dic= {
#  'Name': 'RAM', 
#  'Age': 17,
#  }
 
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)
# details={
#     'Name': 'RAM',
#     'Age': 17, 
#     'student': {
#         'id': 22,
#         'place': 'dharamsala'
#          }
#     } 
# details['student']['id']=35
# print(details)
# classes ={
# "room1":  "6th",
# "room2":  "7th",
# "room3":  "8th"
# }
# mydict=classes.copy()
# print(mydict)
# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state  in states_capitals:
#   print(state,states_capitals[state])
# states_capitals = {
# 'Gujarat' : 'Gandhinagar',
# 'Maharashtra' : 'Mumbai',
# 'Rajasthan' : 'Jaipur',
# 'Bihar' : 'Patna'
# }

# for state in states_capitals:
#     print(states_capitals[state])
############
#dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# c={}
# c.update(dic1)
# c.update(dic2)
# c.update(dic3)
# print(c)
######################
# dict1={"name":"raju","marks":56}
# a=input("enter the key name")
# if a in dict1 :
#     print("exist")
# else:
#     print("not exist")
#################
# my_dict = {
# 'data1':100,
# 'data2': -54,
# 'data3': 247
#   }
# sum=0
# for i in my_dict:
#     sum=sum+my_dict[i]
# print(sum)

###############
# Dic= {
# 1: 'NAVGURUKUL',
# 2: 'IN',  
# 3:{
# 'A' : 'WELCOME',
# 'B' : 'To',
# 'C' : 'DHARAMSALA'
# }}
# for i in Dic:
#     print(i,Dic[i])

################
# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# c={}
# for i in list1:
#     for j in list2:
#         c[i]=j
# print(c)

####################
# dic={"ball":"red",
# "bat":4,
# "wickets":8,
# "ball":"green",
# "bat":3
# }
# print(dic.items())
# for i,j in dic.items():
#     print(i,j)

################
# dic=[{"first":"1"}, 
# {"second": "2"}, 
# {"third": "1"}, 
# {"four": "5"}, 
# {"five":"5"}, 
# {"six":"9"},
# {"seven":"7"}]
# a=[]
# for i in dic:
#     for j,k in i.items():
#         if k not in a:
#             a.append(k)
# print(a)

################
# b={}
# for i in range (1,10):
#     a=input("enter the name")
#     c=int(input("enter the no."))
#     b[a]=c
# print(b)

############3
# a="MISSISSIPPI"
# b={}
# for i in a:
#     c=0
#     for j in a:
#         if j==i:
#             c=c+1
#     if i not in b:
#         b[i]=c
# print(b)

###############
# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# c=0
# for i in dict1.values():
#     a=len(i)
#     c=c+a
#     # for j in i:
#     #     c=c+1
# print("total count",c)

############
# my_dict = {
# 'a':50, 
# 'b':58, 
# 'c':56,
# 'd':40, 
# 'e':100, 
# 'f':20
# }
# a=[]
# for i in my_dict.values():
#     a.append(i)
# c=[]
# for j in range (1,4):
#     b=max(a)
#     c.append(b)
#     a.remove(b)
# print(c)

###############
# a={}
# for i in range (1,16):
#     a[i]=i*i
# print(a)

 
#########################    14
# b={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# f=[]
# for e in b.values():
#     f.append(e)
# g=[]
# for r in b:
#     s=max(f)
#     g.append(s)
#     f.remove(s)
# a={}
# for n in g:
#     for m,z in b.items():
#         if z==n:
#             a[m]=n
# print(f)

##################  13
# b = {
# 'a':50, 
# 'b':58, 
# 'c':56,
# 'd':40, 
# 'e':100, 
# 'f':20
# }
# f=[]
# for e in b.values():
#     f.append(e)
# g=[]
# c=0
# for r in b:
#     s=max(f)
#     g.append(s)
#     f.remove(s)
#     c=c+1
#     if c==3:
#         break
# a=[]
# for n in g:
#     for m,z in b.items():
#         if z==n:
#             a.append(m)
# print(a)

#################   1
# a = {(1,2):1,(2,3):2}
# print(a[1,2])
################   2
# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])
######################     3
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print(len(fruit))
# print(fruit)
#########################    4
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print(len(Details["Student"]))
##########################   5
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print(sum)
# print(my_dict)
######################   6
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates['box']))
###################     7
# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
# "Name" : "Python", 
# "Age":"20", 
# "Addr" : "NJ", 
# "Country" : "USA"
# }
# id2 = id(rec)
# print(id1 == id2)
###################
# details={
# "name":"Shanti",
# "age":12,
# "email":"shanti@navgurukul.org"
# }

# print(details["name"])
# print(details["name"])
# print(details["age"])
################
# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():
#     sum=sum+i
# print(sum)
#####################
# dict={}
# c=0
# for i in range(1,16):
#     c=i*i
#     dict[i]=c
# print(dict)
#############
# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)
# print(s[0])
############## document question
###########      1
# a=int(input("enter no"))
# b={}
# i=1
# while i<=a:
#     f=0
#     c=[]
#     while f<=10:
#         e=i*f
#         c.append(e)
#         f=f+1
#     b[i]=c
#     i+=1
# print(b)

#################
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# b={}
# for i,c in d1.items():
#     for h,n in d2.items():
#         if i==h:
#             a=n+c
#         b[i]=a
#         if i!=h:
#             b[i]=c
# print(b)
###################
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     if i in d2:
#         d2[i]=d2[i]+d1[i]
#     else:
#         d2[i]=d1[i]
    
# print(d2)

############    2
# a='w3resource'
# b={}
# for i in a:
#     c=0
#     for j in a:
#         if j==i:
#             c=c+1
#     if i not in b:
#         b[i]=c
# print(b)

#################   3
# n=int(input("enter the no."))
# a={}
# i=1
# while i<=n:
#     c=i*i
#     a[i]=c
#     i=i+1
# print(a)

##################    4
# n=15
# a={}
# i=1
# while i<=n:
#     c=i*i
#     a[i]=c
#     i=i+1
# print(a)

############   5
#############    6
# a=int(input("entr the no."))
# dic={}
# i=10
# c=0
# while c<=a:
#     dic[c]=i
#     c=c+1
#     i=i+10
# print(dic)

############     7
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# b={}
# for i in (dic1,dic2,dic3):
#     b.update(i)
# print(b)

#############    8
# a={"banana":12,"apple":26,"orange":7}
# n=input("enter the name")
# if n in a:
#     print("the words exist in a dic")
# else:
#     print("the words not exist in a dic")

##############    9
# a={"banana":12,"apple":26,"orange":7}
# for i,j in a.items():
#     print(i,j)

###############   10
# a=15
# dic={}
# i=1
# while i<=a:
#     c=i*i
#     dic[i]=c
#     i=i+1
# print(dic)

###############    11
# a={"banana":12,"apple":26,"orange":7}
# c={'python':20,"gaurav":300,'dev':34,"karan":43}
# for i,j in c.items():
#     a[i]=j
# print(a)

###############   12
# c={'python':20,"gaurav":300,'dev':34,"karan":43}
# for i,j in c.items():
#     print(i,j)

###############    13
# a={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# sum=0
# for i,j in a.items():
#     sum=sum+j
# print(sum)

#############    14
# dic={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# mul=1
# for i in dic.keys():
#     mul*=i
# print(mul)

###############   15
# c={'python':20,"gaurav":300,'dev':34,"karan":43}
# if "dev" in  c:
#     c.pop("dev")
# print(c)

#############    16 not work
# list1=["map","erea","state","frutse"]
# list2=["indiya","2scure",29,26]
# dic={}
# for i,j in list1,list2:
#     dic[i]=[j]
# print(i)

############   16
# list1=["map","erea","state","frutse"]
# list2=["india","2squre",29,26]
# dic={}
# i=0
# while i<len(list1):
#     dic[list1[i]]=list2[i]
#     i=i+1
# print(dic)
#############################
a=int(input("enter no."))
b=""
print("even no.")
i=0
while i<=a:
    if i%2==0:
        print(i)
    else:
        b=b+str(i)+("\n")
    i=i+1
print("odd no")
print(b)
##############    17
# b={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# f=[]
# for e in b.values():
#     f.append(e)
# g=[]
# for r in b:
#     s=max(f)
#     g.append(s)
#     f.remove(s)
# a={}
# for n in g:
#     for m,z in b.items():
#         if z==n:
#             a[m]=n
# print('\33[31m',a)

###################   18
# b={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# f=[]
# for e in b.values():
#     f.append(e)
# a=max(f)
# c=min(f)
# dic={}
# for k,l in b.items():
#     if a==l:
#         dic[k]=l
#     if c==l:
#         dic[k]=l
# print(dic)

###########################   19
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#        },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    }
# }
# a={}
# for i,j in student_data.items():
#     if j not in a.values():
#         a[i]=j
# print(a)
# for i,j in student_data.items():######## not work
#      c=0
#      for h,r in student_data.items():
#         if r==j:
#             c=c+1
#         if c==2:
#             student_data.popitem()
#print(student_data)

###########################      20
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for b in d1:
#     if b in d2:
#         d2[b]=d2[b]+d1[b]
#     else:
#         d2[b]=d1[b]
#         #a[b]=d2[b]
# print(d2)
# #######################
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# a={}
# for i in d1:
#     if i in d2:
#         a[i]=d2[i]+d1[i]
#     else:
#         a[i]=d1[i]   
# print(a)

###################   21
# Sample_Data=[{"V":"S001"},
# {"V": "S002"},
# {"VI": "S001"},
# {"VI": "S005"},
# {"VII":"S005"},
# {"V":"S009"}
# {"VIII":"S007"}]
# dic={}
# for i in (-Sample_Data):
#     for j,p in i.items():
#         if j not in dic:
#             dic[j]=p
# print(dic)

###############
# a=[10,40,5]
# f={}
# i=0
# while i<len(a):
#     c=""
#     j=0
#     b=str(a[i])
#     while j<len(b):
#         if b[j]=="0":
#             c=c+"zero"
#         if b[j]=="1":
#             c=c+"one"
#         if b[j]=="2":
#             c=c+"two"
#         if b[j]=="3":
#             c=c+"three"
#         if b[j] =="4":
#             c=c+"four"
#         if b[j] =="5":
#             c=c+"five"
#         j=j+1
#     f[a[i]]=c
#     i=i+1
# print(f)
###############
# dic={"a":5,"b":40,"c":50}
# list=[]
# dic1={}
# for i in dic.values():
#     list.append(i)
# maxvalu=max(list)
# # minvalu=min(list)
# for j,k in dic.items():
#     if maxvalu == k:
#         dic1[j]=maxvalu
#     # if minvalu == k:
#     #     dic1[j]=minvalu
# print(dic1)

# dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# for key in dic:
#     str=""
#     for key1 in key:
#         if key1==" ":
#             continue
#         str=str+key1
#     dic.update({str:dic[key]})
# print(dic)
################
# dic = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# dic1={}
# for i,j in dic.items():
# 	if " " in i:
# 		s=""
# 		for e in i:
# 			if " " !=e:
# 				s=s+e
# 	dic1[s]=dic[i]
# print(dic1)


# dic={"a":5,"b":40,"c":50}
# max=0
# for i in dic:
#     max=dic[i]>dic[i]

# print(max)
