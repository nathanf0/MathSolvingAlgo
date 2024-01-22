from normalization import normalize, simplified, unnormalize, mathjax
import re
import polynomials
import operations


#Variable Solving Algorithm

def eq(equation, var):
    equation = equation.replace(' ', '')
    arr = equation
    splitarr = arr.split('=')
    left = splitarr[0]
    right = splitarr[1]
    left = unnormalize(left, var)
    right = unnormalize(right, var)
    equation = left + '=' + right
    print('$' + mathjax(left) + '=' + mathjax(right) + '$')
    left = str(simplified(left, var))
    right = str(simplified(right, var))
    left = unnormalize(left, var)
    right = unnormalize(right, var)
    while True:
        if left + '=' + right != equation:
            print('Simplify the equation')
            print('$'+mathjax(left) + '=' + mathjax(right)+'$')

        leftadd = left
        rightadd = right

        left = normalize(left, var)
        right = normalize(right, var)

        testervarcount = 0
        for char in right:
            if char == var:
                testervarcount += 1
                break
        varcount = 0
        for char in left:
            if char == var:
                varcount += 1
                break

        if varcount == 0 and testervarcount > 0:
            leftcopy = left
            rightcopy = right
            left = rightcopy
            right = leftcopy
            print('Swap the left and right sides')
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            left = str(simplified(left, var))
            right = str(simplified(right, var))
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print(mathjax(left) + '=' + mathjax(right))
        elif varcount > 0 and testervarcount > 0:
            rightaddsplit = right.split('+')
            for term in rightaddsplit:
                if var in term:
                    if term[0] == '-':
                        term = list(term)
                        term.pop(0)
                        term = "".join(term)
                        left = left + "+" + term
                        right = right.replace('-'+term, '')
                    else:
                        left = left + "-" + term
                        if term == rightaddsplit[0] and len(rightaddsplit) > 1:
                            right = right.replace(term+"+", '')
                        elif term == rightaddsplit[0]:
                            right = right.replace(term, '')
                        else:
                            right = right.replace("+"+term, '')
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print(f"Move all the {var} variables to the left side")
            print('$' + left + '=' + right + '$')
        elif varcount == 0 and testervarcount == 0:
            print('The variable you are solving for is not in the equation.')
            return None
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        quadmatch = re.search(rf'\d*{var}\^2\+\d*{var}\+*\d*', left)
        if quadmatch:
            if quadmatch.group() == left:
                testquad = 0
                for char in right:
                    if char.isalpha():
                        testquad = 1
                if testquad == 0:
                    if right[0] == '-':
                        right = list(right)
                        right.pop(0)
                        right = "".join(right)
                        left += '+' + right
                    else:
                        left += '-' + right
                    left = simplified(left, var)
                    left = unnormalize(left, var)
                    right = '0'
                    print('It is a quadratic so set the right side equal to 0')
                    print('$' + left + '=' + right + '$')
                    return polynomials.quadraticroots(left, var)
                else:
                    print('Cannot solve this quadratic because there are too many variables')
                    return None

        left = normalize(left, var)
        right = normalize(right, var)

        s = left.split('+')
        for part in s:
            if var in part:
                continue
            if part[0] == '-':
                right +='+'+part[1:]
            else:
                right +='-'+part
            templeft = list(left)
            if '+'+part in left:
                left = left.replace('+'+part, '', 1)
            else:
                left = left.replace(part+'+', '', 1)

        left = unnormalize(left, var)
        right = unnormalize(right, var)

        if left != leftadd or right != rightadd:
            print('Move all terms that do not contain the variable being solved')
            return eq(left + '=' + right, var)
        leftadd = left
        rightadd = right
        left = normalize(left, var)
        right = normalize(right, var)
        left = str(simplified(left, var))
        right = str(simplified(right, var))
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if left != leftadd or right != rightadd:
            print('Simplify')
            print('$'+mathjax(left) + '=' + mathjax(right)+'$')

        checkdenomleft = left.split('/')
        checkdenomright = right.split('/')

        for part in checkdenomleft:
            if var in part and left.index(part) != 0:
                if left[left.index(part) - 1] == '/':

                    part2 = ''
                    denomparenleft = 0
                    denomparenright = 0
                    for char in part:
                        if char == '(':
                            denomparenleft += 1
                        if char == ')':
                            denomparenright += 1
                        part2 += char
                        if denomparenleft == denomparenright:
                            break
                    part2temp = left.index(part2)
                    left = list(left)
                    for i in range(len(part2)):
                        left.pop(part2temp)
                    left.pop(part2temp-1)

                    right = '(' + right + ')' + '*' + part2
                    left = "".join(left)
                    left = simplified(left, var)
                    right = simplified(right, var)
                    left = unnormalize(left, var)
                    right = unnormalize(right, var)
                    print('Multiply both sides by the denominator')
                    return eq(left + '=' + right, var)

        for part in checkdenomright:
            if var in part and right.index(part) != 0:
                if right[right.index(part) - 1] == '/':
                    part2 = ''
                    denomparenleft = 0
                    denomparenright = 0
                    for char in part:
                        if char == '(':
                            denomparenleft += 1
                        if char == ')':
                            denomparenright += 1
                        part2 += char
                        if denomparenleft == denomparenright:
                            break
                    part2tempright = right.index(part2)

                    right = list(right)
                    for i in range(len(part2)):
                        right.pop(part2tempright)
                    right.pop(part2tempright-1)
                    left = '(' + left + ')' + '*' + part2
                    right = "".join(right)
                    left = simplified(left, var)
                    right = simplified(right, var)
                    left = unnormalize(left, var)
                    right = unnormalize(right, var)
                    print('Multiply both sides by the denominator')
                    return eq(left + '=' + right, var)

        leftdiv = left
        rightdiv = right

        left = normalize(left, var)
        right = normalize(right, var)

        termsdivide = left.split('/')



        for part in termsdivide:

            if var in part:
                pass
            else:
                left = left.replace('/'+part, '', 1)
                right = '(' + right + ')' + '*' + part

        left = unnormalize(left, var)
        right = unnormalize(right, var)

        if left != leftdiv or right != rightdiv:
            print('Multiply both sides')
            return eq(left + '=' + right, var)
        leftdiv = left
        rightdiv = right
        left = str(simplified(left, var))
        right = str(simplified(right, var))
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if left != leftdiv or right != rightdiv:
            print('Simplify')
            print('$'+mathjax(left) + '=' + mathjax(right)+'$')

        leftmult = left
        rightmult = right

        left = normalize(left, var)
        right = normalize(right, var)

        termsmult = left.split('*')



        for part in termsmult:
            if var in part:
                continue
            if left.index(part) == 0:
                left = left.replace(part+'*', '', 1)
            else:
                left = left.replace('*'+part, '', 1)
            right = '(' + right + ')' + '/' + part



        left = unnormalize(left, var)
        right = unnormalize(right, var)

        if left != leftmult or right != rightmult:
            print('Divide both sides')
            return eq(left + '=' + right, var)
        leftmult = left
        rightmult = right

        left = str(simplified(left, var))
        right = str(simplified(right, var))
        left = unnormalize(left, var)
        right = unnormalize(right, var)

        if left != leftmult or right != rightmult:
            print('Simplify')
            print('$'+mathjax(left) + '=' + mathjax(right)+'$')



        left = normalize(left, var)
        right = normalize(right, var)


        termsexponent = left.split('^')
        if len(termsexponent) > 1:
            lefttermsexponent = termsexponent[0]
            righttermsexponent = termsexponent[1]


            if var in lefttermsexponent and not var in righttermsexponent:
                left = left.replace('^'+righttermsexponent, '', 1)
                if righttermsexponent == '2':
                    right = 'sqrt('+right+')'
                    expprint = 'Take the square root of both sides'
                elif righttermsexponent == '3':
                    right = 'cbrt('+right+')'
                    expprint = 'Take the cubed root of both sides'
                else:
                    right = '(' + right + ')' + '^(1/' + righttermsexponent+')'
                    expprint = 'Exponentiate both sides with the reciprocal of the exponent'
                print(expprint)
                left = left.replace('**', '^')
                right = right.replace('**', '^')
                return eq(left + '=' + right, var)
            elif var not in lefttermsexponent and var in righttermsexponent:
                left = left.replace(lefttermsexponent+'^', '', 1)
                if lefttermsexponent == 'e':
                    right = 'ln('+right+')'
                else:
                    right = 'ln('+right+')/ln('+lefttermsexponent+')'
                expprint = 'Take the log of both sides'
                print(expprint)
                left = left.replace('**', '^')
                right = right.replace('**', '^')
                return eq(left + '=' + right, var)


            left = unnormalize(left, var)
            right = unnormalize(right, var)

            leftexp = left
            rightexp = right

            left = str(simplified(left, var))
            right = str(simplified(right, var))
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            if leftexp != left or rightexp != right:
                print('Simplify')
                print('$'+mathjax(left) + '=' + mathjax(right)+'$')

        left = normalize(left, var)
        right = normalize(right, var)

        if left[0] == '%':
            left = list(left)
            left.pop(0)
            left = "".join(left)
            right = 'e^('+right+')'
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print('Exponentiate both sides by e')
            return eq(left + '=' + right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        leftln = left
        rightln = right
        left = simplified(left, var)
        right = simplified(right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if leftln != left or rightln != right:
            print('Simplify')
            print('$'+mathjax(left) + '=' + mathjax(right)+'$')

        left = normalize(left, var)
        right = normalize(right, var)

        if left[0] == ';':
            left = list(left)
            left.pop(0)
            left = "".join(left)
            tempright = operations.arctandictrad.get(right)
            if tempright:
                right = tempright
            else:
                right = 'arctan('+right+')'
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print('Take the arctan of both sides')
            return eq(left + '=' + right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        lefttan = left
        righttan = right
        left = simplified(left, var)
        right = simplified(right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if lefttan != left or righttan != right:
            print('Simplify')
            print('$' + mathjax(left) + '=' + mathjax(right) + '$')

        left = normalize(left, var)
        right = normalize(right, var)

        if left[0] == '?':
            left = list(left)
            left.pop(0)
            left = "".join(left)
            tempright = operations.arccosdictrad.get(right)
            if tempright:
                right = tempright
            else:
                right = 'arccos(' + right + ')'
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print('Take the arccos of both sides')
            return eq(left + '=' + right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        leftcos = left
        rightcos = right
        left = simplified(left, var)
        right = simplified(right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if leftcos != left or rightcos != right:
            print('Simplify')
            print('$' + mathjax(left) + '=' + mathjax(right) + '$')

        left = normalize(left, var)
        right = normalize(right, var)

        if left[0] == '@':
            left = list(left)
            left.pop(0)
            left = "".join(left)
            tempright = operations.arcsindictrad.get(right)
            if tempright:
                right = tempright
            else:
                right = 'arcsin(' + right + ')'
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print('Take the arcsin of both sides')
            return eq(left + '=' + right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        leftsin = left
        rightsin = right
        left = simplified(left, var)
        right = simplified(right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if leftsin != left or rightsin != right:
            print('Simplify')
            print('$' + mathjax(left) + '=' + mathjax(right) + '$')

        left = normalize(left, var)
        right = normalize(right, var)

        if left[0] == '¯':
            left = list(left)
            left.pop(0)
            left = "".join(left)
            tempright = operations.tandictrad.get(right)
            tempright2 = operations.tandictdeg.get(right)
            if tempright:
                right = tempright
            elif tempright2:
                right = tempright2
            else:
                right = 'tan(' + right + ')'
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print('Take the tangent of both sides')
            return eq(left + '=' + right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        leftarctan = left
        rightarctan = right
        left = simplified(left, var)
        right = simplified(right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if leftarctan != left or rightarctan != right:
            print('Simplify')
            print('$' + mathjax(left) + '=' + mathjax(right) + '$')

        left = normalize(left, var)
        right = normalize(right, var)

        if left[0] == '®':
            left = list(left)
            left.pop(0)
            left = "".join(left)
            tempright = operations.cosdictrad.get(right)
            tempright2 = operations.cosdictdeg.get(right)
            if tempright:
                right = tempright
            elif tempright2:
                right = tempright2
            else:
                right = 'cos(' + right + ')'
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print('Take the cosine of both sides')
            return eq(left + '=' + right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        leftarccos = left
        rightarccos = right
        left = simplified(left, var)
        right = simplified(right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if leftarccos != left or rightarccos != right:
            print('Simplify')
            print('$' + mathjax(left) + '=' + mathjax(right) + '$')

        left = normalize(left, var)
        right = normalize(right, var)

        if left[0] == '¸':
            left = list(left)
            left.pop(0)
            left = "".join(left)
            tempright = operations.sindictrad.get(right)
            tempright2 = operations.sindictdeg.get(right)
            if tempright:
                right = tempright
            elif tempright2:
                right = tempright2
            else:
                right = 'sin(' + right + ')'
            left = unnormalize(left, var)
            right = unnormalize(right, var)
            print('Take the sine of both sides')
            return eq(left + '=' + right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        leftarcsin = left
        rightarcsin = right
        left = simplified(left, var)
        right = simplified(right, var)
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        if leftarcsin != left or rightarcsin != right:
            print('Simplify')
            print('$' + mathjax(left) + '=' + mathjax(right) + '$')

        while left[0] == '(' and left[len(left)-1] == ')':
            left = list(left)
            left.pop(len(left)-1)
            left.pop(0)
            left = "".join(left)

        if len(left) == 1:
            break

        left = str(simplified(left, var))
        right = str(simplified(right, var))
        left = unnormalize(left, var)
        right = unnormalize(right, var)
        equation = left + '=' + right
