import math
from fractions import Fraction

#Operations to solve string equations/expressions

def disexponent(num, cont):
    if ')^' in num:
        split = num.split('^')
        two = split[1]
        tempindex = num.index(')^')-1
        array.remove(')^')
        temparray = []
        while tempindex > -1:
            if num[tempindex] == '(':
                num.pop(tempindex)
                break
            else:
                for j in range(two):
                    temparray.insert(0, num[tempindex])
        if not ')^' and not '^' in num:
            return "".join(temparray)


def addraw(num1, num2):
    rnum1 = num1.replace('-', '')
    rnum2 = num2.replace('-', '')
    if rnum1.isdigit() and rnum2.isdigit():
        return str(int(num1) + int(num2))
    elif rnum1.replace(".", "").isdigit() and rnum2.replace(".", "").isdigit():
        return str(float(num1) + float(num2))
    elif rnum1.replace("/", "").isdigit() and rnum2.replace(".", "").isdigit():
        temp = num1.split('/')
        num1 = float(temp[0] / temp[1])
        return str(float(num1) + float(num2))
    elif rnum1.replace(".", "").isdigit() and rnum2.replace("/", "").isdigit():
        temp = num2.split('/')
        num2 = float(temp[0] / temp[1])
        return str(float(num1) + float(num2))
    elif rnum1.replace("/", "").isdigit() and rnum2.replace("/", "").isdigit():
        temp1 = num1.split('/')
        temp2 = num2.split('/')
        num1num = int(temp1[0])
        num2num = int(temp2[0])
        num1denom = int(temp1[1])
        num2denom = int(temp2[1])

        commondenom = num1denom * num2denom
        num1num = num1num * num2denom
        num2num = num2num * num1denom
        num3num = num1num + num2num
        return str(num3num) + '/' + str(commondenom)

def add(num1, num2):
    variable = 0
    expcount1 = 0
    expcount2 = 0
    vartypes1 = []
    vartypes2 = []
    for char in num1:
        if char.isalpha():
            variable += 1
            vartypes1.append(char)
        elif char == '^':
            expcount1 += 1
    for char in num2:
        if char.isalpha():
            variable += 1
            vartypes2.append(char)
        elif char == '^':
            expcount2 += 1
    if variable == 0:
        return(addraw(num1, num2))
    elif len(vartypes1) != len(vartypes2):
        return (num1 + '+' + num2)
    elif sorted(vartypes1) == sorted(vartypes2):
        if expcount1 == 0 and expcount2 == 0:
            storedvar = ''
            for var in vartypes1:
                storedvar += var
                num1 = num1.replace(var, '')
                num2 = num2.replace(var, '')
            result = addraw(num1, num2)
            result += storedvar
            return str(result)
        elif expcount1 != expcount2:
            return (num1 + '+' + num2)
        elif expcount1 == 1 and expcount2 == 1:
            num1splitexp = num1.split('^')
            num2splitexp = num2.split('^')
            leftexp1 = num1splitexp[0]
            leftexp2 = num2splitexp[0]
            rightexp1 = num1splitexp[1]
            rightexp2 = num2splitexp[1]
            if rightexp1 == rightexp2:
                storedvar = ''
                for var in vartypes1:
                    storedvar += var
                    leftexp1 = leftexp1.replace(var, '')
                    leftexp2 = leftexp2.replace(var, '')
                result = addraw(leftexp1, leftexp2)
                result += storedvar
                result = result + '^' + rightexp1
                return result
            else:
                return (num1 + '+' + num2)
        else:
            return (num1 + '+' + num2)
    else:
        return (num1 + '+' + num2)

def multraw(num1, num2):
    rnum1 = num1.replace('-', '')
    rnum2 = num2.replace('-', '')
    if rnum1.isdigit() and rnum2.isdigit():
        return str(int(num1) * int(num2))
    elif rnum1.replace(".", "").isdigit() and rnum2.replace(".", "").isdigit():
        return str(float(num1) * float(num2))
    elif rnum1.replace("/", "").isdigit() and rnum2.replace(".", "").isdigit():
        temp = num1.split('/')
        num1 = float(temp[0] / temp[1])
        return str(float(num1) * float(num2))
    elif rnum1.replace(".", "").isdigit() and rnum2.replace("/", "").isdigit():
        temp = num2.split('/')
        num2 = float(temp[0] / temp[1])
        return str(float(num1) * float(num2))
    elif rnum1.replace("/", "").isdigit() and rnum2.replace("/", "").isdigit():
        temp1 = num1.split('/')
        temp2 = num2.split('/')
        num1num = int(temp1[0])
        num2num = int(temp2[0])
        num1denom = int(temp1[1])
        num2denom = int(temp2[1])

        commondenom = num1denom * num2denom
        num3num = num1num * num2num
        return str(num3num) + '/' + str(commondenom)

