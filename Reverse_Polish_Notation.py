#
# Reverse Polish Notation
#
# https://en.wikipedia.org/wiki/Reverse_Polish_notation
#

from Stack import *
import operator

def rpn(input_string):
    """
    Returns evaluated reverse polish notation expression

    Input is a string, containing an expression in 
    reverse polish notation. Expression is evaluated and 
    returns the output as a string.
    
    ex. rpn("3 4 +") = "7" 
    """
    _stack = Stack()
    elements = input_string.split(" ")
    for element in elements:
        if element == '+':
            operator1 = _stack.pop()
            operator2 = _stack.pop()
            _stack.push(operator2 + operator1)
        elif element == '-':
            operator1 = _stack.pop()
            operator2 = _stack.pop()
            _stack.push(operator2 - operator1)
        elif element == '*':
            operator1 = _stack.pop()
            operator2 = _stack.pop()
            _stack.push(operator2 * operator1)
        elif element == '/':
            operator1 = _stack.pop()
            operator2 = _stack.pop()
            _stack.push(operator2 // operator1)
        else:
            _stack.push(int(element))

    result = _stack.pop()
    return result
