def extract(m, row, col):
  res = []
  for i in range(len(m)):
    if (i != row):
      r = m[i].copy()
      r.pop(col)
      res.append(r)
  return res

def calc_det(m):
  if len(m) != len(m[0]):
    raise Exception("Not a square matrix!")

  if len(m) == 3:
    from task6 import calc_det3x3
    return calc_det3x3(m)

  det = 0

  for i in range(len(m)):
    det += ((-1) ** (i + 2)) * m[0][i] * calc_det(extract(m, 0, i))

  return det

if __name__ == '__main__':
  m = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

  print("m: " + str(m))
  print("det: " + str(calc_det(m)))
