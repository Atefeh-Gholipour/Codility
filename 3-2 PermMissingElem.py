
# Lesson 3 (Time Complexity) PermMissingElem

"""
An array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)],
which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].
"""


#A = [2, 3, 1, 5]
#A = [2, 3, 1, 5, 6, 7, 4, 9]
#A = []
#A = [2]
A = [1, 2] 


N = len (A)
B = sorted(A)
if N == 0: 
    i = 1
else:
    for i in range(1, N+2):
        if i < N+1:
            if i == B[i-1]:
                i += 1
            else: break
print(i)
            













