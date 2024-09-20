#(1.)Taking list elements as input(Integer type)
# n=int(input("Enter numbers of elements that you want to enter: "))
# ls=[]
# for i in range(n):
#     ls.append(int(input(f"Enter element no. {(i+1)}: ")))
# # print(ls)
# print("List elements are: ")
# for i in range(len(ls)):print(ls[i])

#(2.)Print all negative elements of List
# ls=[100,-90,89,-56,76,-82,23,43,-12]
# print("Negative elements of list are: ")
# for i in range(len(ls)):
#     if(ls[i]<0):print(ls[i])

#(3.)Print all positive elements of List
# ls=[100,-90,89,-56,76,-82,23,43,-12]
# print("Positive elements of list are: ")
# for i in range(len(ls)):
#     if(ls[i]>0):print(ls[i])

#(4.)Differentiate Positive, Negative and Zero elements in different lists and also count no. of diffrenet elements
# ls=[90,-89,34,23,-45,-1,0,-20,64,-76,-32,-21,0,234,-99]
# pos=[]
# neg=[]
# zero=[]
# i=0
# while i<len(ls):
#     if (ls[i]>0):pos.append(ls[i])
#     elif(ls[i]==0):zero.append(ls[i])
#     else:neg.append(ls[i])
#     i+=1
# print("Total Positive Numbers are:",len(pos),"\nElements are:",pos)
# print("Total Zero Numbers are:",len(zero),"\nElements are:",zero)
# print("Total Negetive Numbers are:",len(neg),"\nElements are:",neg)

#(5.)Sum,minimum and maximum numbers from List
# ls=[90,-89,34,23,-45,-1,0,-20,64,-76,-32,-21,0,234,-99]
# #Without using built-in functions 
# max_val,min_val,sum_val=ls[0],ls[0],0
# for ele in ls:
#     if ele>max_val : max_val=ele
#     elif ele<min_val : min_val=ele
#     sum_val+=ele
# print("Maximum element is: {0}\nMinimum element is: {1}\nSum of all elements is: {2}".format(max_val,min_val,sum_val))

# #With Using built-in functions
# print("Maximum element is: {0}\nMinimum element is: {1}\nSum of all elements is: {2}".format(max(ls),min(ls),sum(ls)))

#(6.)Sorting list elements in ascending order
# ls=[90,-89,34,23,-45,-1,0,-20,64,-76,-32,-21,0,234,-99]
# #Without using built-in functions(Bubble sort)
# def swap_values(a,b):
#     return b,a

# def print_list(ls,name='List'):
#     if len(ls)!=0:
#         print(name,"is: ")
#         for i in range(len(ls)):
#             print(ls[i])
#     else:
#         print(name,"is empty")
        
# for i in range(len(ls)):
#     for j in range(i+1):
#         if ls[i]<ls[j]:
#             ls[i],ls[j]=swap_values(ls[i],ls[j])
            
# print_list(ls,'After sorting in ascending order List')

# #(7.) Sorting list elements in descending order
# for i in range(len(ls)):
#     for j in range(i+1):
#         if ls[i]>ls[j]:
#             ls[i],ls[j]=swap_values(ls[i],ls[j])
            
# print_list(ls,'After sorting in descending order List')

#(8.) Finding second largest element of list
# for i in range(len(ls)):
#     for j in range(i+1):
#         if ls[i]<ls[j]:
#             ls[i],ls[j]=swap_values(ls[i],ls[j])
# print("Second largest element in list is:",ls[(len(ls)-2)])

#(9.) Sorting List elements with using .sort() function
# ls=[90,-89,34,23,-45,-1,0,-20,64,-76,-32,-21,0,234,-99]
# #List in ascending order
# ls.sort()
# print(ls)
# ls=sorted(ls)
# print(ls)
# #List in descending order
# ls.sort(reverse=True)
# print(ls)
# ls=sorted(ls,reverse=True)
# print(ls)

#(10.) Finding second largest element in list using built-in function
# ls=[90,-89,34,23,-45,-1,0,-20,64,-76,-32,-21,0,234,-99]
# ls.sort(reverse=True)
# print("Second largest list element is:",ls[1])

#(11.)Find odd and even elements, also count no. of elements and their sum
# ls=[i for i in range(1,11)]
# print(type(ls))
# sum_even,sum_odd,count_even,count_odd=0,0,0,0
# for x in ls:
#     if x%2==0:
#         count_even+=1
#         sum_even+=x
#     else:
#         count_odd+=1
#         sum_odd+=x
# print("No. of odd elements are",count_odd,"And their sum is:",sum_odd)
# print("No. of even elements are",count_even,"And their sum is:",sum_even)

