#!/usr/bin/python3

import MasaResorte as mr
import numpy as np
import matplotlib.pyplot as plt

#el rango de tiempo a usar
t = np.linspace(0,20,100)

#los 5 MAS
oscilador1=mr.Oscilador(1,1,0,t)
oscilador2=mr.Oscilador(2,1,0,t)
oscilador3=mr.Oscilador(1,2,0,t)
oscilador4=mr.Oscilador(1,1,np.pi,t)
oscilador5=mr.Oscilador(0.5,1,0,t)
oscilador6=mr.Oscilador(0,0,0,t)

#los 5 subamortiguados, me equivoque y les puse forzados
forzado1=mr.OsciladorForzado(1,1,0,t, 0.3)
forzado2=mr.OsciladorForzado(2,1,0,t, 0.3)
forzado3=mr.OsciladorForzado(1,2,0,t, 0.3)
forzado4=mr.OsciladorForzado(1,1,np.pi,t, 0.1)
forzado5=mr.OsciladorForzado(0.5,1,0,t, 0.3)

#se hace la imagen de la posicion vs t de los 5 MAS y se guarda con nombre
#punto1a.png
fig, ax = plt.subplots(figsize=(11,9))
plt.plot(t,oscilador1.posicion, label="base", linewidth=3)
plt.plot(t,oscilador2.posicion, label="amp. doble", marker=".")
plt.plot(t,oscilador3.posicion, label="frec. doble", marker="+")
plt.plot(t,oscilador4.posicion, label="des. pi", marker="o")
plt.plot(t,oscilador5.posicion, label="amp. mitad", marker="*")
plt.legend()
plt.grid()
plt.xlabel("tiempo(s)")
plt.ylabel("posicion(m)")
plt.title("posicion vs t",size=20)
plt.xlim(0,20)
plt.savefig("punto1a.png")

#se hace la imagen del espacio de fase de los 5 MAS y se guarda con nombre
#punto1b.png
fig, ax = plt.subplots(figsize=(11,9))
plt.plot(oscilador1.posicion, oscilador1.velocidad, label="base", linewidth=5)
plt.plot(oscilador2.posicion, oscilador2.velocidad, label="amp. doble", marker=".")
plt.plot(oscilador3.posicion, oscilador3.velocidad, label="frec. doble", marker="+")
plt.plot(oscilador4.posicion, oscilador4.velocidad, label="des. pi", marker="o")
plt.plot(oscilador5.posicion, oscilador5.velocidad, label="amp. mitad", marker="*")
plt.legend()
plt.grid()
plt.xlabel("posicion(m)")
plt.ylabel("velocidad(m/s)")
plt.title("Espacio de fase", size=20)
plt.savefig("punto1b.png")

#se hace la imagen de la posicion vs t de los 5 subamortiguados y se guarda con nombre
#punto2a.png
fig, ax = plt.subplots(figsize=(11,9))
plt.plot(t,forzado1.posicion, label="base", linewidth=3)
plt.plot(t,forzado2.posicion, label="amp.doble", marker=".")
plt.plot(t,forzado3.posicion, label="frec.doble", marker="+")
plt.plot(t,forzado4.posicion, label="des.pi, menor disi. ", marker="o")
plt.plot(t,forzado5.posicion, label="amp.mitad", marker="*")
plt.legend()
plt.grid()
plt.xlabel("tiempo(s)")
plt.ylabel("posicion(m)")
plt.title("posicion vs t",size=20)
plt.xlim(0,20)
plt.savefig("punto2a.png")

#se hace la imagen del esacio de fase de los subamortiguados y se guarda con nombre
#punto2b.png
fig, ax = plt.subplots(figsize=(11,9))
plt.plot(forzado1.posicion, forzado1.velocidad, label="base", linewidth=5)
plt.plot(forzado2.posicion, forzado2.velocidad, label="amp. doble", marker=".")
plt.plot(forzado3.posicion, forzado3.velocidad, label="frec. doble", marker="+")
plt.plot(forzado4.posicion, forzado4.velocidad, label="des. pi", marker="o")
plt.plot(forzado5.posicion, forzado5.velocidad, label="amp. mitad", marker="*")
plt.legend()
plt.grid()
plt.xlabel("posicion(m)")
plt.ylabel("velocidad(m/s)")
plt.title("Espacio de fase", size=20)
plt.savefig("punto2b.png")
