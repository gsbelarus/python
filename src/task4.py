data = [2, 3, 4]

def calc_len(d):
  import math
  t = 0
  for x in d:
    t += x ** 2
  return math.sqrt(t)

if __name__ == '__main__':
  print("Data: " + str(data))
  print("Len: " + str(calc_len(data)))