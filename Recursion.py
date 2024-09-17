#Recursion
#Print n to 1
# def show(n):
#     if (n==0): return
#     print(n)
#     show(n-1)

#Print 1 to n
# def show(n):
#     if(n==0):return
#     show(n-1)
#     print(n)
# show(5)

# Factorial of given number using recursion
# def fact(n):
#     if(n==1):return 1
#     return n*fact(n-1)
# ans=fact(8)
# print("Factorial of given number is:",ans)

# def fact_num(n):
#     if(n==0 or n==1): return 1
#     return fact_num(n-1) * n
# print(fact_num(8))

#Multiplication table using recusrion
#Forward
# def mult_tb(n,i=1):
#     if(i==11):return
#     print(f"{n} x {i} = {n*i}")
#     mult_tb(n,i+1)
# mult_tb(109)

#Backward
# def mult_tb(n,i=10):
#     if(i==0):return    
#     mult_tb(n,i-1)
#     print(f"{n} x {i} = {n*i}")
# mult_tb(109)

#Pattern Try
# def pattern_1(n,i,j):
#     if(i==n and j==n+1):return
#     elif(j==i+1):
#         print()
#         pattern_1(n,i+1,j=1)
#     else:
#         print(j,end='')
#         pattern_1(n,i,j+1)
# pattern_1(5,1,1)

#Sum of Number 1 to n
# def sum_of_num(n,sum=0):
#     if(n==0): return sum
#     sum+=n
#     return sum_of_num(n-1,sum)
# print(sum_of_num(5))

#Count Number of Digits
# def count_digits(n,count=0):
#     if(n==0): return count    
#     n//=10
#     count+=1
#     return count_digits(n,count)
# print(count_digits(10826348721367))

#Sum of Digits
# def sum_of_digits(n,sum=0):
#     if(n==0): return sum
#     sum+=n%10
#     n//=10
#     return sum_of_digits(n,sum)
# print(sum_of_digits(1725437632))

#Product of Digits
# def product_of_digits(n,mul=1):
#     if (n==0): return mul
#     mul*=n%10
#     n//=10
#     return product_of_digits(n,mul)
# print(product_of_digits(1467))

#Reverse of Number
# def reverse_of_number(n,rev=0):
#     if(n==0): 
#         # print("Reverse of Number is:",rev)
#         return rev
#     rev=rev*10+n%10
#     n//=10
#     return reverse_of_number(n,rev)
# print(reverse_of_number(123))

# def reverse_of_number(n,rev=0):
#     if(n==0): 
#         print("Reverse of Number is:",rev)
#         return
#     rev=rev*10+n%10
#     n//=10
#     reverse_of_number(n,rev)
# reverse_of_number(12345)

#Power of Number
# def power_of_num(base,exp,ans=1):
#     if (exp==0): return ans
#     ans*=base
#     return power_of_num(base,exp-1,ans)
# print(power_of_num(2,3))

#Print HCF of two numbers
# def hcf(n1,n2,i=1,ans=0):
#     if (i>n1 or i>n2):return ans
#     if(n1%i==0 and n2%i==0):ans=i
#     return hcf(n1,n2,i+1,ans)
# print(hcf(19,38))

#Print LCM of two numbers
# def lcm(n1,n2,i=1,ans=0):
#     if (i>n1 or i>n2):
#         ans=(n1*n2)//ans
#         return ans
#     if(n1%i==0 and n2%i==0):ans=i
#     return lcm(n1,n2,i+1,ans)
# print(lcm(24,36))

#Fibonacci Series upto n
# def fibonacci_series(n,i=1,a=0,b=1,sum=0):
#     if(i==n+1):return
#     print(a)
#     sum=a+b
#     a=b
#     b=sum    
#     fibonacci_series(n,i+1,a,b,sum)
# print("Fibonacci Series is:")
# fibonacci_series(10)

# def fibonacci_series_print(n,i=1,a=0,b=1,sum=0,ans=[]):
#     if(i==n+1):
#         print(f"Fibonacci Series upto {n} is:")
#         for x in ans: print(x)
#         return
#     ans.append(a)
#     sum=a+b
#     a=b
#     b=sum    
#     fibonacci_series_print(n,i+1,a,b,sum,ans)
# fibonacci_series_print(8)

#Converting Decimal to Binary
# def convert_decimal_binary(n,bin=[]):
#     if (n==0):
#         ans=0
#         for x in bin: ans=ans*10+x
#         return ans
#     bin.append(n%2)
#     n//=2
#     return convert_decimal_binary(n,bin)
# print(convert_decimal_binary(10))

# def decimal_to_binary(n,bin=0):
#     if (n==0):return bin
#     return (bin+n%2+decimal_to_binary(n//2,bin)*10)
# print(decimal_to_binary(19))

#Printing List Elements
# def print_list(list,idx=0):
#     if (idx==len(list)):return
#     print(list[idx],end=" ")
#     print_list(list,idx+1)
# print_list([1,2,3,4,5,6,7,8,9,0])

#Sum of num 1 to n
# def sum_of_num(n):
#     if(n==1): 
#         print(n,end='=')
#         return 1
#     print(n,end="+")
#     return sum_of_num(n-1)+n
# print(sum_of_num(5))

# n=5
# sum=0
# for i in range(1,n):
#     print(i,end=' + ')
#     sum+=i
# else:
#     print(n,'=',sum+n)
