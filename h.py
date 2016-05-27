from math import sqrt

def fac(n):
    F = 1
    for i in range(1, n + 1):
        F *= i
    return F

	
def gcd(a, b):

	while a!=0 and b!=0:
		if a > b:
			a = a % b
		else:
			b = b % a	
		F = a+b
	
	return F    

def fib():
	a, b = 1, 1
	while True:
	
		yield a
		
		a, b = b, a + b

def quadratic(a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
	    return ((-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a))
    elif D == 0:
    	return -b / (2 * a)
    else:
    	return None
	
	#### Конец задания. Дальше идет проверочный код, который вы не правите.

print(fac(4))
print(fac(5))	
print(fac(6))	
print('-------------------')
print(gcd(8, 12))
print(gcd(70, 105))
print('-------------------')
f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print('-------------------')
print(quadratic(1, -5, 6))
print(quadratic(2, 4, 2))
print(quadratic(1, 2, 3))

