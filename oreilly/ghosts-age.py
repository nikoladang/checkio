__author__ = 'nikoladang'
# http://www.geeksforgeeks.org/check-number-fibonacci-number/
# https://docs.python.org/2/library/math.html

import math

def isFibo(x):
    s = math.floor(math.sqrt(x))
    return s*s == x

def checkio(opacity):
    listOpa = [10000] # newborn ghost

    for i in range(1,5001):
        age = i
        value1 = 5*age*age + 4
        value2 = 5*age*age - 4
        if isFibo(value1) or isFibo(value2):
            listOpa.append(listOpa[i-1] - i)
        else:
            listOpa.append(listOpa[i-1] + 1)

    return listOpa.index(opacity)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"