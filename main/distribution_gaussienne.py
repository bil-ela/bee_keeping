import pylab
from math import sqrt
import numpy

pylab.clf()
pylab.grid

x=pylab.linspace(-4,4,1000)
f = lambda x:(1/sqrt(numpy.pi))*numpy.exp((-x**2))
g = lambda x:(-80/81)*x**2+(800/9)*x
h = lambda x:0.95*x
pylab.plot(x,f(x))
pylab.show()


def mal_baisse(nb):                     #En automne, les mâles meurent tous petit à petit
    mal=numpy.zeros(91);mal[0]=nb
    for i in range (90):
        mal[i+1] = int(0.95*mal[i])
    return mal

def inte_gauss_trap(f,a,b,n):
    h=(b-a)/n
    j=0
    for i in range (n):
        j=j+(f(a+(i+1)*h)+f(a+i*h))*h
        j=0.5*j
    return j

def inte_gauss_rect(f,a,b,n): 
    h=(b-a)/n
    j=0
    for i in range (n):
        j=j+f(a+i*h)*h
    return j

print(inte_gauss_rect(f,-3,3,7000))
        

print(inte_gauss_trap(f,-3,3,7000))

def calcg(x):
    for i in range (0,90):
        x = x + int(g(i))       #Combien d'abeilles pondu pendant le printemps en moyenne ? (réponse : 120000)
        
    return x
