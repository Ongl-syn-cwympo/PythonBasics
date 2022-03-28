# The Fibonacci sequence is a type series where each number is the sum of the two that precede it.
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

# Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
  
