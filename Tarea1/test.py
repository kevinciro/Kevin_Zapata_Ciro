import funciones

#el factorial de 5 es 120
print(funciones.Factorial(5))

# si se pasa un decimal (float) tira error
print(funciones.Factorial(0.3))

#el factor binomial de 4,2 es 6
print(funciones.Binomial(4,2))

#si se le pasa un float tira error
print(funciones.Binomial(4,2.))
