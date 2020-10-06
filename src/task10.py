def find_min(f, a, b, p):
  import sys
  min = sys.float_info.max
  x = a
  while x <= b:
    v = f(x)
    if v < min:
      min = v
    x += p
  return min

if __name__ == '__main__':
  def func(x):
    return 3 * (x ** 3) + 4 * (x ** 2) + 5 * x + 21

  print("min: " + str(find_min(func, -1000000, 1000000, 0.1)))