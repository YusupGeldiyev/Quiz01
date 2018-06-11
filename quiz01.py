#matVec takes a matrix and a vector and returns the corresponding matrix-vector multiply
def matVec(matrix,vector):
  '''
This function takes a matrix and a vector as its arguments. It then gets a new vector 
before retruning the now updated vector.
  ''' 
  result = []
  for i in range(len(matrix)):
      total = 0    
      for j in range(len(vector)):
        total += matrix[i][j] * vector[j]
  result.append(total)
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
