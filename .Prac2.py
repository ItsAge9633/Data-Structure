

#list1=['Aishwarya', 'Snehal', 'Priya', 'Neha']
#print("Given List is: "+str(list))

list=[]
n=int(input("How many words want to enter"))
for i in range (n):
      str=input("Enter a String")
      list.append(str)

print("Given List is: ", list)


def fun1():
    max_len=-1
    for i in list:
        if len(i)> max_len:
            max_len=len(i)
            maxString=i

    print("A word with logest length is", maxString)
fun1()

#to determinethe frequency of occurence of particular character in the string
def fun2():
    count=0
    str=input("Enter a String: ")
    char=input("Enter a character to determine a frequency of occurence in the string: ")
    for i in str:
        if i==char:
            count=count+1

    print("count of ", char ,"in a given string is", count)

fun2()

#To check whether given string is palindrome or not
def fun3():
     str=input("Enter a String: ")
     n=len(str)
     flag=0
     for i in range(0, int(n/2)):
         if str[i] != str[n-i-1]:
             flag=0
             break
         else:
            flag=1
     if(flag==0):
        print(str, " is not a palindrome")
     else:
        print(str, " is a palindrome")
fun3()

#to display index of first apperance of the substring
def fun4():
    
    str1=input("Enter a String: ")
    str2=input("Enter a substring: ")
    str1_len=len(str1)
    str2_len=len(str2)
    for i in range(str1_len - str2_len+1):
        if str1[i:i+str2_len] == str2:
            count=i
    print("To display index of first apperance of the substring", str2, " is", count)
fun4()

#to count the occurence of each word in given string
def fun4():
    #count=0
    str1=input("Enter a String: ")
    str2=input("Enter a word for count the ooccurence: ")
    str1_len=len(str1)
    str2_len=len(str2)
    for i in range(str1_len - str2_len+1):
        if str1[i:i+str2_len] == str2:
            count=count+1
    print("To display index of first apperance of the substring", str2, " is", count)
fun4()
