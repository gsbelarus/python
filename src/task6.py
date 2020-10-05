def calc_det2x2(m):
  return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def calc_det3x3(m):
  return m[0][0] * calc_det2x2([[m[1][1], m[1][2]], [m[2][1], m[2][2]]]) \
    - m[0][1] * calc_det2x2([[m[1][0], m[1][2]], [m[2][0], m[2][2]]]) \
    + m[0][2] * calc_det2x2([[m[1][0], m[1][1]], [m[2][0], m[2][1]]])

if __name__ == '__main__':
  m = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
  print("matrix: " + str(m))
  print("Det: " + str(calc_det3x3(m)))