def multiply(num1, num2):
    variable = 0
    expcount1 = 0
    expcount2 = 0
    vartypes1 = []
    vartypes2 = []
    for char in num1:
        if char.isalpha():
            variable += 1
            vartypes1.append(char)
        elif char == '^':
            k = num1.index(char)
            expcount1 += 1
    for char in num2:
        if char.isalpha():
            variable += 1
            vartypes2.append(char)
        elif char == '^':
            expcount2 += 1
    if variable == 0:
        return(multraw(num1, num2))
    if num1 == num2:
        return num1 + '^2'
    elif expcount1 == 0 and expcount2 == 0:

        if len(vartypes1) > 0 and len(vartypes2) == 0:
            storedvar = ''
            for var in vartypes1:
                storedvar += var
                num1 = num1.replace(var, '')
            result = multraw(num1, num2)
            result += storedvar
            return result

        elif len(vartypes1) == 0 and len(vartypes2) > 0:
            storedvar = ''
            for var in vartypes2:
                storedvar += var
                num2 = num2.replace(var, '')
            result = multraw(num1, num2)
            result += storedvar
            return result

        elif len(vartypes1) > 0 and len(vartypes2) > 0:
            storedvar = ''
            for var in vartypes1:
                storedvar += var
                num1 = num1.replace(var, '')
            for var in vartypes2:
                storedvar += var
                num2 = num2.replace(var, '')
            result = multraw(num1, num2)
            result += storedvar
            return result
    elif expcount1 == 1 and expcount2 == 1:
        expcounter = 0
        num1splitexp = num1.split('^')
        num2splitexp = num2.split('^')
        leftexp1 = num1splitexp[0]
        leftexp2 = num2splitexp[0]
        rightexp1 = num1splitexp[1]
        rightexp2 = num2splitexp[1]
        leftexp1len = len(leftexp1)
        leftexp2len = len(leftexp2)
        tempvar1 = ''
        tempvar2 = ''
        if leftexp1[leftexp1len-1] != ')':
            tempvar1 = leftexp1[leftexp1len-1]
        else:
            charright1 = 0
            charright2 = 0

        for char in rightexp1:
            if char.isalpha():
                charright1 += 1
        for char in rightexp2:
            if char.isalpha():
                charright2 += 1
        if charright1 == 0 and charright2 == 0:
            if leftexp1 == leftexp2:
                finalexp = add(rightexp1, rightexp2)
                return leftexp1 + '^' + finalexp
            else:
                return num1 + '*' + num2
        else:
            return num1 + '*' + num2
    else:
        return num1 + '*' + num2

def divideraw(num1, num2):
    rnum1 = num1.replace('-', '')
    rnum2 = num2.replace('-', '')
    if rnum1.isdigit() and rnum2.isdigit():
        return str(int(num1) / int(num2))
    elif rnum1.replace(".", "").isdigit() and rnum2.replace(".", "").isdigit():
        return str(float(num1) / float(num2))
    elif rnum1.replace("/", "").isdigit() and rnum2.replace(".", "").isdigit():
        temp = num1.split('/')
        num1 = float(temp[0] / temp[1])
        return str(float(num1) / float(num2))
    elif rnum1.replace(".", "").isdigit() and rnum2.replace("/", "").isdigit():
        temp = num2.split('/')
        num2 = float(temp[0] / temp[1])
        return str(float(num1) / float(num2))
    elif rnum1.replace("/", "").isdigit() and rnum2.replace("/", "").isdigit():
        temp2 = num2.split('/')
        num = temp2[0]
        denom = temp2[1]
        num2 = denom+'/'+num
        multraw(num1, num2)

