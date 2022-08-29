# #my_file = open("people.txt")
# #file_data = my_file.read()
# #print (file_data)
# #my_file.close()
# #my_file2 = open("people1.txt", "w")
# #my_file2.write("Abhishek - Gurgaon1 \n\n priyanka - shiml \nneela - delhisashi - jaipur sarika - delhideepti - shimlaharshad - delhitrishna - delhipradeep - jaipursekhar - delhinand - delhianoop - delhibalwinder - jaipurEdit this code" )
# #my_file2.write("Ranveer - Delhi")
# #my_file2.close()
# #my_file3 = open("people3.txt", "w")
# #my_file3.write("Abhishek - Gurgaon\n")
# #my_file3.write("Ranveer - Delhi")
# #my_file3.close()
# #batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
# #students_file = open("navgurukul_students.html", "w")
# #students_file.write("\n")
# #students_file.write("\n")
# #students_file.write("\n")
# #students_file.write("\n")
# #students_file.write("\n")
# #students_file.write("")
# #for student in batch1_students:
# #    students_file.write("" + student + "\n")
# #    students_file.write("\n")
# #students_file.write("\n")
# #students_file.write("\n")
# #students_file.close()
# #my_file3 = open("test_file.txt", "a")
# #my_file3.write("Yahan main kuch likha")
# #my_file3.write("\nYaha maine kuch aur bhi likha.")
# #my_file3=open("test_file.txt","r")
# #print(my_file3.read())
# #my_file3.close()
# #my_file3=open("test_file.txt","r")
# #my_file3.read()
# #print(my_file3)
# my=open("people_excerccise.tet","r")
# print(my.read())
# #def name():
# #    a="hellow soni\n"
# #    return(a*5)
# #a=name()
# #print(a)
# # a=[7,4,3,9,2,5,0,1,5,]
# # i=0
# # while i<len(a):
# #     if a[i]%2==0:
# #         print(a[i],"even no.")
# #     else:
# #         print(a[i],"odd no.")
# #     i=i+1

# a=int(input("enter no."))
# if a<0:
#     print(a*-1)
# else:
#     print(a*-1)
# nums = [2,7,11,15]
# target = 9
# ###########QUESTION 1
# x ="124"
# b=list(x)
# a=[]
# i=-1
# while i>=(-len(b)):
#     a.append(b[i])
#     i=i-1
# if a==b:
#     print(a,"pelindrom")
# else:
#     print(":-is not pelindrom")
###########x=121
# a=x%10
# b=x//10
# c=b%10
# d=b//10
# e=a,c,d
# if e==x:
#     print("palindrom")
# else:
#     print("not palindrom")
# print(e)

# #########x=int(input("number "))
# y=x
# i=0
# re=0
# while x>0:
#     re=x%10
#     x//=10
# if y==re:
#     print("drom")
# else:
#     print("not")


# ###########x=int(input("number "))
# y=x
# i=0
# re=0
# while x>0:
#     re=x%10+(re*10)
#     x//=10
# if y==re:
#     print("drom")
# else:
#     print("not")
# print(y)

 #l1 = [2,4,3]
# l2 = [5,6,4]
# i=-1

############ QUESTION 2
# s = "abcabcbb"
# a=[]
# i=0
# while i<len(s):
#     if s[i] not in a:
#         a.append(s[i])
#     i=i+1
# print(len(a))


############QUESTION 3
# nums = [0,0,1,1,1,2,2,3,3,4]
# n=[]
# i=0
# while i<len(nums):
#     if nums[i] not in n:
#         n.append(nums[i])
#     if nums[i] in n:
#         n.append("_")
#     i=i+1

################QUESTION 4
# a=input("enter no.")
# c=input("enter no.")
# b=int(a)
# e=int(c)
# d=b*e
# f=str(d)
# print(f)

#########QUESTION  5

# number=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
# roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
# n=int(input("enter any no."))
# rom=""

# for i in range(len(number)):
#     m=n//number[i]
#     for j in range(m):
#         rom+=roman[i]
#     n=n%number[i]
# print(rom)

############QUESTION 6
# a=[1,7,7,4,5,5]
# i=0
# l=[]
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#             if c==2:
#                 if a[i] not in l:
#                     l.append(a[i])
#         j=j+1
#     i=i+1

###########QUESTION  7
# nums = [5,7,7,8,8,10]
# a=int(input("enter no."))
# i=0
# l=[]
# while i<len(nums):
#     if nums[i]==a:
#         l.append(i)
#     if a not in nums:
#         l.append(-1)
#         l.append(-1)
#         break
#     i=i+1
# print(l)

###########QUESTION  8
# a=['1','2','8']
# a.clear()
# print(a)

############3QUESTION  9  43
# a=int(input("enter no."))
# b=3
# c=a//b
# print(c)

#############QUESTION  10
# a=input("enter")
# if a>="()" or a>="(())":
#     print(len(a))
# elif a=="":
#     print(len(a))
# else:
#     print("not valid")

###########QUESTION  11
# nums = [4,5,6,7,0,1,2]
# a=int(input("enter no."))
# i=0
# while i<len(nums):
#     if nums[i]==a:
#         print(i)
#         break
#     if a not in nums:
#         print(-1)
#         break
#     i=i+1

##########QUESTION  12
# nums = [1,3,5,6]
# a=int(input("enter no."))
# i=0
# l=[]
# while i<=len(nums):
#     if nums[i]<a:
#         l.append(nums[i])
#     if nums[i]>=a:
#         break
#     i=i+1
# print(len(l))

############QUESTION  13 41
# nums =[3,4,-1,1]
# a=min(nums)
# b=max(nums)
# c=a
# i=0
# while i<len(nums):
#     if a<=b:
#         if c not in nums:
#             print(c)
#     c=c+1
#     i=i+1

# s = "abcabcbb"
# a=[]
# i=0
# while i<len(s):
#     j=0
#     c=0
#     while j<len(s):
#         if s[i]==s[j]:
#             c=c+1
#         if s[i] not in a:
#             a.append(s[i])
#         j=j+1
#     a.append(c)
#     i=i+1
# print(a)
#########################
# city_population ={
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
#     }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))
# Dict = {
#     'ball' : 'green',
#     'Ball': 'red'
#     }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])
# student={'name':"johan","age":25,"courses":["maths","science"]}
# for valu,key in student.items():
#     print(valu,key)
########### a=[4,5,5,5,3,8]
# i=0
# while i<len(a):
#     if a[i]==5:
#         print(a[i])
#         break
#     i=i+1
# a=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# while i<len(a):
#     if a[i]>=20 and a[i]<=40:
#         count+=1
#     i+=1
# print(count)
#  Dic= {1:'NAVGURUKUL',2:'IN',3:{'A':'WELCOME','B':'To','C':'DHARAMSALA'}}
# a=[True,False,False,True,False]
# i=0
# while i<len(a):
#     if a[i] in a:
#         c=int(a[i])
#         d=float(c)
#         print(d)
#     i+=1
# binary_number = [1, 0, 0, 1, 1, 0, 1,1, 1]
# i=0
# e=0
# while i<len(binary_number):
#     if binary_number[i] in binary_number:
#         c=float(binary_number[i])
#         e=e+c
#     i+=1
# print(e)