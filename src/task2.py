data1 = [1, 2, 3, 4]
data2 = [0, 0, 0, 1]

def scalar_product(v1, v2):
  l = len(v1)

  if len(v2) != l:
    raise Exception("Vectors should be of equal length")

  p = 0

  for i in range(l):
    p += v1[i] * v2[i]

  return p

if __name__ == '__main__':
  print("Data1: " + str(data1))
  print("Data2: " + str(data2))
  print("Dot product: " + str(scalar_product(data1, data2)))