
#linear,sentinal and binary search

def l_search(p,n,list1):
    flag=1
    for i in range(n):
        if(list1[i]==p):
            print("Roll Number %d did attend the training program."%(p))
            flag=1;
            break
        else:
            flag=0

    if(flag==0):
        print("Roll Number %d did not attend the training program."%(p))

def s_search(p,n,list1):
    flag=1

    list1.append(p)
    i=0
    while(list1[i] != p):
        i+=1
        flag=1
    
    if(i==n):
        flag=0
            
    if(flag==1):
        print("Roll Number %d did attend the training program."%(p))
    else:
        print("Roll Number %d did not attend the training program."%(p))

            
def b_search(p,list1,h,l):
    
    mid=int((h+l)/2)

    if h>=l:
        if(p==list1[mid]):
            return mid
        elif(p<list1[mid]):
            return b_search(p,list1,mid-1,l)
        else:
            return b_search(p,list1,h,mid+1)
    else:
        return -1

def f_search(p,n,list1):
    f=0    
    a,b=0,1
    c=a+b
    while c<n:
        a=b
        b=c
        c=a+b
    offset=-1
    while c>1:
        i=min(offset+a, n-1)
        if list1[i]<p:
            c=b
            b=1
            a=c-b
            offset=i
        elif list1[i]>p:
            c=a
            b=b-a
            a=c-b
        else:
            print("element ",p," is found at index ", i)
            f=1
            break
    if f==0 and b!=0 and list1[offset+1]==p:
        print("element ",p," is found at index ", i)
        exit
    if f==0:
        print("element not found")
    
list1=[]
n=int(input("Enter the number of students who attended the program:"))
for i in range(n):
    m=int(input("Enter element no.%d :"%(i+1)))
    list1.append(m)
p=int(input("\nEnter the Roll no to search:"))


print("Menu:\n1.Linear Search\n2.Sentinal Search\n3.Binary Search\n4.Fibonacci Search\n5.Exit")
while(1):
    s=int(input("\nChoose your option:"))
    if(s==1):
        print("\nLinear Search:")
        l_search(p,n,list1)

    elif(s==2):
        print("\nSentinal Search:")
        list1.append(p)
        s_search(p,n,list1)

    elif(s==3):
        print("\nBinary Search:")
        l=0
        h=n-1
        x= b_search(p,list1,h,l)
        if x!=-1:
            print("Roll Number %d did attend the program and its index is %d."%(p,x))
        else:
            print("Elemnet not found")

    elif(s==4):
        print("\nFibonacci Search:")
        l=0
        f_search(p,n,list1)       

    elif(s==5):
        print("Exit")
        break

    else:
        print("Invalid option")
