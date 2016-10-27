# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:22:49 2016

@author: Sergej
"""

print(chr(27) + "[2J\n")
class solver:
    @staticmethod
    def f_cubic(x,a,b,c,d):
        return a*x**3 + b*x**2 + c*x + d
        
    @staticmethod
    def df_cubic(x,a,b,c):
        return 3*a*x**2 + 2*b*x + c
        
    @staticmethod
    def horner(x, *polynom):
        result = 0
        lsg = []
        for koeffizient in polynom:
            result = result * x + koeffizient
            lsg.append(result)
        return lsg

    @staticmethod
    def newton(functype,a,b,c,d,tol = 1e-09):
        if (functype == 'Cubic' or functype == 'cubic'):
            x = 1
            x_neu = x + x
            counter = 0
            while (abs(x_neu-x) > tol):
                counter +=1
                #print(counter,'.) f(',x,') = ',solver.f(x))
                x = x_neu 
                x_neu = x - solver.f_cubic(x,a,b,c,d)/solver.df_cubic(x,a,b,c)
            x1 = x_neu
            poly_new = solver.horner(x1,*(a,b,c,d))
            p = poly_new[1]/poly_new[0]
            q = poly_new[2]/poly_new[0]
            x2 = -p/2 + (p**2/4-q)**0.5
            x3 = -p/2 - (p**2/4-q)**0.5
            x = [x1,x2,x3]
            return x

