import random 

def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

def f1(x,n):
  return (x*x-1)%n

def f2(x,n):
  return (x*x+1)%n

def f3(x,n):
  return (x*x*x-1)%n

def f4(x,n):
  return random.randint(0,n)

def rho(n, f=f1):
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

def test_correct(f,n=100):
  for i in xrange(2,100):
    rho_i = rho(i,f)
    if(rho_i):
        if (i % rho_i != 0):
            print i, rho_i, "incorrect!" 
    else:
        factors = prime_factors(i)
        if (len(factors)!=1):
            print i, rho_i, "incorrect! (not a prime)	" 

if __name__ == '__main__':
    print "f1"
    test_correct(f1)
    print
    print "f2"
    test_correct(f2)
    print
    print "f3"
    test_correct(f3)
    print
    print "f4"
    test_correct(f4)
#  import timeit     
#    t1 = timeit.timeit("rho({}, f1)".format(i), setup="from __main__ import rho, f1")
#    t2 = timeit.timeit("rho({}, f2)".format(i), setup="from __main__ import rho, f2")
#    t3 = timeit.timeit("rho({}, f3)".format(i), setup="from __main__ import rho, f3")
#    t4 = timeit.timeit("rho({}, random_)".format(i), setup="from __main__ import rho, random_")
#    print t1,t2,t3

