""" Hey!! Welcome to my module called SRUTHI"""

def isEven(num):
    """ check whether a number is even or odd"""
    if num%2==0:
        return True
    return False


def factorial(num):
    """generates fatorial of a number"""
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact


pi=3.14
gravity=9.8


def isOdd(num):
    """chek whwther number is even or odd"""
    if num%2==0:
        return False
    return True