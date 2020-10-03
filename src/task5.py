def factorial(n):
  res = 1
  for x in range(2, n + 1):
    res *= x
  return res

def calc_c(k, n):
  return factorial(n) / (factorial(k) * factorial(n - k))

def calc_prob(n, m, s):
  ''' n -- overall attempts, m -- attempts satisfying the condition, s -- number for the condition "not less than s" '''
  p = (6 - s + 1) / 6
  return calc_c(m, n) * (p ** m) * ( (1 - p) ** (n - m) )

if __name__ == '__main__':
  print("N, M, S: 5, 1, 4")
  print("Probability: " + str(calc_prob(5, 1, 4)))