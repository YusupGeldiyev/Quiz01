#matVec takes a matrix and a vector and returns the corresponding matrix-vector multiply
def matVec(matrix,vector):
  '''
This function takes a matrix and a vector as its arguments. then it creates array and It then gets a new vector 
by multiplying given matrix and given vector. finally, it returns the result back to array after calculation
  ''' 
  result = []
  for i in range(len(matrix)):
    # runs for the raws of new vector
      total = 0    
      for j in range(len(vector)):
        #runs for the columns of new vector
        total += matrix[i][j] * vector[j]
  result.append(total)
  # the amount of columns in the matrix hast to be the amount as the raws in the vector
  return result

matrix1 = [[2,3],[4,5],[5,6]]
vector1 = [1,1]

matrix2 = [1,1]
vector2 = [[1,1], [1,2]]

matrix3 = 'test'
vector3 = 3

#print(matVec(matrix1,vector1))
#print(matVec(matrix2,vector2))
print(matVec(matrix3,vector3))