def exponentraw(num1, num2):
    rnum1 = num1.replace('-', '')
    rnum2 = num2.replace('-', '')
    if rnum1.isdigit() and rnum2.isdigit():
        return str(int(num1) ** int(num2))
    elif rnum1.replace(".", "").isdigit() and rnum2.replace(".", "").isdigit():
        return str(float(num1) ** float(num2))
    elif rnum1.replace("/", "").isdigit() and rnum2.replace(".", "").isdigit():
        temp = num1.split('/')
        num1 = float(temp[0] / temp[1])
        return str(float(num1) ** float(num2))
    elif rnum1.replace(".", "").isdigit() and rnum2.replace("/", "").isdigit():
        temp = num2.split('/')
        num2 = float(divideraw(temp[0], temp[1]))
        if num2 % 2 == 0:
            if not '-' in num2:
                num2 = float(temp[0] / temp[1])
                return '±'+str(float(num1) ** float(num2))
            else:
                num2 = num2.replace('-')
                temp = num2.split('/')
                num2 = float(temp[0] / temp[1])
                return '±' + str(float(num1) ** float(num2))+'i'
        else:
            return str(float(num1) ** float(num2))

    elif rnum1.replace("/", "").isdigit() and rnum2.replace("/", "").isdigit():
        temp1 = num1.split('/')
        temp2 = num2.split('/')
        num1 = float(temp1[0] / temp1[1])
        if num2 % 2 == 0:
            if not '-' in num2:
                num2 = float(temp[0] / temp[1])
                return '±'+str(float(num1) ** float(num2))
            else:
                num2 = num2.replace('-')
                temp = num2.split('/')
                num2 = float(temp[0] / temp[1])
                return '±' + str(float(num1) ** float(num2))+'i'
        else:
            return str(float(num1) ** float(num2))

def rawln(num):
    if '-' in num:
        return "You cannot take the natural log of a negative number!"
    elif num.isdigit():
        return str(math.log(int(num)))
    elif num.replace('.', '').isdigit():
        return str(math.log(float(num)))

sindictrad = {
    "0": "0",
    "pi/6": "1/2",
    "pi/4": "(sqrt(2))/2",
    "pi/3": "(sqrt(3))/2",
    "pi/2": "1",
    "2pi/3": "(sqrt(3))/2",
    "3pi/4": "(sqrt(2))/2",
    "5pi/6": "1/2",
    "pi": "0",
    "7pi/6": "-1/2",
    "5pi/4": "-(sqrt(2))/2",
    "4pi/3": "-(sqrt(3))/2",
    "3pi/2": "-1",
    "5pi/3": "-(sqrt(3))/2",
    "7pi/4": "-(sqrt(2))/2",
    "11pi/6": "-1/2",
    "2pi": "0"
}

sindictdeg = {
    "0": "0",
    "30": "1/2",
    "45": "(sqrt(2))/2",
    "60": "(sqrt(3))/2",
    "90": "1",
    "120": "(sqrt(3))/2",
    "135": "(sqrt(2))/2",
    "150": "1/2",
    "180": "0",
    "210": "-1/2",
    "225": "-(sqrt(2))/2",
    "240": "-(sqrt(3))/2",
    "270": "-1",
    "300": "-(sqrt(3))/2",
    "315": "-(sqrt(2))/2",
    "330": "-1/2",
    "360": "0"
}

cosdictrad = {
    "0": "1",
    "pi/6": "(sqrt(3))/2",
    "pi/4": "(sqrt(2))/2",
    "pi/3": "1/2",
    "pi/2": "0",
    "2pi/3": "-1/2",
    "3pi/4": "-(sqrt(2))/2",
    "5pi/6": "-(sqrt(3))/2",
    "pi": "-1",
    "7pi/6": "-(sqrt(3))/2",
    "5pi/4": "-(sqrt(2))/2",
    "4pi/3": "-1/2",
    "3pi/2": "0",
    "5pi/3": "1/2",
    "7pi/4": "(sqrt(2))/2",
    "11pi/6": "(sqrt(3))/2",
    "2pi": "1"
}

cosdictdeg = {
    "0": "1",
    "30": "(sqrt(3))/2",
    "45": "(sqrt(2))/2",
    "60": "1/2",
    "90": "0",
    "120": "-1/2",
    "135": "-(sqrt(2))/2",
    "150": "-(sqrt(3))/2",
    "180": "-1",
    "210": "-(sqrt(3))/2",
    "225": "-(sqrt(2))/2",
    "240": "-1/2",
    "270": "0",
    "300": "1/2",
    "315": "(sqrt(2))/2",
    "330": "(sqrt(3))/2",
    "360": "1"
}

tandictrad = {
    "0": "0",
    "pi/6": "(sqrt(3))/3",
    "pi/4": "1",
    "pi/3": "sqrt(3)",
    "pi/2": "Undefined",
    "2pi/3": "-sqrt(3)",
    "3pi/4": "-1",
    "5pi/6": "(-sqrt(3))/3",
    "pi": "0",
    "7pi/6": "(sqrt(3))/3",
    "5pi/4": "1",
    "4pi/3": "sqrt(3)",
    "3pi/2": "Undefined",
    "5pi/3": "-sqrt(3)",
    "7pi/4": "-1",
    "11pi/6": "(-sqrt(3))/3",
    "2pi": "0"
}

