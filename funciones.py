def Factorial( int ):
    # Funcion para calcular el factorial de un entero dado
    
    n = 1 #Variable "muda" para guardar en valor del factorial
    
    #ciclo para calcular el factorial
    for i in range(1, int+1):
        #cada iteracion se le suma 1 a i, empieza en 1, y se multiplica por el valor anterior de n
        n = n*i
        
    return n
  
  
  
