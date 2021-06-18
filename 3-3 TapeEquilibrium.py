
# Lesson 3 (Time Complexity) TapeEquilibrium

"""
A non-empty array A consisting of N integers is given.
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part
and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal
difference that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
"""



"""
# o(n*n)
def TapeEquilibrium(A):
    N = len(A)
    Diff = []

    for p in range(1, N):
        X1 = sum(A[0:p])
        X2 = sum(A[p:N])
        Diff.append(abs(X2 - X1))
    print(Diff)

    MinDiff = min(Diff)    
    return MinDiff
"""

"""
# o(n*n)
import sys
def TapeEquilibrium(A):
    N = len(A)
    Diff = []
    MinDiff = sys.maxsize
    for p in range(1, N):
        SUM1 = 0
        for i in range(0,p):
            SUM1 += A[i]
        SUM2 = 0
        for j in range(p,N):
            SUM2 += A[j]

        Diff = abs(SUM2 - SUM1)
        MinDiff = min(MinDiff, Diff)    
    return MinDiff
"""

"""
import sys
def TapeEquilibrium(A):
    #MinDiff = None
    MinDiff = sys.maxsize
    SUM1 = 0
    SUM2 = sum(A)
    for p in range(1,len(A)-1):
        SUM1 += A[p-1]
        SUM2 -= A[p-1]
        Diff = abs(SUM1 - SUM2)
        print(Diff)
        #if MinDiff is None or Diff < MinDiff:
        #     MinDiff = Diff
        MinDiff = min(MinDiff, Diff)
    return MinDiff

"""


A = [1, 1, 3]
#A = [3, 1, 2, 4, 3]
#A = [1, 2]
#A = [1, -2, -2, -3, 4]
#A = [1, 1]

import sys
MinDiff = sys.maxsize
SUM1 = 0
SUM2 = sum(A)
for p in range(1,len(A)):
    SUM1 += A[p-1]
    SUM2 -= A[p-1]
    Diff = abs(SUM1 - SUM2)
    print(Diff)
    MinDiff = min(MinDiff, Diff)
print(MinDiff)





#print(TapeEquilibrium(A))










