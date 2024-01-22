import re
import operations
from removebrackets import removeBrackets
import math
from fractions import Fraction

#Solve expressions that do not contain variables

def evaluate_innermost(innermost):
    while True:
        copy = innermost
        #Process sine
        while re.search(r'@(\(.*\)|[-\d\.a-zA-Z]+)', innermost):
            match = re.search(r'@(?P<number>\(.*\)|[-\d\.a-zA-Z]+)', innermost)
            if match:
                num = match.group('number')
                if 'pi' in num:
                    result = operations.sinraw(num, 'radians', 'exact')
                else:
                    result = operations.sinraw(num, 'degrees', 'exact')
                innermost = innermost.replace(match.group(), result)

        #Process cosine
        while re.search(r'\?(\(.*\)|[-\d\.a-zA-Z]+)', innermost):
            match = re.search(r'\?(?P<number>\(.*\)|[-\d\.a-zA-Z]+)', innermost)
            if match:
                num = match.group('number')
                if 'pi' in num:
                    result = operations.cosraw(num, 'radians', 'exact')
                else:
                    result = operations.cosraw(num, 'degrees', 'exact')
                innermost = innermost.replace(match.group(), result)

        #Process tangent

        while re.search(r';(\(.*\)|[-\d\.a-zA-Z]+)', innermost):
            match = re.search(r';(?P<number>\(.*\)|[-\d\.a-zA-Z]+)', innermost)
            if match:
                num = match.group('number')
                if 'pi' in num:
                    result = operations.tanraw(num, 'radians', 'exact')
                else:
                    result = operations.tanraw(num, 'degrees', 'exact')
                innermost = innermost.replace(match.group(), result)

        #Process logarithms
        while re.search(r'%(-?\d+\.?\d*)', innermost):
            match = re.search(r'%(?P<number>-?\d+\.?\d*)', innermost)
            if match:
                num = match.group('number')
                result = operations.rawln(num)
                innermost = innermost.replace(match.group(), result)

        # Process exponents
        while re.search(r'-?\d+\.?\d*\^-?\d+\.?\d*', innermost):
            match = re.search(r'(-?\d+\.?\d*)\^(-?\d+\.?\d*)', innermost)
            if match:
                num1, num2 = match.groups()
                result = operations.exponentraw(num1, num2)
                innermost = innermost.replace(match.group(), result)


        # Process multiplication
        while re.search(r'-?\d+\.?\d*[*]-?\d+\.?\d*', innermost):
            match = re.search(r'(-?\d+\.?\d*)[*](-?\d+\.?\d*)', innermost)
            if match:
                num1, num2 = match.groups()
                result = operations.multraw(num1, num2)
                innermost = innermost.replace(match.group(), result)

        # Process division
        while re.search(r'-?\d+\.?\d*[/]-?\d+\.?\d*', innermost):
            match = re.search(r'(-?\d+\.?\d*)[/](-?\d+\.?\d*)', innermost)
            if match:
                num1, num2 = match.groups()
                result = operations.divideraw(num1, num2)
                innermost = innermost.replace(match.group(), result)

        # Process addition
        while re.search(r'-?\d+\.?\d*[+]-?\d+\.?\d*', innermost):
            match = re.search(r'(-?\d+\.?\d*)[+](-?\d+\.?\d*)', innermost)
            if match:
                num1, num2 = match.groups()
                result = operations.addraw(num1, num2)
                innermost = innermost.replace(match.group(), result)

        if innermost == copy:
            return innermost

def replace_numbers_with_multiplication(input_string):
    # Define a regular expression pattern to match a number followed by parentheses
    pattern = r'(\d+)(\()'

    # Define a replacement string with a multiplication symbol
    replacement = r'\1*('

    # Use re.sub to replace matches in the input string
    result_string = re.sub(pattern, replacement, input_string)

    return result_string

def sqr_sim(und_root):
    und_root = int(und_root)
    if math.sqrt(und_root).is_integer():
        return str(int(math.sqrt(und_root)))
    und_root0 = round(und_root)
    rt_fc = []
    coef = 1
    if und_root < 0:
        return None
    elif und_root == 0:
        return 0
    else:
        for i in range(2, und_root0):
            if und_root%(i**2) == 0:
                rt_fc.append(i)
                und_root /= i**2

                for i0 in range(2, und_root0):
                    if und_root%(i0**2) == 0:
                        rt_fc.append(i0)
                        und_root /= i0**2

        for ele in rt_fc:
            coef *= ele
        if coef > 1:
            return str(int(coef)) + 'sqrt' + str(int(und_root))
        else:
            return 'sqrt' + str(int(und_root))

def simplifyfrac(eq):
    spliteq = eq.split('/')
    num = int(spliteq[0])
    denom = int(spliteq[1])
    q = Fraction(num, denom)
    num = Fraction.numerator
    denom = Fraction.denominator
    return str(num)+'/'+str(denom)


def simplifyraw(expression):
    expression = expression.replace(")(", ")*(")
    expression = replace_numbers_with_multiplication(expression)
    expression = removeBrackets(expression)
    # Find the innermost parentheses
    innermost_match = re.search(r'\(([^()]+)\)', expression)

    while innermost_match:
        innermost = innermost_match.group(1)
        innermost_result = evaluate_innermost(innermost)
        expression = expression.replace(f'({innermost})', innermost_result)
        innermost_match = re.search(r'\(([^()]+)\)', expression)

    # Evaluate the remaining expression
    result = evaluate_innermost(expression)
    result = removeBrackets(result)
    return result

