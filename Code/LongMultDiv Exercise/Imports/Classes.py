'''
Classes for LongMultDiv Exercises

You do not need to understand how this code works as
this code goes beyond the scope of this workshop
but feel free to ask questions if you are interested.
'''
class Number(object) :
  '''
  An array of digits

  Representation: Highest to Lowest Ordinals
  '''
  def __init__(self, num) :
    self._digits = []
    self.neg = False
    if isinstance(num, int) :
      if num == 0 :
        self._digits = [0]
      if num < 0 :
        self.neg = True
        num *= -1
      while num > 0 :
        self._digits.append(num % 10)
        num /= 10
      self._digits.reverse()
    else :
      raise TypeError("Number must be initialized with an int.")

  def _toInt(self) :
    value = 0
    for digit in self._digits:
      value *= 10
      value += digit
    if self.neg :
      return -value
    else :
      return value

  def __eq__(self, other) :
    if isinstance(other, self.__class__) :
      return self._toInt() == other._toInt()
    else :
      return NotImplemented 

  def __ne__(self, other) :
    return not self.__eq__(other)

  def __add__(self, other) :
    if isinstance(other, self.__class__) :
      return Number(self._toInt() + other._toInt())
    else :
      return NotImplemented 

  def __sub__(self, other) :
    if isinstance(other, self.__class__) :
      return Number(self._toInt() - other._toInt())
    else :
      return NotImplemented 

  def __mul__(self,other) :
      return NotImplemented 

  def __repr__(self):
    return (self._toInt())

  def __str__(self):
    return str(self._toInt())

  def __gt__(self, other) :
    return self._toInt() > other._toInt()

  def __lt__(self, other) :
    return self._toInt() < other._toInt()

  def __getitem__(self, index) :
    return self._digits[index]

class Digit(Number) :
  '''
  A base-10 Integer in Number form
  '''
  def __init__(self, num) :
    if isinstance(num, int) :
      if num > 9 or num < 0:
        raise ValueError("Digit must be initialized with a value in range [0,9]")
      else :
        super(Digit, self).__init__(num)
    else :
      raise TypeError("Digit must be initialized with an int.")

  def __eq__(self, other) :
    if type(other) is type(self) :
      return self._toInt() == other._toInt()
    else :
      return NotImplemented 

  def __mul__(self,other) :
    if type(other) is type(self) :
      return Number(self._toInt() * other._toInt())
    else :
      raise NotImplementedError