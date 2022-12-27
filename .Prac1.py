"""In second year computer engineering class, group A students play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton."""



list1=["Aishwarya","Priya","Neha","Anjali"]          #cricket
list2=["Asmita","Pritam","Priya","Sanika"]         #badminton
list3=["priya","Sanika","Pritam","Shruti","Neha"]            #football
r1=[]
r2=[]
r3=[]
r4=[]

cricket=[]
n=int(input("How any students play cricket"))
for i in range (n):
     name=(input("Enter Student name"));
     cricket.append(name)

print(cricket)

#Printing
print("students who play Cricket")
print(list1)
print("\nstudents who play Badminton")
print(list2)
print("\nprint students who play football");
print(list3)

#List of students who play both cricket and badminton
def fun1():
     for i in list1:
         for j in list2:
             if(i==j):
                 r1.append(i)
     print("\nList of students who play both cricket and badminton")
     print(r1)
fun1()

#List of students who play either cricket or badminton but not both
def func2():
        
     for i in list1:   
         for j in list2:
             if(i==j):
                 break;
         if(i!=j):
             r2.append(i)
             
     for i in list2:    
         for j in list1:
             if(i==j):
                 break;
         if(i!=j):
             r2.append(i)
     print("\nList of students who play either cricket or badminton but not both")
     print(r2)
func2()

#Number of students who play neither cricket nor badminton
def func3():
    for  i in list3:
        r3.append(i)
        
    for i in r3:  
         for j in list1:
             if(i==j):
                 r3.remove(i)
             
    for i in r3: 
         for j in list2:
             if(i==j):
                 r3.remove(i)   
    print("\nNumber of students who play neither cricket nor badminton")
    print(r3)
func3()

#Number of students who play cricket and football but not badminton.
def func4():
    for i in list1:
        for j in list3:
            if(i==j):
                r4.append(i)
    for i in r4:
        for j in list2:
            if(i==j):
                r4.remove(i)
    print("\nNumber of students who play cricket and football but not badminton.")
    print(r4)
func4()   
