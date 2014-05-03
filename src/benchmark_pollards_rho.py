import random 

def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

def square_minus_one(x,n):
  return (x*x-1)%n

def square_plus_one(x,n):
  return (x*x+1)%n

def power_3_minus_one(x,n):
  return (x*x*x-1)%n

def random_(x,n):
  return random.randint(0,n)

def rho(n, f):
  x = 2
  y = 2
  d = 1
  while d==1:
    x = f(x,n)
    y = f(f(y,n),n) 
    d = gcd(abs(x-y),n)
  if d==n:
    return False
  return d

def prime_factors(n):
  factors = set()
  i = 2
  while i*i <= n:
    while (n % i) == 0:
      factors.add(i)
      n = n / i
    i += 1
  if n > 1:
    factors.add(n)
  return factors

if __name__ == '__main__':
  import timeit 
  for i in xrange(2,100):
    print i,
    t1 = timeit.timeit("rho({}, square_minus_one)".format(i), setup="from __main__ import rho, square_minus_one")
    t2 = timeit.timeit("rho({}, square_plus_one)".format(i), setup="from __main__ import rho, square_plus_one")
    t3 = timeit.timeit("rho({}, power_3_minus_one)".format(i), setup="from __main__ import rho, power_3_minus_one")
#    t4 = timeit.timeit("rho({}, random_)".format(i), setup="from __main__ import rho, random_")
    print t1,t2,t3

