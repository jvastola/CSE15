# Exercise 1: Implement Euclid's Algorithm for finding the greatest common divisor of two integers
def gcd(a, b):
  if a % b != 0:
    return gcd(b, a % b)
  else:
    return b
print gcd(128, 60)
# Expected output: 4



# Exercise 2: Consider the following representation of mathematical expressions: a list of tuples, where each tuple has exactly 2 elements, a coefficient and a term. For example, the expression:

# 2x + 5y - 3z is represented as [(2, x), (5, y), (-3, z)]

# We sometimes need to simplify expressions by grouping together like terms. For example:

# 2x + 5y + 4x = 6x + 5y

# Implement the function groupLikeTerms, where the input exp is a mathematical expression represented as a list of tuples, and it should return a simplified mathematical expression represented as a list of tuples.
def groupLikeTerms(exp):
  Sum = {}
  for a, b in exp:
        if b in Sum:
            Sum[b] += a
            new_arr=[]
            new_tmp=()
        else:
            Sum[b] = a
  for a, b in Sum.items():
        new_tmp = (b, a)
        new_arr.append(new_tmp)
        new_tmp = ()
  new_arr = [(a,b) for (b,a) in sorted(Sum.items())]
  return new_arr
print groupLikeTerms([(5, "x"), (5, "y"), (-3, "x")])
# Expected output: [(2, 'x'), (5, 'y')]



# Exercise 3: We sometimes need to substitute expressions into other expressions. For example if we have the expression 2x + 5y, and we know that x = 3a - b, we can substitute the expression for x into the original expression, resulting in: 6a - 2b + 5y.

# Implement the substitution function below. It should take an expression (list of tuples), a term, and another expression. It should substitute the occurences of term in exp, with value. The result should be in its simplest form, i.e. like terms should be grouped together

# For example: substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)]) results in [(-5, 9), (2, 23)]
def substitute(exp, term, value):
    list1 = []
    l = len(exp)
    for i in range(0,l):
      if exp[i][1] == term:
        a = exp[i][0]
        l = len(value)
        for x in range (0,l):
          b = value[x][0]
          c = a *b
          list1.append((c,value[x][1]))
      else:
        list1.append((exp[i][0],exp[i][1]))
    list1 = groupLikeTerms(list1)
    return list1

print substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)])
# Expected output: [(-5, 9), (2, 23)]



# Exercise 4: Using the functions you implemented above, implement the Extended Euclidean Algorithm, which returns the GCD of two integers a, and b, as a linear combination of a and b.

# For example: extended_euclid(101, 23) results in (1, [(22, 23), (-5, 101)]), where the GCD is 1 and it can be expressed as 22*23 - 5*101
def extended_euclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    c = a
    d = b
    while b != 0:
        q = a//b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        a, b = b, a % b
    return  a, [(y0, d), (x0, c)]
print extended_euclid(101, 23)
# Expected output: (1, [(22, 23), (-5, 101)])


# Exercise 5: Use the Extended Euclidean Algorithm to implement the function for multiplicative inverses. As you know, a multiplicative inverse n modulo m is guaranteed to exist if n and m are relatively prime. If they are not, your algorithm should return None (which is the null value of Python), otherwise, if n and m are relatively prime, you should return the inverse of n modulo m.
def inverse(n, m):
  a, [(b, d), (w, c)] = extended_euclid(n, m)
  if a == 1:
    return w
  else:
    return n
print inverse(23, 101)
# Expected output: 22
