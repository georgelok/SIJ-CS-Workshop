from ..Classes import Digit, Number

# Test Values and indices of Numbers
a = Number(123456)
assert(not a.neg)
assert(a[0] == 1)
assert(a[1] == 2)
assert(a[2] == 3)
assert(a[3] == 4)
assert(a[4] == 5)
assert(a[5] == 6)
assert(a._toInt() == 123456)

b = Number(654321)
assert(not(a+b).neg)
assert((a + b)._toInt() == 777777)
assert((a + b) == Number(777777))

c = Number(654321)
assert(a < b)
assert(b > a)
assert(b == c)

d = Number(-123456)
assert(d.neg)
assert(d[0] == 1)
assert(d[1] == 2)
assert(d[2] == 3)
assert(d[3] == 4)
assert(d[4] == 5)
assert(d[5] == 6)
assert(d._toInt() == -123456)


# Test all valid values for Digit
for i in range(10) :
  a = Digit(i)
  assert(a._toInt() == i)
  assert(a == Number(i))
  assert(a[0] == i)

try:
  a = Digit(10)
except ValueError:
  pass
except:
  assert(False)

try:
  a = Digit(-1)
except ValueError:
  pass
except:
  assert(False)

# Test Addition and Multiplication of Digits
a = Digit(5)
b = Digit(6)
c = Digit(5)
assert(type(a+b) is Number)
assert((a+b)._toInt() == 11)
assert((a*b)._toInt() == 30)
assert(a < b)
assert(b > a)
assert(a == c)
print "All Tests Pass"



