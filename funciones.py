#!/usr/bin/python3

def Factorial( a ):
    # Funcion para calcular el factorial de un entero a dado
    
    #El valor debe ser un entero positivo o cero
    if a>=0 and type(a)==int :
        
        n = 1 #Variable "muda" para guardar en valor del factorial
    
        #ciclo para calcular el factorial
        for i in range(1, a+1):
            #cada iteracion se le suma 1 a i, empieza en 1, y se multiplica por el valor anterior de n
            n = n*i
        return n
    
    #si no es positivo
    else:
        return print("Ingrese solo enteros mayores o igales a cero")
  


def Binomial( n, k ):
    #funcion para calcular el coeficiente binomial dados n y k
    
    #verificar que n sea mayor o o igual que k y que ambos sean enteros
    if n>=k and type(n)==int and type(k)==int:
        
        try:
            #se usa la formula 1.1 para calcular el coeficiente binomial, b
            return Factorial(n)/( Factorial(k)*Factorial(n-k) )
        
        except:
            return
        
    # si n no es mayor o o igual que k o alguno no es entero
    else:
        return print("Asegurese que n sea mayor o igual que k y que ambos sean enteros")  
  


def Pascal(n):
    #funcion para graficar un triangulo de pascal hasta el n-esimo termino empezando desde cero
    
    
    archivo = open("pascal-n.txt", "w")
    
    #se verifica que el numero sea entero y mayor que cero
    if type(n)==int and n>=0:
        
        #primer ciclo para las filas (las n)
        for i in range(0, n+1):
            
            #se imprimen un numero de espacios que van disminuyendo en cada fila
            #se empieza con n+1 espacios, se van disminuyendo en i cada iteracion
            #no se hace salto de linea
            espacios = " ".center(3*(n-i+1))
            archivo.write(espacios)
            
            #segundo ciclo para las columnas (numeros dentro de cada fila)
            for j in range(0, i+1):
                
                #se imprime en la misma linea los coeficientes binomiales asociados a la fila
                #estos se centran dependiendo del numero de digitos presentes en los numeros mayores
                #no se hace salto de linea
                coeficientes = str(Binomial(i,j)).center(6)
                archivo.write(coeficientes)
            
            #se imprime la fila y se hace el salto de linea
            numero = str(i)
            archivo.write("n = ")
            archivo.write(numero)
            archivo.write("\n")
        
        archivo.close()
            
        return
    
    #si no es mayor entero o no es mayor que cero
    else:
        return print("Ingrese un numero entero mayor o igual a cero")

    
    
if __name__ == "__main__":
    print("Módulo funciones como script")
