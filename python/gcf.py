from functools import reduce
import math
# Am I the only one who calles it GCF (greatest common factor) rather than GCD
def gcf(numbers):
  return reduce(math.gcd, numbers)
