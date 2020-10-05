def calc_derivative(f, x):
  delta = 0.000000000001
  return (f(x + delta) - f(x - delta)) / (2 * delta)

if __name__ == '__main__':

  def f(x):
    return x ** 2

  print("f: x ** 2")
  print("x = 0")
  print("Deriv: " + str(calc_derivative(f, 0)))
  print("x = 1")
  print("Deriv: " + str(calc_derivative(f, 1)))