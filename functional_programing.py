''''
#primenumber:
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print('number is not prime')
#                 break
#             else :
#                 print('number is prime')
#                 break
# prime(8)     
# #by using the function ,write functional programing on the prime  number
# lower = 900
# upper = 1000

# print("Prime numbers between", lower, "and", upper, "are:")
# def x(lower,upper):
#     for num in range(lower, upper + 1):
   
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                    break
#                 else:
#                    print(num)
#                    break
# x(1,15)


# #reverse number

# def x(n):
#     print(n)
#     s=0
#     while n!=0:
#         d=n%10
#         s=s*10+d
#         n//=10
#     print('reverse',s)

# x(12456)        
# '''
# #reverse the string
# # def x(n):
# #     a=n.split()
# #     l=[]
# #     for i in a:
# #         l.append(i[: :-1])
# #         e=' '.join(l)
# #     print(e)
# # x('i love python ,python is good')  
             

# #reverse the string
# def x(n):
    
#     print('the value is ',n)
#     a=" "
#     for i in n:
#         a=i+a 
#         return a
    
        
# x('I love my baby who is naughty')

# # #reverse list with function
# # l=[1,2,3,4,5,7]
# # l1=[]
# # for i in l:
# #     l1.insert(0,i)
# # print(l1)

    
# # #calculate the string the in dict
# # s='i love aboli ,where pune is strong'
# # x=s.split()
# # print(x)
# # for i in x:
# #     x.insert(7,'beautiful')
# #     #x[0]=x[-1]
# # print(x)
# # print(" ".join(x))


# x=' i am aboli'
# s=x.split()
# w=s
# s[2]='pranit'
# print(w)

#     # #reverse list by using functional programing
            
#     # def x(n):
#     #     s=0
#     #     r=len(n)-1
#     #     for i in n:
#     #         while(s<r):
#     #            temp=n[s]
#     #            n[s]=n[r]
#     #            n[r]=temp
#     #            s+=1
#     #            r-=1
#     #     return n        
                    
#     # print(x([1,2,3,4,5,6,7,8]) ) 
# # reverse string using function          
# s='i am aboli i love  icecream'
# a=s.split() 
# print(a)             
# def x(n):
#     l=[]
   
#     for i in n:
#         l.insert(0,i)
#         u=' '.join(l)
#     print(u)
# x(a)  
        

# def x(n):
#     first=0
#     second=1
#     for i in range(n):
#         print(first,end=' ')
#         temp=first
#         first=second
#         second=temp+first
     
   
#x(10) 

# #fnd the perfect nuber in range

# def x(a,b):
#     for n in range(a,b):
#         s=0
#         for i in range(1,n):
#             if (n%i==0):
#                 s=s+i
#         if n==s:
#             print(n)
                
         
# x(1,500)           
# #find the prime number in range of ...
# def x(a,b):
#     for n in range(a,b+1):
#         if n>1:
#             for i in range(2,n):
#                 if n%i==0:
                    
#                     break
#                 else:
#                     print(n)
#                     break
# x(1,1000)                    

# lower = 900
# upper = 1000

# print("Prime numbers between", lower, "and", upper, "are:")
# def x(lower,upper):
#     for num in range(lower, upper + 1):
   
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                    print(num)
#                    break
#                 else:
#                    print(num)
#                    break
# x(900,1000)

# s='aboli vijay mohitkar'
# e=s.split()
# def x(n): 
#     l=[]
#     for i in range(1,len(n)):
#         if n[i]==3:
#            l.append(i)
#     print(l)

# x([1,2,3,4,3,3,6])

# #unicodes in python

# unicode_1 = ("\u0124", "\u2665", "\U0001f638", "\u265E", "\u265F", "\u2168") 
# print(unicode_1)
#cnsider dict keys and values list and tuple
# l = ['a', 'ab', 'abc']
# t = (10, 100, 1000)
# d={}
# for i in range(len(l)):
#     d[l[i]]=t[i]
# print(d)  
# c=100
# def x(c):
#     c=c-1
#     if c<0:
#         return 1
#     print('hello word')   
#     x(c)

# x(c)


def x(c):
        return(c *100)
        
print(x("hello world"))    