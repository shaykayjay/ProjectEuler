"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

if __name__ == '__main__':
    print 'Problem 001'

def sum_mult_3_5(n):
    mult_3_5  = []
    for i in range(n):
        if i % 3 == 0:
            mult_3_5.append(i)
            
        elif i % 5 == 0:
            mult_3_5.append(i)

    sum_mult = sum(mult_3_5)
    print "Sum of numbers below %d that are multiples of 3 or 5 is: " % (n) + str(sum_mult)

sum_mult_3_5(10)
sum_mult_3_5(1000)