#Two Dimentional List
# (12.)Sum of Two Dimetional Lists
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[[1,2,3],[4,5,6],[7,8,9]]
# a=eval(input("Enter the First List: "))
# b=eval(input("Enter the Second List: "))

# if len(a)==len(b) and len(a[0])==len(b[0]):
#     c=[]
#     #Sum of Elements
#     for i in range(len(a)):
#         row=[]
#         for j in range(len(a[i])):
#             row.append(a[i][j]+b[i][j])
#         c.append(row)
#     #Printing Final List
#     print("Final list after summation is: ")
#     for i in range(len(c)):
#         for j in range(len(c[i])):
#             print(c[i][j],end=' ')
#         print()
# else:
#     print("Invalid Input")
    
#(13.)Subtraction of two dimentional lists
# a=eval(input("Enter the First List: "))
# b=eval(input("Enter the Secondt List: "))

# if len(a)==len(b) and len(a[0])==len(b[0]):
#     c=[]
#     #Sum of Elements
#     for i in range(len(a)):
#         row=[]
#         for j in range(len(a[i])):
#             row.append(a[i][j]-b[i][j])
#         c.append(row)
#     #Printing Final List
#     print("Final list after summation is: ")
#     for i in range(len(c)):
#         for j in range(len(c[i])):
#             print(c[i][j],end=' ')
#         print()
# else:
#     print("Invalid Input")
    
#(14.)Multiplication of Lists
def input_2D_list(name='List'):
    print("Enter for",name,": ")
    row=int(input("Enter Numbers of Rows: "))
    col=int(input("Enter Numbers of Columns: "))
    ls=[]
    print("Enter {0} elements for {1}: ".format((row*col),name))
    for i in range(row):
        row=[]
        for j in range(col):
            row.append(int(input(f"Enter ls[{i}][{j}]: ")))
        ls.append(row)
    return ls

def print_2D_list(ls,name='List'):
    print(name,"is: ")
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            print(ls[i][j],end=' ')
        print()

def multiply_2D_lists(a,b):
    c=[]
    if len(a[0])==len(b):
        mul=[]
        row=len(a)
        col=len(b[0])
        for i in range(row):
            row=[]
            for j in range(col):
                x=0
                for k in range(len(a[0])):
                   x+=a[i][k]+b[k][j]
                row.append(x)
            mul.append(row)
        return mul 
    else:
        print("Invalid List input")
        
# a=input_2D_list("List a")
# print_2D_list(a,"List a")
# b=input_2D_list("List b")
# print_2D_list(b,"List b")
# c=multiply_2D_lists(a,b)
# print_2D_list(c,"Final List")

#(15.)Finding Maximum and minimum elements from 2D Lists
# a=input_2D_list('List a')
# print_2D_list(a,'List a')
# max=a[0][0]
# min=a[0][0]

# for i in range(len(a)):
#     for j in range(len(a[0])):
#         if a[i][j]>max:max=a[i][j]
#         elif a[i][j]<min:min=a[i][j]
# print("Maximum element is:",max)
# print("Minimum element is:",min)

#(16.)Transpose of matrix
# a=input_2D_list('List a')
# b=[]
# for i in range(len(a[0])):
#     row=[]
#     for j in range(len(a)):
#         row.append(a[j][i])
#     b.append(row)
# print_2D_list(a,"Original List")
# print_2D_list(b,"Transposed List")

#(16.)Transpose of Matrix-Another Method
# a=input_2D_list("List a")
# b=[]
# for i in range(len(a[0])):
#     row=[]
#     for j in range(len(a)):
#         row.append(0)
#     b.append(row)

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         b[j][i]=a[i][j]
# print_2D_list(a,"List a")
# print_2D_list(b,"Transposed - List b")

#(17.)Cont Positive, Negative and Zeros
# countpos,countneg,countzero=0,0,0
# a=input_2D_list('List a')
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if (a[i][j]>0):countpos+=1
#         elif (a[i][j]<0):countneg+=1
#         else:countzero+=1
# print("Total no. positive numbers:",countpos)
# print("Total no. negetive numbers:",countneg)
# print("Total no. zero numbers:",countzero)

#(18.)Upper triangular matrix and sum of those elements
a=input_2D_list('List a')
sum=0
print("Upper triangular matrix: ")
for i in range(len(a)):
    for k in range(0,i):
        print(end='  ')
    for j in range(i,len(a[i])):
        print(a[i][j],end=' ')
        sum+=a[i][j]
    print()
print("Sum of elements of upper triangular matrix is:",sum)
#(19.)Lower triangular matrix and sum of those elements
sum=0
print("Lower triangular matrix: ")
for i in range(len(a)):
    for j in range(0,i+1):
        print(a[i][j],end=' ')
        sum+=a[i][j]
    print()
print("Sum of elements of lower triangular matrix is:",sum)