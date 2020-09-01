#!/usr/bin/python3

import funciones

#la probabilidad de obtener 10 caras en 100 intentos
n=100
k=10
prob = funciones.Binomial(n,k)/ 2**(n)
print("La probabilidad de obtener 10 caras en 100 intentos es: ", prob)


#la probabilidad de obtener mas de 30 caras en 100 intentos
n=100
prob1=0
for k in range(30,101):
    prob1 = prob1 + ( funciones.Binomial(n,k)/(2**(n)) )
print("La probabilidad de obtener mas de 30 caras en 100 intentos es: ", prob1)
