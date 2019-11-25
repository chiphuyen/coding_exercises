'''
Question Statement
Rotate a n*n matrix by 90 degrees without using extra space

'''
N = 4
  
def rotateMatrix(matrix): 
      
    for i in range(0, int(N/2)): 

        for j in range(i, N-i-1): 

            tmp = matrix[i][j] 

            matrix[i][j] = matrix[j][N-1-i] 
  
            matrix[j][N-1-i] = matrix[N-1-i][N-1-j] 
  
            matrix[N-1-i][N-1-j] = matrix[N-1-j][i] 
  
            matrix[N-1-j][i] = tmp 
  
  
def displayMatrix( matrix ): 
      
    for i in range(0, N): 
          
        for j in range(0, N): 
              
            print (matrix[i][j]) 
        print ("")
      
      
  
matrix = [[0 for i in range(N)] for j in range(N)] 
matrix = [ [0, 1, 2, 3 ], 
        [00, 11, 22, 33 ], 
        [44, 55, 66, 77 ], 
        [88, 99, 110, 120 ] ] 
rotateMatrix(matrix) 
  
displayMatrix(matrix) 