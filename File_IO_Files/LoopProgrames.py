import math
# Print ASCII values with characters

# for i in range (65,90+1):
#     print(chr(i),"-",i)

# Power of a Number using Loop
# base = int(input("Enter a Number: "))
# exp = int(input("Enter Exponent: "))
# pow=1
# for i in range (1,exp+1):
#     pow*=base
# print(base,"raised to",exp,"is:",pow)

# Prime Number
# n=int(input("Enter a Number: "))

# i=2
# flag=True
# if (n<=1): print("Not Prime Number")
# else:
#     while i<n :
#         if n%i==0:
#             flag=False
#             break
#         i+=1
    
#     if flag==True: print("Prime Number")
#     else: print("Not Prime Number")

# Prime Numbers 1 to n
# num=int(input("Enter a Number: "))
# print("Prime Number List from 1 to",num)
# for j in range (1,num+1):
#     i=2
#     n=j
#     flag=True
#     if (n<=1): continue
#     else:
#         while i<n :
#             if n%i==0:
#                 flag=False
#                 break
#             i+=1

#         if flag==True: print(j)

#Sum of Prime Number from 1 to n
# num=int(input("Enter a Number: "))
# print("Prime Number List from 1 to",num)
# sum=0
# for j in range (1,num+1):
#     i=2
#     n=j
#     flag=True
#     if (n<=1): continue
#     else:
#         while i<n :
#             if n%i==0:
#                 flag=False
#                 break
#             i+=1

#         if flag==True: sum+=j
# print("Sum of Prime Number from 1 to",num,"is:",sum)

# Armstrong Number
# n=int(input("Enter a Number: "))
# temp=n
# temp1=n
# ans=0
# count=0

# while temp1>0 :
#     count+=1
#     temp1//=10

# while temp>0 :
#     ans+=int(math.pow(temp%10,count))
#     temp//=10
      
# if ans==n : print("Armstrong Number")
# else: print("Not Armstrong Number")

# Armstrong Number from 1 to n
# num=int(input("Enter a Number: "))
# print("Armstrong Numbers From 1 to",num)
# for j in range (1,num+1):
#     temp=j
#     temp1=j
#     ans=0
#     count=0
    
#     while temp1>0 :
#         count+=1
#         temp1//=10
    
#     while temp>0 :
#         ans+=int(math.pow(temp%10,count))
#         temp//=10
          
#     if ans==j : print(j)

# Disarium Number
# n=int(input("Enter a Number: "))

# temp=n
# temp1=n
# ans=0
# count=0
# while temp1>0 :
#     count+=1
#     temp1//=10

# while temp>0 :    
#     ans+=int(math.pow(temp%10,count))
#     temp//=10
#     count-=1
    
# if ans==n : print("Disarium Number")
# else: print("Not Disarium Number")

# Disarium Number 1 to n
# num=int(input("Enter a Number: "))
# print("Disarium Numbers from 1 to",num)
# for j in range (1,num+1):
#     temp=j
#     temp1=j
#     ans=0
#     count=0
#     while temp1>0 :
#         count+=1
#         temp1//=10

#     while temp>0 :    
#         ans+=int(math.pow(temp%10,count))
#         temp//=10
#         count-=1

#     if ans==j : print(j)

# Perfect Number
# n=int(input("Enter a Number: "))
# sum=0
# mul=1
# while n>0 :
#     rem=n%10
#     sum+=rem
#     mul*=rem
#     n//=10

# if sum==mul : print("Perfect Number")
# else: print("Not Perfect Number")

# Perfect Number from 1 to n
# num=int(input("Enter a Number: "))
# print("Prefect Number from 1 to",num)
# for j in range (1,num+1):
#     n=j
#     sum=0
#     mul=1
#     while n>0 :
#         rem=n%10
#         sum+=rem
#         mul*=rem
#         n//=10        
#     if sum==mul : print(j)

# Convert Decimal to Binary
# n=int(input("Enter a Number: "))
# temp=n
# bin=""
# rev=""

# while temp>0 :
#     rev+=format(temp%2)
#     temp//=2
# for i in range((len(rev)-1),-1,-1):
#     bin+=rev[i]
# binInt=int(bin)
# print("Binary number of",n,"is:",binInt)

# Convert Binary to Decimal
# n=int(input("Enter a Binary Number: "))
# flag=True
# temp=n

# while temp>0 :
#     rem=temp%10
#     if rem<0 or rem>2 : 
#         flag=False 
#         print("Enter Valid Input")
#         break
#     temp//=10

# if flag==True :
#     dec=0
#     i=0
#     while n>0:
#         dec+=((n%10)*int(math.pow(2,i)))
#         i+=1
#         n//=10
#     print("Decimal Number is:",dec)