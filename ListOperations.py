#List Operations
# import sys
num=[]
while True:
    print("""
        -----------List Operatons-----------
        Press 1 for inseting element in list
        Press 2 for updating element in list
        Press 3 for deleting element from list
        Press 4 for searching element in list
        Press 5 for printing list
        Press 6 for sorting list
        Press 7 to find maximum element from list
        Press 8 to find minimum element from list
        Press 9 to find sum of list elements
        Press 10 to exit
        ------------------------------------
          """)
    choice=int(input("Enter from options(1 to 9): "))
    
    if choice==1:
        print("""
            Press 1 for insert element at the end of list
            Press 2 for insert element at particular index
            Press 3 for inserting elements in range             
              """)
        inchoice=int(input("Enter from above choice(1 or 2): "))
        
        if inchoice==1:
            ele=int(input("Enter element to insert(Integer type): "))
            num.append(ele)
            print(ele,"inserted successfully at",num.index(ele))
        elif inchoice==2:
            ele=int(input("Enter element to insert(Integer type): "))
            index=int(input("Enter index at which you want to insert element(Integer type): "))
            num.insert(index,ele)
            print(ele,"inserted successfully at",num.index(ele))
        elif inchoice==3:
            n=int(input("Enter numbers of elements that you want to insert: "))
            for i in range(n):
                num.append(int(input(f"Number {i+1}: ")))
        else:
            print("Valid options are only 1 or 2")
            
    elif choice==2:
        idx=int(input("Enter index of element that you want to update(Integer Type): "))
        if len(num)!=0:            
            if idx>=0 and idx<len(num):
                ele=int(input("Enter element that you want to update(Integer Type): "))
                num[idx]=ele
                print(ele,"at index",num.index(ele),"has been updated successfully")
            else:
                print("Invalid Index")
        else:
            print("List is empty")
            
    elif choice==3:
        print("""
              Press 1 for deleting element by index 
              Press 2 for deleting element by value
              Press 3 for deleting elements in range
              """)
        inchoice=int(input("Enter from above choice(1 or 2 or 3): "))
        
        if inchoice==1:
            index=int(input("Enter index at which you want to delete element(Integer type): "))
            if len(num)>0:
                if index>=0 and index<=len(num):
                    print(num.pop(index),"is deleted from index",index)
                else:
                    print("Invalid index")
            else:
                print("List is empty")
        elif inchoice==2:
            del_ele=int(input("Enter element to delete(Integer type): "))
            if del_ele in num:
                idx=num.index(del_ele)
                num.remove(del_ele)                
                print(del_ele,"removed from list from index",idx)
            else:
                print("Element don't lies in the list")
        elif inchoice==3:
            lower_limit=int(input("Enter Lower Limit in list(Integer type): "))
            uppper_limit=int(input("Enter Upper Limit in list(Integer type): "))
            if lower_limit>=0 and uppper_limit<=len(num):
                del num [lower_limit:uppper_limit]
                print(f"Elements from {lower_limit} to {uppper_limit} has been removed from list")
            else:
                print("Enter valid range")
        else:
            print("Valid options are 1 or 2 or 3")
    
    elif choice==4:
        print("""
              Press 1 for searching element using value and to find index
              Press 2 for searching element using index and to find value              
              """)
        inchoice=int(input("Enter from above choice(1 or 2): "))
        
        if inchoice==1:
            ele=int(input("Enter element to search(Integer type): "))
            if ele in num:
                print(ele,"found in list at index",index(ele))
            else:
                print("Element don't lies in the list")
        elif inchoice==2:
            idx=int(input("Enter index of element to search(Integer type): "))
            if idx>=0 and idx<=len(num):
                if len(num)==0:
                    print("List is empty")
                else:
                    print(f"Element {num[idx]} found at index {idx}")
            else:
                print("Invalid index")
        else:
            print("Valid options are 1 or 2")
    
    elif choice==5:
        if len(num)!=0:
            print("List is: \n---------")
            for x in num:
                print(x)            
            else:print("---------")
        else:
            print("List is empty")
    
    elif choice==6:
        print("""
              Press 1 for sorting list in ascending order
              Press 2 for sorting list in descending order
              """)
        inchoice=int(input("Enter from above options(1 or 2): "))
        
        if inchoice==1:
            if len(num)!=0:
                num=sorted(num)
                print("List is successfully sorted in ascending order")
            else:
                print("List is empty")
        elif inchoice==2:
            if len(num)!=0:
                num=sorted(num,reverse=True)
                print("List is successfully sorted in descending order")
            else:
                print("List is empty")
        else:
            print("Valid options are 1 or 2")
    
    elif choice==7:
        if len(num)!=0:print("Maximum element in list is:",max(num))
        else:print("List is empty")
        
    elif choice==8:
        if len(num)!=0:print("Maximum element in list is:",min(num))
        else:print("List is empty")
    
    elif choice==9:
        if len(num)!=0:print("Sum of element in list is:",sum(num))
        else:print("List is empty")
    
    elif choice==10:
        break
        # sys.exit()
        
    else:
        print("Valid options are from 1 to 9")