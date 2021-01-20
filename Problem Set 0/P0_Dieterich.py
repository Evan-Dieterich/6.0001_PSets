#6.0001 Problem Set 0 Solution - Evan Dieterich

import numpy

x = int(input('Please enter an integer: '))
y = int(input('Please enter another integer: '))
z = x**y
a = numpy.log2(z)

print(x, "^", y, "=", z)
print('Log2(' + str(z) + ')' + " = " + str(a))

