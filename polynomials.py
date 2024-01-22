import simplifyraw
import re
from normalization import normalizeraw, unnormalizeraw, mathjax, simplified
import math

#Find quadratic roots

def quadraticroots(eq, var):
    spliteq = eq.split('+')
    Aterm = spliteq[0]
    Bterm = spliteq[1]
    Cterm = spliteq[2]
    Acoef = Aterm[:-3]
    Bcoef = Bterm[:-1]
    Ccoef = Cterm
    denom = Acoef + '*2'
    denom = simplifyraw.simplifyraw(denom)
    if Bcoef[0] == '-':
        Bcoef = '(' + Bcoef + ')'
    print("Use the quadratic formula")
    print(r"$" + var + r" = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$")
    print("Plug in the coefficients")
    print(r"$" + var + r" = \frac{-"+Bcoef+r"\pm \sqrt{"+Bcoef+r"^2-4("+Acoef+r")("+Ccoef+")}}{2("+Acoef+r")}$")
    print("Simplify the expression inside the square root first")
    inner = Bcoef+"^2-4("+Acoef+")("+Ccoef+")"
    inner = normalizeraw(inner)
    simplifiedinner = simplifyraw.simplifyraw(inner)
    simplifiedinner = unnormalizeraw(simplifiedinner)
    print(r"$" + var + r" = \frac{-" + Bcoef + r"\pm \sqrt{" + simplifiedinner + "}}{2(" + Acoef + r")}$")
    if simplifiedinner[0] == '-':
        print("Because it is negative, there will be imaginary roots")
        simplifiedinner = list(simplifiedinner)
        simplifiedinner.pop(0)
        simplifiedinner = "".join(simplifiedinner)
        print(r"$" + var + r" = \frac{-" + Bcoef + r"\pm \sqrt{-" + simplifiedinner + r"}}{"+denom+r"}$")
        simplifiedinner = simplifyraw.sqr_sim(int(simplifiedinner))
        if 'sqrt' in simplifiedinner:
            simplifiedinner = simplifiedinner.replace('sqrt', 'i\sqrt{')
        else:
            simplifiedinner = simplifiedinner+'i'
        print(r"$" + var + r" = \frac{-" + Bcoef + r"\pm " + mathjax(simplifiedinner) + r"}}{"+denom+r"}$")

        totalpos = '(-'+Bcoef + '+' + simplifiedinner +')/'+denom
        totalneg = '(-'+Bcoef + '-' + simplifiedinner +')/'+denom
    else:
        print(r"$" + var + r" = \frac{-" + Bcoef + r"\pm \sqrt{-" + simplifiedinner + r"}{2(" + Acoef + r")}$")
        simplifiedinner = simplifyraw.sqr_sim(int(simplifiedinner))
        print(r"$" + var + r" = \frac{-" + Bcoef + r"\pm " + mathjax(simplifiedinner) + r"}{2(" + Acoef + r")}$")


