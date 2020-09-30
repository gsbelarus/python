data1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [1, 1, 1]
]

data2 = [
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
]

def get_column_vector(m, j):
  v = []
  for i in range(len(m)):
    v.append(m[i][j])
  return v

from task2 import scalar_product

def matrix_product(a, b):
  if len(a[0]) != len(b):
    raise Exception("Number of columns of matrix a doesn't match number of rows of matrix b")

  p = []

  for i in range(len(a)):
    l = []
    for j in range(len(b[0])):
      l.append(scalar_product(a[i], get_column_vector(b, j)))
    p.append(l)

  return p

if __name__ == '__main__':
  print("Data1: " + str(data1))
  print("Data2: " + str(data2))
  print("Matrix product: " + str(matrix_product(data1, data2)))