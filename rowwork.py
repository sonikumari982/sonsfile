# a=input("enter name")
# i=1
# c=(a[-1])
# b=c+""
# f=len(a)
# while i<len(a[1:f]):
#     b=b+a[i] 
#     i=i+1
# h=b+a[0]
# print(h)

# # #####################
# a=input("enter name")
# c=a[-1]#+b
# f=len(a)-1
# h=c+a[1:f]+a[0:1]
# print(h)

#######
# #initialize the string
# string1 = "hello, i am john, i work in marketing"

# #split the string
# x = string1.rsplit(', ')
# y = string1.rsplit()

# #print the lists
# print(x)
# print(y)
############
# string1 = "hello\ni am john\ni work in marketing"

# #split the string
# x = string1.splitlines()
# for l in x:
#     h=l.split()
#     print(h)

# #print the list
# print(x)
# # print(string1)
#######Escaping a String
# speech = "She said: \"Hi\""
# print(speech)
# #prints: She said: "Hi"
############# F-Strings
# days = 365
# print(f"There are {days}in a year")
###########
# for _ in range(1:100):
# #Do something 100 times.
# for _ in range(10): 
#     print("Hey! Listen!") 
###########
# while 5 > 1:
#     print("I'm a survivor")
###########
# list1 = [1, 2, 3]
# list2 = [9, 8, 7]
# new_list = list1 + list2
# list2 += list1
# print(list2)
# print(new_list)
##############
# letters = ["a","b","c","d"]
# print(letters[1:3])
#Result: ["b", "c"]
############# Randomisation   #####?????
# import random
# # randint(start, end)
# n = random.randint(2, 5)
# #n can be 2, 3, 4 or 5.
# print(n)
########### ads
# a=abs(-4.6)####### why we use -
# # result 4.6
# print(a)
######## new way of string
# print("print('what to print')")
# print('print("what to print")')
###########
# str="soni kumari"
# for i in str:
#     print(i)
# x=int(input("enetr"))
# y=int(input("enter"))
# a=x
# for i in range(1,y):
#     a=a*x
# print(a)
# print()
# x=int(input("enter"))
# y=int(input("enter"))
# a=x
# for i in range(1,y) :
# 	a=a*x
# print(a)
###########
# dic1={"googl":1,"feacebook":2,"mi":3}
# dic2={"gfg":1,"mi":2,"youtub":3}
# dic1.update(dic2);
# for key,value in dic1.items():
#     print(key,value)
#########3
# li=[]
# li.append([1,[2,3],4])
# li.extend([7,8,9])
# print(li)
# print(li[0][1][1])
# print(li[2])
##########
# a,b,c=int(input("enter")),int(input("enter")),int(input("enter"))
# print(a,b,c)
##############
# t=int(input())
# for i in range(t):
#     w,x,y,z=map(int,input().split())
#     b=w+(y*z)
#     if b>x:
#         print("OVERFLOW")
#     elif b==x:
#         print("Filled")
#     else:
#         print("UNFILLED")
###########
# w,x,y,z=map(int,input().split())
# print(w,x,y,z)
#############
# a=50
# b=""
# i=1
# while i<=50:
#     print(i)
#     a+=1
#     b=b+str(a)+("\n")
#     i+=1
# print(b)
############
# list = [5,6,[],3,[],[],9]
# for i in list:
#     if i == []:
#         list.remove(i)
# print(list)
# list = [5,6,[],3,[],[],9]
# a=[]
# i=0
# while i<=len(list):
#     if list[i]>=0:
#         a.append(list[i]) 
#     i=i+1
# print(a)
###################
# a={"nidhi":[20,25,30],
# "abhishak":[95,100,80],
# "shanti":[40,60,90],
# "avinas":[30,50,70]}
# sum1=0
# sum2=0
# sum3=0
# for valu in a.values():
#     count=0
#     while count<len(valu):
#         if count==0:
#             sum1+=valu[count]
#         elif count==1:
#             sum2+=valu[count]
#         elif count==2:
#             sum3+=valu[count]
#         count+=1
#print(sum1,sum2,sum3)
##############
# a={"nidhi":[20,25,30],
# "abhishak":[95,100,80],
# "shanti":[40,60,90],
# "avinas":[30,50,70]}
# def mark(a,i):
#     sum=0
#     z=[]
#     for value in a.values():
#         z.append(value[i])
#         sum=sum+value[i]
#     print(sum)
#     b=sum/len(z)
#     print(b)
# mark(a,0)
# mark(a,1)
# mark(a,2)
##################
# que_list=["Who Invented computer","Who invented Internet","When was python developed","what is the fullform of www."]
# opt_list=[["Vint cerf","Mark Jukerberg","Charls babbage","Robert Vintage"],["Vint cerf","vinton cerf", "Guido","John babbage"],["21 feb","20 feb","20 march","19 jan"],["world web wide","world wide web","world web webside","world wide webside"]]
# ans_list=[3,1,2,2]
# def call():
#     insilization=0
#     amount=0
#     while insilization<len(que_list):
#         print(que_list[insilization])
#         option=opt_list[insilization]
#         secinsilization=0
#         while secinsilization<len(option):
#             print(option[secinsilization])
#             secinsilization+=1
#         enter=int(input("enter the option......"))
#         if ans_list[insilization]==enter:
#             amount=500*(insilization+1)
#             print("right answere you win",amount)
#         else:
#             print("rong ansser\ngame over","your total amount",amount)
#             break

