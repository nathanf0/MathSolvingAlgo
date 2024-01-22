from sympy import sympify, simplify, symbols
import re
from removebrackets import removeBrackets
import simplifyraw
#Convert to mathjax format for nice display on page
def mathjax(eq):
    pattern = r'sqrt\((.*?)\)'
    pattern2 = r'cbrt\((.*?)\)'
    eq = re.sub(pattern, r'\\pm\\sqrt{\1}', eq)
    eq = re.sub(pattern2, r'\\sqrt[3]{\1}', eq)
    eq = re.sub(r'(\([^)]+\))\s*\/\s*(\d+)', r'\\frac{\1}{\2}', eq)
    eq = re.sub(r'(\d+)\s*\/\s*(\d+)', r'\\frac{\1}{\2}', eq)
    return eq
#Normalize data
def normalize(equation, var):
    arr = equation.replace(' ', '')
    arr = arr.replace('**', '^')
    arr = arr.replace('+-', '-')

    normalized = re.sub(r'(?<![\+\-\*/\^(a-z)])-(?![\+\-\*/\^\d])', '+-', arr)

    # Add a '+' after an opening parenthesis if the expression starts with a negative number or variable
    normalized = re.sub(r'\(\-(\d+\.?\d*|[a-z]+)\)', r'(+\1)', normalized)

    # Normalize standalone subtraction (e.g., '4-6' becomes '4+-6') for variables
    arr = re.sub(r'(\d+\.?\d*|[a-z]+)-(?=\d)', r'\1+-', normalized)
    arr = arr.replace('sqrt', '¿')
    arr = arr.replace('cbrt', '»')
    arr = arr.replace('ln', '%')
    arr = arr.replace('arccsc', '1/arcsin')
    arr = arr.replace('arcsec', '1/arccos')
    arr = arr.replace('arccot', '1/arctan')
    arr = arr.replace('arcsin', '¸')
    arr = arr.replace('arccos', '®')
    arr = arr.replace('arctan', '¯')
    arr = arr.replace('csc', '/sin')
    arr = arr.replace('sec', '/cos')
    arr = arr.replace('cot', '/tan')
    arr = arr.replace('sin', '@')
    arr = arr.replace('cos', '?')
    arr = arr.replace('tan', ';')
    arr = re.sub(rf'(\d+){var}', r'\1*' + var, arr)
    arr = re.sub(r'(\d+)([¿»%¸®¯@?;])', r'\1*\2', arr)
    arr = arr.replace(')(', ')*(')
    arr = arr.replace(var+'(', var+'*(')
    arr = arr.replace(')'+var, ')*'+var)



    parcount = 0
    tempindex = 0
    for char in arr:
        if char == '(':
            parcount += 1
        if char == ')':
            parcount -= 1
        if parcount != 0 and char == '+':
            templist = list(arr)
            templist[tempindex] = '~'
            arr = "".join(templist)

            arr = "".join(templist)
        if parcount != 0 and char == '*':
            templist = list(arr)
            templist[tempindex] = '#'
            arr = "".join(templist)
        if parcount != 0 and char == '/':
            templist = list(arr)
            templist[tempindex] = '$'
            arr = "".join(templist)
        if parcount != 0 and char == '^':
            templist = list(arr)
            templist[tempindex] = '&'
            arr = "".join(templist)
        tempindex += 1
    return arr
#Normalize data that does not contain variables
def normalizeraw(equation):
    arr = equation.replace(' ', '')
    arr = arr.replace('**', '^')
    arr = arr.replace('+-', '-')

    normalized = re.sub(r'(?<![\+\-\*/\^(a-z)])-(?![\+\-\*/\^\d])', '+-', arr)

    # Add a '+' after an opening parenthesis if the expression starts with a negative number or variable
    normalized = re.sub(r'\(\-(\d+\.?\d*|[a-z]+)\)', r'(+\1)', normalized)

    # Normalize standalone subtraction (e.g., '4-6' becomes '4+-6') for variables
    arr = re.sub(r'(\d+\.?\d*|[a-z]+)-(?=\d)', r'\1+-', normalized)
    arr = arr.replace('sqrt', '¿')
    arr = arr.replace('cbrt', '»')
    arr = arr.replace('ln', '%')
    arr = arr.replace('arccsc', '1/arcsin')
    arr = arr.replace('arcsec', '1/arccos')
    arr = arr.replace('arccot', '1/arctan')
    arr = arr.replace('arcsin', '¸')
    arr = arr.replace('arccos', '®')
    arr = arr.replace('arctan', '¯')
    arr = arr.replace('csc', '/sin')
    arr = arr.replace('sec', '/cos')
    arr = arr.replace('cot', '/tan')
    arr = arr.replace('sin', '@')
    arr = arr.replace('cos', '?')
    arr = arr.replace('tan', ';')
    arr = re.sub(r'(\d+)([¿»%¸®¯@?;])', r'\1*\2', arr)
    arr = arr.replace(')(', ')*(')


    return arr
