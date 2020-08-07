# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import math
def multiply(num1, num2):
    n1 = len(num1)
    n2 = len(num2)
    if n1 == 0 or n2 == 0:
        breakpoint()
    if n1 == 1 and n2 == 1:
        return str(int(num1) * int(num2))
    a, b = str(num1)[:n1 // 2], str(num1)[n1 // 2:]
    c, d = str(num2)[:n2 // 2], str(num2)[n2 // 2:]
    ac = multiply(a, c)
    result1 = str(ac) + str(n1 * '0')
    ad = multiply(a, d)
    bc = multiply(b, c)
    ad = list(ad)
    bc = list(bc)

    result2 = addition(ad, bc)

    result2 = result2 + str(int(n1 / 2) * '0')

    bd = multiply(b, d)
    result3 = bd
    print(a, b, c, d)
    print(result1)
    print(result2)
    print(result3)

    result1 = list(result1)
    result2 = list(result2)
    result3 = list(result3)
    result = addition(result1, result2, result3)
    return str(result)

def max(a, b):
    return a if a > b else b

def addition(num1, num2, num3=[0]):
    result = []
    carry = 0
    digit = 0
    number = 0
    print(num1, num2, num3)
    maxlen = max(max(len(num1), len(num2)), len(num3))
    for i in range(1, maxlen + 1):
        number = 0
        if i <= len(num1):
            number += int(num1[-i])
        if i <= len(num2):
            number += int(num2[-i])
        if i <= len(num3):
            number += int(num3[-i])
        number += carry
        print(carry)
        carry = 0
        digit = number

        print(digit)
        if number > 9:
            digit = number % 10
            carry = number//10
        result.insert(0, str(digit))
    if carry > 0: result.insert(0, str(carry))
    result = ''.join(result)
    return str(result)


print(multiply('3141592653589793238462643383279502884197169399375105820974944592',
               '2718281828459045235360287471352662497757247093699959574966967627'))
print(len(
    '8338501009337007687781042603542304498329996508169487535661494318069142095844205524071134729160495531424733726055477252340611184'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
