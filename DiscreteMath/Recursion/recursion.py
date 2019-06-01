import sys
sys.setrecursionlimit(100000)

def factorial(n):
    # Provide your code here
  if n == 1:
    return n
  else:
    return n*factorial(n-1)
print "factorial(5):", factorial(5)
# Expected 120

def fib(n):
    # Provide your code here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print "fib(7):", fib(7)
# Expected 13

def equal(A, B):
  if len(A)==0:
      if len(B)==0:
          return True
  if A[0] != B[0]:
    return False
  else:
    return equal(A[1:],B[1:])

    # Provide your code here

print "equal('ALICE', 'BOB):", equal('ALICE', 'BOB')
# Expected False
print "equal('ALICE', 'ALICE'):", equal('ALICE', 'ALICE')
# Expected True

def addup(list):
    # Provide your code here
    if len(list)==0:
        return 0
    return list[0] + addup(list[1:])

print "addup([1,2,3,4,5]):", addup([1,2,3,4,5])
# Expected 15
print "addup(range(101)):", addup(range(101))
# Expected 5050

def reverse(A):
    # Provide your code here
    if len(A) == 0:
      return A
    else:
      return reverse(A[1:]) + A[0]

print "reverse('hello'):", reverse('hello')
# Expected olleh

def isSorted(list):
    if len(list)==1 or len(list)==0:
        return True
    return list[0]<=list[1] and isSorted(list[1:])
    # Provide your code here

print "isSorted([1,2,3,4]):", isSorted([1,2,3,4])
# Expected True
print "isSorted([1,22,3,4]):", isSorted([1,22,3,4])
# Expected False

def linearSearch(A, value):
    if len(A)==0:
      return False
    if A[0]==value:
      return True
    return linearSearch(A[1:],value)
    # Provide your code here

print "linearSearch([1, 2, 3, 4, 5], 4):", linearSearch([1, 2, 3, 4, 5], 4)
# Expected True
print "linearSearch(range(900), -1):", linearSearch(range(900), -1)
# Expected False

def binarySearch(A, value):
    if len(A)==0:
        return False
    b=len(A)/2
    if A[b]==value:
        return True
    if A[b]>value:
        return binarySearch(A[:b],value)
    if A[b]<value:
        return binarySearch(A[b:],value)

    # Provide your code here

print "binarySearch([1, 2, 3, 4, 5], 4):", binarySearch([1, 2, 3, 4, 5], 4)
# Expected True
print "binarySearch(range(1000000), -1):", binarySearch(range(1000000), -1)
# Expected False
