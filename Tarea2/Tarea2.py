#!/usr/bin/python3

import vector

a = vector.VectorCartesiano(1.5, 0, 2.4)
b = vector.VectorCartesiano(0, 1, 9)
c = vector.VectorCartesiano(4.2, 0.05, 0)
apb = vector.VectorCartesiano.punto(a, b)
apc = vector.VectorCartesiano.punto(a, c)
bpc = vector.VectorCartesiano.punto(b, c)
acb = vector.VectorCartesiano.cruz(a, b)
acc = vector.VectorCartesiano.cruz(a, c)
bcc = vector.VectorCartesiano.cruz(b, c)

print("a en esfericas es:", end=" ")
a.transf_esfericas().Print()

print("b en esfericas es:", end=" ")
b.transf_esfericas().Print()

print("c en esfericas es:", end=" ")
c.transf_esfericas().Print()


print("El producto punto de a con b es: ", apb)
print("El producto punto de a con c es: ", apc)
print("El producto punto de b con c es: ", bpc)

print("El producto cruz de a con b es:", end=" " )
acb.Print()

print("El producto cruz de a con c es:", end=" " )
acc.Print()

print("El producto cruz de b con c es:", end=" " )
bcc.Print()

print("El angulo (en radianes) entre a y b es: ", a.ang_entre(b))
print("El angulo (en radianes) entre a y c es: ", a.ang_entre(c))
print("El angulo (en radianes) entre b y c es: ", b.ang_entre(c))
