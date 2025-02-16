# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:01:22 2021

@author: UAML
"""

#The example script is included below (and attached)

import numpy as n
import pylab as p
import scipy.integrate as integrate
import sympy as sm
#import matplotlib.pyplot as plt



def dx(x, y):
    return a*x-b*x*y

def dy(x, y):
    return -c*y+d*x*y

def derivs(state, t):
    """
    Map the state variable [rabbits, foxes] to the derivitives
    [deltar, deltaf] at time t
    """
    #print t, state
    x, y = state  # rabbits and foxes
    deltax = dx(x, y)  # change in rabbits
    deltay = dy(x, y) # change in foxes
    return deltax, deltay


a=1
b=0.1
c=0.1
d=0.01
#e=0.01


a/b

c/d

# the initial population of rabbits and foxes
x0 = 10
y0 = 12


t = n.arange(0.0, 100, 0.1)

z0 = [x0, y0]  # the initial [rabbits, foxes] state vector
y = integrate.odeint(derivs, z0, t)
x = y[:,0]  # extract the rabbits vector
y = y[:,1]  # extract the foxes vector


p.figure()
p.plot(t, x, label='Presas')
p.plot(t, y, label='Depredadores')
p.xlabel('Tiempo')
p.ylabel('Población')
p.title('Soluciones del modelo')
p.grid()
p.legend()
#p.savefig('lotka_volterra.png', dpi=150)
#p.savefig('lotka_volterra.eps')


p.figure()
p.plot(x,y)
p.xlabel('Presas')
p.ylabel('Depredadores')
p.title('Retrato fase')




x, y = sm.symbols('x, y')
P = a*x-b*x*y
Q = -c*y+d*x*y
# Set P(x,y)=0 and Q(x,y)=0.
Peqn = sm.Eq(P, 0)
Qeqn = sm.Eq(Q, 0)
criticalpoints = sm.solve((Peqn, Qeqn), x, y)
print(criticalpoints)



"""
p.figure()
p.plot(x,y)
p.xlim(0,120)
p.ylim(0,15)
p.xlabel('rabbits')
p.ylabel('foxes')
p.title('phase plane')
"""