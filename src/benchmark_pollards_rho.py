def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

def f(x,n):
  return (x*x-1)%n

def rho(n):
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

if __name__ == '__main__':
	import timeit
	for i in xrange(2,100):
		print i,
		t = timeit.timeit("rho({})".format(i), setup="from __main__ import rho")
		print t, "rho({})={}".format(i,rho(i))

