#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

class Oscilador:
    #clase oscilador armonico simple toma como entrada la amplitud, frecuencia natural, desface y tiempo
    #con algunos metodos que permiten ver graficas directamente
    def __init__(self, A, w_0, d, t):
        self.amplitud = A
        self.frecuencia_natural = w_0
        self.desface = d
        self.tiempo = t
        
        #la posicion y la velocidad los defini como atributos de clase usando las ecuaciones dadas en el pdf.
        self.posicion = self.amplitud*np.cos(self.frecuencia_natural*self.tiempo + self.desface)
        self.velocidad =  -self.amplitud*self.frecuencia_natural*np.sin(self.frecuencia_natural*self.tiempo + self.desface)
    
    def pos_vs_t(self):
        #metodo para graficar directamente un oscilador, para la tarea no sirve mucho porque los piden juntos
        plt.plot(t, self.posicion)
        plt.ylabel("posicion (m)")
        plt.xlabel("tiempo (s)")
        plt.title("posicion vs t")
        plt.grid()
        return plt.show()
    
    
    def esp_fase(self):
        #metodo para graficar el espacio de fase de un oscilador
        plt.plot(self.posicion, self.velocidad)
        plt.xlabel("posicion (m)")
        plt.ylabel("velocidad (m/s)")
        plt.title("Espacio de fase")
        plt.grid()
        return plt.show()


class OsciladorForzado(Oscilador):
    #Clase oscilador forzado, recibe los parametros de amplitud, frecuencia (del forzado subamortiguado)
    #el desface, el tiempo, y el parametro gamma que es la disipacion
    #como hereda los metodos de la clase oscilador puede entregar las graficas de pos vs t y espacio de fase directamente
    #aunque estos metodos de graficacion que le puse no los use en la solucion de la tarea
    def __init__(self, c, w, d, t, gamma):
        self.gamma = gamma
        
        #se hereda la clase oscilador para hacer uso de sus atributos de velocidad y posicion
        #en el pdf se ve que estos sirven para calcular la velocidad y posicion de un subamortiguado
        Oscilador.__init__(self, c, w, d, t)
        self.posicion = np.exp(-gamma*0.5*t)*self.posicion
        self.velocidad = np.exp(-gamma*0.5*t)*self.velocidad - (gamma*0.5)*self.posicion
        
        #agrego algunos atrubitos
        self.amplitud_forz = c
        self.frec_forz = w
        self.coef_fric = gamma
