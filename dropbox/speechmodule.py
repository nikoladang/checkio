__author__ = 'nikoladang'
# http://stackoverflow.com/questions/14120340/python-error-in-basic-subtraction
    # http://stackoverflow.com/questions/11950819/python-math-is-wrong/11950951#11950951
# http://stackoverflow.com/questions/3886402/python-how-to-get-numbers-after-decimal-point

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

from decimal import *
getcontext().prec = 8

def checkio(number):
    words = []
    original = number
    while number != 0:
        if number < 10:
            words.append(FIRST_TEN[int(number-1)])
            break
        elif number >= 10 and number <= 19:
            whole = int(number // 10)
            # number = math.ceil((number/10 - whole)*10)
            number = int((Decimal(number)/10 - whole)*10)
            words.append(SECOND_TEN[int(number)])
            break
        elif number == 100:
            words.append("one "+HUNDRED)
            break
        elif number > 100:
            whole = int(number // 100)
            number = int((Decimal(number)/100 - whole)*100)
            words.append(FIRST_TEN[whole-1]+ " hundred")
        elif number > 10:
            whole = int(number // 10)
            # number = (number/10 - whole)*10
            number = int((Decimal(number)/10 - whole)*10)
            words.append(OTHER_TENS[whole-2])
    result = " ".join(words)
    print(result)
    return " ".join(words)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
