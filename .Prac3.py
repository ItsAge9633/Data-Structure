"""Write a Python program to compute following computation on matrix:
a) Addition of two matrices, B) Subtraction of two matrices, c) Multiplication of
two matrices d) Transpose of a matrix"""

op=1
X = [[5,9,3],
    [8 ,2,6],
    [1 ,6,9]]

Y = [[3,8,5],
    [6,5,3],
    [2,5,3]]

result = [[0,0,0],
         [0,0,0],
        [0,0,0]]




print("First Matix:")
for r in X:
        print(r)
print("\nSecond Matrix:")
for r in Y:
        print(r)


#a)Add two matrices using nested loop

def addition():

   # iterate through rows
   for i in range(len(X)):
      # iterate through columns
      for j in range(len(X[0])):
         result[i][j] = X[i][j] + Y[i][j]

   print("\nAddition of Given Matrix:")
   for r in result:
      print(r)

# Sub of two matrices
def subtraction():
   
   # iterate through rows
   for i in range(len(X)):
      # iterate through columns
      for j in range(len(X[0])):
         result[i][j] = X[i][j] - Y[i][j]

   print("\nSubtraction of Given Matrix:")
   for r in result:
      print(r)


# Multiplication of two matrices using nested loop
def Multiplication():
    
   # iterate through rows
   for i in range(len(X)):
      # iterate through columns
      for j in range(len(X[0])):
          # iterate through rows of Y
          for k in range(len(Y)):
              result[i][j] += X[i][k] * Y[k][j]
         
   print("\nMultiplication of Given Matrix:")
   for r in result:
      print(r)
      
def transpose():
    #transpose of given First matrix
    print("\ntranspose of given First matrix")
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[j][i]= X[i][j]
            
    
    for r in result:
        print(r)             


while(op!=0):
    print("\nWhich operation You want to perfrom")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Transpose")
    choice=(int(input()))


    if(choice==1):
        addition()
            
    elif(choice==2):
        subtraction()
                    
    elif(choice==3):
        Multiplication()

    elif(choice==4):
        transpose()

    else:
        print("Invalid choice");
        
                    