#         insilization+=1
# call()
#############3
# question_list=["How many continents are there?", "What is capital of India?", "Which course is taught in navgurukul?"]
# option_list=[["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
# answer_list=[3,4,1]
# def option(index):
#     j=0
#     while j<len(option_list[index]):
#         print(j+1,option_list[index][j])
#         j=j+1
#     user_ans = int(input('.....'))
#     if user_ans==answer_list[index]:
#         return True
#     else:
#         return False
# def que():
#     index=0
#     while index<len(question_list):
#         print("Q.",index+1,question_list[index],"?")
#         result=option(index)
#         if result=="no":
#             index+=1
#         elif result==True:
#             print("congratulations")
#         else:
#             print("you loose")
#             break   
#         index+=1

# def main():
#     que()
# main()
# a={"nidhi":[20,40,30],"abhishek":[95,100,80],"jyoti":[80,70,90]}
# def max_sub(a,i):
# 	sum=0
# 	num=val[i]
# 	for value in a.values():
# 		if num<=value[i]:
# 			num=value[i]
# 	return num
# for val in a.values():
# 	l=len(val)
# 	for index in range(l):
# 		print(max_sub(a,index))
# 	break
# a={"nidhi":[20,25,30],
# "abhishak":[95,100,80],
# "shanti":[40,60,90],
# "avinas":[30,50,70]}
# def mark(a,i):
#     sum=0
#     z=[]
#     for value in a.values():
#         z.append(value[i])
#         sum=sum+value[i]
#     maxv=max(z)
#     print(maxv)
# mark(a,0)
# mark(a,1)
# mark(a,2)
# a={"nidhi":[20,25,30],
# "abhishak":[95,100,80],
# "shanti":[40,60,90],
# "avinas":[30,50,70]}
# ##################
# def mark(a,i):
#     sum=0
#     z=[]
#     for value in a.values():
#         z.append(value[i])
#         sum=sum+value[i]
#     minv=min(z)
#     print(minv)
# mark(a,0)
# mark(a,1)
# mark(a,2)
###############
# n,atm=map(float,input().split())     ( ? )
# n=int(n)
# if (n+0.5<=atm and n%5==0):
#     print(float(atm-n-0.5))
# else:
#     print(float(atm))
#print((400*10)+(30*90))
# runtime=int(input())
# for i in range(runtime):
#     strvalu=input("enyer")
#     drom=strvalu[ : :-1]
#     if drom==strvalu:
#         print("wins")
#     else:
#         print("loses")
a="sonikumari"
print(a[-1::-1g])