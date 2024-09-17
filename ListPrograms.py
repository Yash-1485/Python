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