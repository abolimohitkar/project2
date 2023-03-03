#1> calculate the length of string:
# def x(str):
#     count=0
#     for char in str:
#         count +=1
#     return  count
# print(x('mamma i love you'))  

#2>WAP for calculate number of elements in string
# s=input('enter the string:')
# x=s
# #z=x.split()
# d={}
# count=0
# for i in x:
#     if i in d:
#      d[i]+=1

#     else:
#         d[i]=1
# print(d)

#if having the string  values should be return as per the question
# def x(str):
#     if len(str)<2:
#         return " "
#     return str[0:2]+str[-2:]

# print(x('w3resource')) 
# print(x('w3'))
# print(x('w'))

#value should be resta$t
# def x(l):
#     c=l[0]
#     l=l.replace(c,"$")
#     l=c+l[1:]
#     return l
# print(x('restart'))
       
# def x(a,b):
#     w=b[:2]+a[2:]
#     q=a[:2]+b[2:]

#     return w + ' '+ q    
# print(x('abc','xyz'))  
# def x(s):
#     length=len(s)
#     if length>2:
#         if s[-3:]=='ing':
#             s+='ly'
#         else:
#             s+='ing' 
#     return s    
# print(x('abc'))
# print(x('string'))

# import requests
# x=requests.get("https://google.com")
# print(x) 

#strip () inbuild function to remove white space in function#

x='  aboli'
print(x)
print(x.strip())

#or leading whitespace character we can use the lstrip() function

x='    aboli vijay mohitkar'
print(x)
print(x.lstrip())

#join() is function which concanated the string
# str='rohan'
# str1='ab'
# stra=str.join(str1)
# print(stra)

# #by using random module we can shuffle elements in the string and list

# import random
# z=['a','c','b','x','z','y']
# random.shuffle(z)
# print(z)


x=123
print(len(str(x)))
d=x//10
print(d)


#def x(a,b):

#x(100,499)    

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")
def x(lower,upper):
    for num in range(lower, upper + 1):
   
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                   break
                else:
                   print(num)
                   break
x(1,15)

    

