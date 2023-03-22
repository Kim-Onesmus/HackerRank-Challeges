x = int(input('Enter the value of X '))
y = int(input('Enter the value of Y '))
z = int(input('Enter the value of Z '))
n = int(input('Enter the value of N '))

coordinates = [[i, j, k] 
               for i in range(x+1) 
               for j in range(y+1) 
               for k in range(z+1) 
               if i+j+k != n]


print(coordinates)