tandictdeg = {
    "0": "0",
    "30": "(sqrt(3))/3",
    "45": "1",
    "60": "sqrt(3)",
    "90": "Undefined",
    "120": "-sqrt(3)",
    "135": "-1",
    "150": "(-sqrt(3))/3",
    "180": "0",
    "210": "(sqrt(3))/3",
    "225": "1",
    "240": "sqrt(3)",
    "270": "Undefined",
    "300": "-sqrt(3)",
    "315": "-1",
    "330": "(-sqrt(3))/3",
    "360": "0"
}

arcsindictrad = {v: k for k, v in sindictrad.items()}
arccosdictrad = {v: k for k, v in cosdictrad.items()}
arctandictrad = {v: k for k, v in tandictrad.items()}
arcsindictdeg = {v: k for k, v in sindictdeg.items()}
arccosdictdeg = {v: k for k, v in cosdictdeg.items()}
arctandictdeg = {v: k for k, v in tandictdeg.items()}
def normaltrigrad(num):
    num = num.replace('pi', '')
    if num == '':
        num = '1'
    if num[1] == '/':
        num = num[0] + '1' + num[1:]
    if num[1] == '-':
        num = eval(num)
        num = 2 - num
    else:
        num = eval(num)
    while num > 2:
        num -= 2
    num = Fraction(num)
    num = str(num)
    temp = num.split('/')
    if temp[0] == '1':
        temp[0] = ''
    temp[0] = temp[0] + 'pi'
    if len(temp) > 1:
        temp[1] = '/' + temp[1]
    temp = "".join(temp)
    return temp

def normaltrigdeg(num):
    if num[0] == '-':
        num = eval(num)
        num = 360 - num
    else:
        num = eval(num)
    while num > 360:
        num -= 360
    return str(num)

def sinraw(num, type, resulttype):
    if resulttype == 'exact':
        if type == 'radians':
            num = normaltrigrad(num)
            answer = sindictrad.get(num)
            if answer:
                return answer
            else:
                return sinraw(num, 'radians', 'decimal')
        elif type == 'degrees':
            num = normaltrigdeg(num)
            answer = sindictdeg.get(num)
            if answer:
                return answer
            else:
                return sinraw(num, 'degrees', 'decimal')

    elif resulttype == 'decimal':
        if type == 'radians':
            num = num.replace('pi', '')
            if num[0] == '/':
                num = '1' + num
            num = eval(num)
            num = float(num)*math.pi
            num = math.sin(num)
            return str(num)
        elif type == 'degrees':
            num = math.sin(math.radians(float(num)))
            return str(num)

def cosraw(num, type, resulttype):
    if resulttype == 'exact':
        if type == 'radians':
            num = normaltrigrad(num)
            answer = cosdictrad.get(num)
            if answer:
                return answer
            else:
                return cosraw(num, 'radians', 'decimal')
        elif type == 'degrees':
            num = normaltrigdeg(num)
            answer = cosdictdeg.get(num)
            if answer:
                return answer
            else:
                return cosraw(num, 'degrees', 'decimal')

    elif resulttype == 'decimal':
        if type == 'radians':
            num = num.replace('pi', '')
            if num[0] == '/':
                num = '1' + num
            num = eval(num)
            num = float(num)*math.pi
            num = math.cos(num)
            return str(num)
        elif type == 'degrees':
            num = math.cos(math.radians(float(num)))
            return str(num)

def tanraw(num, type, resulttype):
    if resulttype == 'exact':
        if type == 'radians':
            num = normaltrigrad(num)
            answer = tandictrad.get(num)
            if answer:
                return answer
            else:
                return tanraw(num, 'radians', 'decimal')
        elif type == 'degrees':
            num = normaltrigdeg(num)
            answer = tandictdeg.get(num)
            if answer:
                return answer
            else:
                return tanraw(num, 'degrees', 'decimal')

    elif resulttype == 'decimal':
        if type == 'radians':
            num = num.replace('pi', '')
            if num[0] == '/':
                num = '1' + num
            num = eval(num)
            num = float(num)*math.pi
            num = math.tan(num)
            return str(num)
        elif type == 'degrees':
            num = math.tan(math.radians(float(num)))
            return str(num)

