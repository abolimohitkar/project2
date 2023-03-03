#multipy elements in list
# l=[1,2,3,40,5,6,10]
# l1=[]
# for i in l:
#     x=i*i
#     l1.append(x)
# print(l1)

# def x(l):
#     t=1
#     for i in l:
#         t=i*i
#         return t
        
# z=x([10,20,3,5,1])
# print(z)
#find the max value in list
# def x(l):
#     max=l[0]
#     for i in l:
#         if i > max:
#             max=i
#     return max

# print(x([1,2,3,5]))

#find the min value in list

# def x (l):
#     min=l[0]
#     for i in l:
#         if i<min:
#             min=i
#     return min
# print(x([1,2,4,5,6,12,13]))    
# 
# find the values with the numbers on both are same
# def x(l):
#     pass

# print(x(['abc','aaa','xcx','121']))
# count=0

# for i in range(1,102):

#       count+=i
# print(count)
# print(sum(range(1,102)))

# l=[10,20,30,40,50]

# z=0
# for i in l:
#     z+=i
#     avg=z/(len(l))
# print(avg)

# def x(l):
#     c=0
#     for i in l:
#         if(len(l))>1 and i[0]==i[-1]:
#             c+=1
#     return c
# print(x(['101','112','nayan','sias','sser','212'])) 
# 
# def last(n):
#     return n[-1]
# def sort(tuples):
#     return sorted(tuples,key=last)
# print(sort([(2,1),(3,3),(1,2),(4,4)]))
# 
# l=[10,20,30,40,20,10,30]
# s=set(l)
# print(s)
# z=list(s)
# print(z)                  

# 1.List Comprehension
#l=[1,2,3,4]
# x=[i+2 for i in l]
# print(x)
#-----------------------------------   
# x=[i%2 for i in l]
# print(x)
#-----------------------------------
# x=[i==1 for i in l]
# print(x)
#----------------------------------
# list1=[i for i in range(len(l))if i%2==0]
# print(list1)


# 1>Answer:-
# def x(n):
#     return n*10

# print(x('thekiranacadmy'))   

# l=[0,1,2,3,4]
# l1=()
# for i in l:

# s='python'
# print(list(s))
# a=list(s)
# count=0

# l=[0,1,2,3,4] 
# x=len(l)
# print(x)
# l2=[]
# for i in l:
#     z=(l[i]-(x-1),l[i])
    
# l2.append(z)
# print(l2)

#out=[(0,4),(1,3)]
# n=int(input('enter the number:'))
# list1=[0,1,2,3,4,5,6,8,9,10,11,12]
# print(len(list1))
# list2=[]
# for i in range(len(list1)-1):
#     print(i,"*")
#     for j in range(i+1,len(list1)):
#         print(j,"-")
#         sum=list1[i]+list1[j]
#         if (sum==n):
#             o=(list1[i],list1[j])
#             list2.append(o)
# print(list2) 

def tup(l):
    l2=[]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            x=l[i]+l[j]
            if(x==4):
                z=(l[i],l[j])
                l2.append(z)
    print(l2)            
                
tup([0,1,2,3,4,5,6])   


def x(n):
    for i in n:
        n[0],n[-1]=n[-1],n[0]
    print(n)


x([1,2,3,4,5])        


































#l2=[(l[0],l[-1]),(l[1],l[-2])]


# l=[0,1,2,3,4]
# l2=[1,2,3,4,5]
# l3=zip(l,l2)
# print(l3)


# x,y,z,a,b=10,20,30,40,50
# # print(x,y,z,a,b)


# # km=1000 
# # d=3280.84   #1km=3280.84ft 
# # e=39370.1             
# # n=int(input('enter the number'))
# # meter=n/km
# # feet=d*n
# # inch=e*n
# # cm=n*100000



# #l=['e','a','i','u','o','a']
# # x=sorted(l)
# import math
# x=math.factorial(5)
# print(x)

# def fun(n):
#     if n==1:
#         return 1
#     else:
#         return n*fun(n-1)
# print(fun(5))  
# n=5
# x=1
# for i in range(n,0,-1):
#     x=x*i

# print(x)

    


    
# def prime():
#     n=int(input('enter number'))
#     y=int(input('enter number'))
#     if n>1:
#         for i in range(n,y):
#             if n%i ==0:
#                 print(n)
               
               
            
# prime()        
    









    