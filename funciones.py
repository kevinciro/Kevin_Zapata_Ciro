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
  
