__author__ = 'meldd'

# lab 02  15 feb 2016 - 01 March 2016

import re # import regular expressions

while (True):

  #  op = 1
    expr = input('please enter an expression in one of the following forms:'
                  ' NUMBER+NUMBER // NUMBER - NUMBER // NUM * NUM // N / N ')

    expr = re.sub("\s","", expr)
    expr = re.sub("\W[[+-/*]]","", expr)
    expr = re.sub("\W[[+-/*]]","", expr)
    print(expr)


    if  re.match('^[\d]+[+-/*][\d]+$', expr):
        # use regular expressions to check for correct input

        if (expr.find("/") != -1):  # to find the operands, only continues into the for loop if it finds it

            n = len(expr)  # get length of entered expression
            op = expr.find("/")
            print('you entered:', expr[0:n+1])  # reprint the input expression using place value settings
            opint = int(op)
            Value1 = int(expr[0: opint])  #splice to left of operand and make integer
            Value2 = int(expr[opint+1: n])
            print('first value=', Value1)
            print('second value=', Value2)
            math = Value1 / Value2
            print (math, '=', expr)


        elif (expr.find("+") != -1):
            n = len(expr)  # get length of entered expression
            print('you entered', expr[0:n+1])  # reprint the input expression using place value settings
            op = expr.find("+")  # to find the operand
            opint = int(op)
            #continue
            Value1 = int(expr[0: opint])  # splice to left of operand and make integer
            Value2 = int(expr[opint+1: n])
            print('first value=', Value1)
            print('second value=', Value2)
            math= Value1 + Value2
            print(math, '=', Value1, '+', Value2)

        elif (expr.find("-") != -1):
            n = len(expr)  # get length of entered expression
            print (expr[0:n+1])  # reprint the input expression using place value settings
            op = expr.find("-")  # to find the operand
            opint = int(op)
            Value1 = int(expr[0: opint])  #splice to left of operand and make integer
            Value2 = int(expr[opint+1: n])
            print('first value=', Value1)
            print('second value=', Value2)
            math = (Value1 - Value2)
            print(math, '=', Value1, '-', Value2)

        elif (expr.find("*") != -1):
            n = len(expr)  # get length of entered expression
            print (expr[0:n+1])  # reprint the input expression using place value settings
            op = expr.find("*")  # to find the operand
            opint = int(op)
            Value1 = int(expr[0: opint])  # splice to left of operand and make integer
            Value2 = int(expr[opint+1: n])
            print('first value=', Value1)
            print('second value=', Value2)
            math = (Value1 * Value2)
            print(math, '=', Value1, '*', Value2)


    else:
        print ('not a match, please enter a new expression in the correct form')