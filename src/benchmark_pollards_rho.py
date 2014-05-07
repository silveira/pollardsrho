import random 

import math 

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

# http://en.wikipedia.org/wiki/Ulam_spiral#Hardy_and_Littlewood.27s_Conjecture_F
def f5(x,n):
  return (4*x*x-2*x+41)%n

def f6(x,n): return (x+1)%n

def f7(x,n): return (x+2)%n

def f8(x,n): return (x+math.sqrt(n))%n

def f9(x,n): return (2**x)%n

def f10(x,n): return (2**x)%n

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
  for i in xrange(2,n):
    rho_i = rho(i,f)
    if(rho_i==False):
        factors = prime_factors(i)
        if (len(factors)!=1):
            print "rho(%d) = %s. Incorrect, not a prime." % (i, rho_i),
            print prime_factors(i)
    else:
        if (i % rho_i != 0):
            print "rho(%d) = %d. Incorrect." % (i, rho_i) 


if __name__ == '__main__':
    for f in f1, f2, f3, f4, f5, f6, f7, f8, f9:
        print f.func_name
        test_correct(f,1000)
        print

    
#  import timeit     
#    t1 = timeit.timeit("rho({}, f1)".format(i), setup="from __main__ import rho, f1")
#    t2 = timeit.timeit("rho({}, f2)".format(i), setup="from __main__ import rho, f2")
#    t3 = timeit.timeit("rho({}, f3)".format(i), setup="from __main__ import rho, f3")
#    t4 = timeit.timeit("rho({}, random_)".format(i), setup="from __main__ import rho, random_")
#    print t1,t2,t3

