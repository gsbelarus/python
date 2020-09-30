# array of [value, probability] pairs
data = [[1, 0.2], [2, 0.4], [3, 0.3], [4, 0.1]]

def calc_expect(d):
  expectation = 0
  for x in d:
    expectation += x[0] * x[1]
  return expectation

def calc_disp(d):
  expectation = calc_expect(d)
  dispersion = 0
  for x in d:
    dispersion += ((x[0] - expectation) ** 2) * x[1]
  return dispersion

if __name__ == '__main__':
  print("Data: " + str(data))
  print("Expectation: " + str(calc_expect(data)))
  print("Dispersion: " + str(calc_disp(data)))
