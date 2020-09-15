#!/usr/bin/python3

import math

class VectorCartesiano:
    #clase que da un vector en coordenadas cartesianas, necesita de la libreria math!
    
    def __init__(self, x, y, z):
        
        #se comprueba que las componentes sean flotantes, si son enteros se
        #convierten a flotantes
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            
            if type(x)==float and type(y)==float and type(z)==float:
                self.x = x
                self.y = y
                self.z = z
                
                #se define atributo de coordenadas para el indexado
                self.coordenadas = [x, y, z]
                
                #se define el atributo de magnitud 
                self.magnitud = pow(x**2 + y**2 + z**2, 0.5)
        

        #si se da otra entrada que no sea numerica aparecera el error
        except ValueError:
            return print("Ingrese solo numeros!")
            #pass
            
    def __mul__(self, other):
        #Sobrecarga de la multiplicacion
        return VectorCartesiano(self.x * other.x, self.y * other.y, self.z * other.z)
    
    
    def punto(self, other):
        #Producto punto en cartesianas
        
        """
        Decidi dividirlo por componentes para hcerlo mas legible
        pero en el return se puede poner la suma:
        VectorCartesiano.__mul__(self, other).x+VectorCartesiano.__mul__(self, other).y
        +VectorCartesiano.__mul__(self, other).z
        """
        puntox = VectorCartesiano.__mul__(self, other).x
        puntoy = VectorCartesiano.__mul__(self, other).y
        puntoz = VectorCartesiano.__mul__(self, other).z
        return puntox+puntoy+puntoz
    
    
    def cruz(self, other):
        #Produnto cruz en cartesianas
        
        """
        Decidi dividirlo por componentes para hcerlo mas legible
        pero en el return dentro del VectorCartesiano se pueden
        poner las componentes correspondientes
        """
        
        cruzx = (self.y*other.z) - (self.z*other.y)
        cruzy = -(self.x*other.z) + (self.z*other.x)
        cruzz = (self.x*other.y) - (self.y*other.x)
        return VectorCartesiano(cruzx, cruzy, cruzz)
    
    
    def __add__(self, other):
        #Sobrecarga de la suma
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
           
        
    def __sub__(self, other):        
        #Sobrecarga de la resta
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)
    
    
    def __getitem__(self, index):        
        #Sobrecarga del indexado, []
        return self.coordenadas[index]
    
    
    def __eq__(self, other):        
        #Sobrecarga de la comparacion
        return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y and self.z == other.z

    def Print(self):
        #Metodo para imprimir un vector
        print(f"[{self.x},{self.y},{self.z}]")
        
        
    def transf_esfericas(self):
        #Metodo para transformar componentes de un vector cartesiano
        #a las componentes de un vector en esfericas
        
        #se mira si la magnitud no es cero
        if self.magnitud!=0:
            r = self.magnitud
            theta = math.acos(self.z/r)
            
            #si x es diferente de cero se calcula normalmente
            if self.x!=0:
                phi = math.atan(self.y/self.x)
            
            #si x=0 estamos en el plano y-z o en el plano phi=pi/2
            else:
                phi = math.pi*0.5
       
        #si la magnitud es cero, todas sus componentes son cero 
        #aunque en principio solo es necesario que r=0 
        #y theta y phi pueden ser cualquier numero
        else:
            r=0
            theta=0
            phi=0
        
        return VectorCartesiano(r, theta, phi)
    
    
    def ang_entre(self, other):
        #Metodo para calcular el angulo entre dos vectores
        
        #si la magnitud de alguno de los dos es cero. el angulo se asumira como cero
        if self.magnitud==0 or other.magnitud==0:
            return 0
        
        #si la magnitud de ambos es diferente de cero, el angulo se calcula 
        #con el producto punto
        else:    
            return math.acos(VectorCartesiano.punto(self,other)/(self.magnitud*other.magnitud))

    def __del__(self):
        class_name = self.__class__.__name__
        #print (class_name, "destruido")


class VectorPolar(VectorCartesiano):
    #clase que da un vector en esfericas, necesita de la libreria math!
    
    def __init__(self, r, theta, phi):
        
        #se comprueba que los valores esten dentro de los rangos validos
        if r>=0 and theta>=0 and theta<=math.pi:
            
            self.r = r
            self.theta = theta
            self.phi = phi
            
            #Se heredan todos los atributos y metodos de la clase VectorCartesiano
            #pero con r,theta y phi como entradas
            #esto se hace ya que ambas bases son ortonormales y todos los metodos
            #estaran bien definidos para esta clase, excepto el de transformacion a esfericas
            #ya que este es un vector en esfericas!
            VectorCartesiano.__init__(self, self.r, self.theta, self.phi)
            
            #se cambian los atributos de x,y,z heredados de VectorCartesiano, para poner
            #en su lugar la transformacion de esfericas a cartesianas
            self.x = r*math.sin(theta)*math.cos(phi)
            self.y = r*math.sin(theta)*math.sin(phi)
            self.z = r*math.cos(theta)
            
            #se cambia la magnitud heredada de VectorCartesiano, ya que en esfericas este valor
            #es r
            self.magnitud = float(r)
            
        
        #si no estan en rangos validos se imprime el error.
        else: print("rangos malos")
            
            
    def transf_esfericas(self):
        #metodo para quitar el metodo heredado de VectorCartesiano
        return print('El vector ya esta en coordenadas esfericas')
            
            
    def transf_cartesianas(self):
        #Metodo de transformacion de esfericas a cartesianas
        return VectorCartesiano(self.x, self.y, self.z)
    
    
    def __del__(self):
        class_name = self.__class__.__name__
        #print (class_name, "destruido")

#if __name__ == "__main__":
    #print("Modulo new_func como script")