#Simplify using a combination of sympy simplification algorithms and mine
def simplified(eq, var):
    try:
        eq = normalize(eq, var)
        eq = eq.replace(' ', '')
        eq = eq.replace('**', '^')
        eq = removeBrackets(eq)
        eq = unnormalize(eq, var)
        eq = re.sub(rf'(\d+){var}', r'\1*' + var, eq)
        try:
            equation = sympify(eq)
            simplified_equation = simplify(equation)
            simplified_equation = str(simplified_equation)
            simplified_equation = simplified_equation.replace('**', '^')
            simplified_equation = simplified_equation.replace(' ', '')
            simplified_equation = simplified_equation.replace('log', 'ln')
        except:
            pass
        patterncbrt = r'(\d+)\^\(1/3\)'
        patternsqrt = r'(\d+)\^\(1/2\)'
        simplified_equation = re.sub(patterncbrt, r'»(\1)', simplified_equation)
        simplified_equation = re.sub(patternsqrt, r'¿(\1)', simplified_equation)
        simplified_equation = re.sub(rf'(\d+)\*{var}', r'\1' + var, simplified_equation)
        return simplified_equation
    except:
        return eq
#Unnormalize the data so it doesn't look odd
def unnormalize(str, var):
    str = str.replace('**', '^')
    two = str.replace('~', '+')
    three = two.replace('#', '*')
    arr = three.replace('$', '/')
    arr = arr.replace('&', '^')
    arr = re.sub(r'(\d+)\*([¿»%¸®¯@?;])', r'\1\2', arr)
    arr = re.sub(rf'(\d+)\*{var}', r'\1'+var, arr)

    for char in arr:
        if char.isalpha():
            alphaindex = arr.index(char)
            if arr[alphaindex-1] == '*':
                arr = list(arr)
                arr.pop(alphaindex-1)
                arr = "".join(arr)
    arr = arr.replace('¿', 'sqrt')
    arr = arr.replace('»', 'cbrt')
    arr = arr.replace('%', 'ln')
    arr = arr.replace('@', 'sin')
    arr = arr.replace('?', 'cos')
    arr = arr.replace(';', 'tan')
    arr = arr.replace('/sin', 'csc')
    arr = arr.replace('/cos', 'sec')
    arr = arr.replace('/tan', 'cot')
    arr = arr.replace('¸', 'arcsin')
    arr = arr.replace('®', 'arccos')
    arr = arr.replace('¯', 'arctan')
    arr = arr.replace('1/arcsin', 'arccsc')
    arr = arr.replace('1/arccos', 'arcsec')
    arr = arr.replace('1/arctan', 'arccot')

    arr = arr.replace('+-', '-')
    arr = arr.replace('*(', '(')

    return arr
#Unnormalize data that doesnt contain variables
def unnormalizeraw(str):
    str = str.replace('**', '^')
    two = str.replace('~', '+')
    three = two.replace('#', '*')
    arr = three.replace('$', '/')
    arr = arr.replace('&', '^')
    arr = re.sub(r'(\d+)\*([¿»%¸®¯@?;])', r'\1\2', arr)

    arr = arr.replace('¿', 'sqrt')
    arr = arr.replace('»', 'cbrt')
    arr = arr.replace('%', 'ln')
    arr = arr.replace('@', 'sin')
    arr = arr.replace('?', 'cos')
    arr = arr.replace(';', 'tan')
    arr = arr.replace('/sin', 'csc')
    arr = arr.replace('/cos', 'sec')
    arr = arr.replace('/tan', 'cot')
    arr = arr.replace('¸', 'arcsin')
    arr = arr.replace('®', 'arccos')
    arr = arr.replace('¯', 'arctan')
    arr = arr.replace('1/arcsin', 'arccsc')
    arr = arr.replace('1/arccos', 'arcsec')
    arr = arr.replace('1/arctan', 'arccot')

    arr = arr.replace('+-', '-')
    arr = arr.replace('*(', '(')
    return arr