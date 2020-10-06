def calc_eucl_dist(v1, v2):
  import math
  s = 0
  for i in range(len(v1)):
    s += (v1[i] - v2[i]) ** 2
  return math.sqrt(s)

if __name__ == '__main__':
  v1 = [1, 0, 0]
  v2 = [0, 1, 0]

  print("v1: " + str(v1))
  print("v2: " + str(v2))
  print("Dist: " + str(calc_eucl_dist(v1, v2)))