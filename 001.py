# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

M   =    3
N   =    5
MAX = 1000

def sum_mult(n1, n2, num):
    i = 0
    s = 0
    while(i < num):
        if (i % n1 == 0 or i %n2 == 0 and i % 15 != 0):
            s += i
        i += 1
    return s

print(sum_mult(M, N, MAX))

