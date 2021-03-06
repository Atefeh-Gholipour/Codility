
# Lesson 1 (Iteration)
"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.
Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5,
because N has binary representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32 the function should return 0,
because N has binary representation '100000' and thus no binary gaps.
Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].
"""

def BinaryGap(number):
    Current_gap = 0
    Max_gap = 0

    while number > 0:
        if number & 1 == 1:
            number >>= 1
            while number & 1 == 0 and number > 0 :
                number >>= 1
                Current_gap += 1
            else:
                Max_gap = max (Max_gap, Current_gap)
                Current_gap = 0;
        else:
            number >>= 1
   
    return Max_gap




# decimal number
number = int(input("Enter any decimal number within the range [1..2,147,483,647]: "))

# print equivalent binary number
print("Equivalent Binary Number: ", bin(number).replace("0b",""))

print("Binary Gap is", BinaryGap(number))


