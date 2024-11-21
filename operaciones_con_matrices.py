import random

def escalarPorMatriz(numero, matriz): #PIDO UN NUMERO Y UNA MATRIZ
    resultado = []
    for fila in matriz: #'FILA' SON LAS LISTAS CREADAS CON 'GENERAR MATRIZ'
        nueva_fila = []
        # print(f"ESTA ES LA FILA: {fila}")
        for elemento in fila: #ELEMENTO TOMA LOS VALORES DE LOS ELEMENTOS EN LAS LISTAS(FILAS)
            # print(f"ESTE ES EL ELEMENTO: {elemento}")
            nueva_fila.append(numero * elemento) #A LA LISTA VACIA LE AGREGO EL RESULTADO DE LA OPERACION
        resultado.append(nueva_fila) #CREO MI MATRIZ(LISTA DE LISTAS)
    return resultado #REGRESO EL RESULTADO

def sumarMatrices(matriz_1, matriz_2):
    if len(matriz_1) != len(matriz_2) or len(matriz_1[0]) != len(matriz_2[0]): #VERIFICO QUE LAS LISTAS SEAN DEL MISMO TAMAÑO
        return "ERROR"
    resultado = [] 
    for i in range(len(matriz_1)): #I ENTRA A CADA SUBLISTA DE LA MATRIZ
        # print(f"ESTE ES I: {i}") #PRUEBA DE ESCRITORIO
        nueva_fila = [] #CREO UNA LISTA VACIA PARA LOS RESULTADOS DE CADA SUBLISTA DE LA MATRIZ
        for j in range(len(matriz_1[0])): #J ENTRA A CADA ELEMENTO DE CADA SUBLISTA DE LA MATRIZ (ESPECIFICAMENTE A CADA SUBLISTA A LA QUE ENTRA I)
            # print(f"ESTE ES J: {j}")
            nueva_fila.append(matriz_1[i][j] + matriz_2[i][j]) #AGREGO LOS RESULTADOS DE LAS OPERACIONES A UNA LISTA
        resultado.append(nueva_fila) #AGREGO CADA 'SUBLISTA' A LA LISTA 'PRINCIPAL' Y ASI CREAR UNA LISTA DE LISTAS
    return resultado

def productoMatricial(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2): 
        return "ERROR"
    resultado = []
    for i in range(len(matriz1)): #ENTRO A LAS SUBLISTAS DE LA MATRIZ 1
        # print(f"ESTE ES I: {i}") 
        nueva_fila = [] #CREO UNA LISTA VACIA PARA LOS RESULTADOS DE LAS OPERACIONES
        for j in range(len(matriz2[0])): #ENTRO A LOS 'ELEMENTOS' DE LA PRIMER SUBLISTA DE LA SEGUNDA MATRIZ
            # print(f"ESTE ES J: {j}")
            suma = 0 #CREO UN 'CONTADOR'
            for k in range(len(matriz2)): #ENTRO A CADA LISTA DE LA SEGUNDA MATRIZ
                # print(f"ESTA ES K: {k}")
                suma += matriz1[i][k] * matriz2[k][j] #A LA SUMA LE SUMO EL RESULTADO DE LA MULTIPLICACION 'UNO A UNO' ENTRE LOS ELEMTOS DE AMBAS MATRICES
            nueva_fila.append(suma) #AGREGO SUBLISTAS
        resultado.append(nueva_fila) #CREO UNA LISTA DE LISTAS
    # LO QUE SE ESPERA HACER CON LOS CICLOS 'FOR' ES INGRESAR A CADA ELEMENTO DE LA 'MATRIZ 1' Y COMPARARLO CON LOS 'ELEMENTOS' DE LAS 'SUBLISTAS' DE LA 'MATRIZ 2'
    return resultado

def generarMatriz(filas, columnas):
    matriz = []
    for _ in range(filas): #SOLO TOMO LA CANTIDAD DE SUBLISTAS A CREAR(POR ESO EL '-')
        # print(f"ESTE ES '_': ")
        fila = [] #CREO UNA CANTIDAD DE 'SUBLISTAS' DEPENDIENDO LAS FILAS
        for _ in range(columnas): #TOMO LA CANTIDAD DE 'NUMEROS' A METER EN CADAD SUBLISTA
            # print(f"ESTE ES '_': ")
            fila.append(random.randint(1, 10)) #CREO UNA CANTIDAD ALEATORIA DE NUMEROS ENTRE 1-10 Y LOS METO A CADA SUBLISTA
        matriz.append(fila) #CREO MI MATRIZ(LISTA DE LISTAS)
    return matriz

# PROCESAR LAS ENTRADAS: 
semilla = int(input("Introduce la semilla para el generador de números aleatorios: "))
random.seed(semilla)

# NUMERO DE OPERACIONES A HACER
num_operaciones = int(input("Introduce el número de operaciones: "))
resultados = [] #CREO UNA LISTA VACIA PARA AL FINAL AGREGAR LOS RESULTADOS (y así formar una lista de listas)

for _ in range(num_operaciones): #HACER 'N' VECES LAS OPERACIONES
    
    # MENU DE OPERACIONES:
    operacion = input("Introduce la operación\na. Escalar por matriz\nb. Sumar matrices\nc. Multiplicar matrices\n: ").lower()
    
    # CONDICIONALES DEPENDIENDO EL MENU:
    if operacion == "a":
        f, c = map(int, input("Introduce las dimensiones de la matriz (filas columnas): ").split()) #CONVIERTO LOS ELEMENTOS(DE LA LISTA) EN ENTEROS
        matriz = generarMatriz(f, c) #MANDO CREAR UNA MATRIZ ALEATORIA
        escalar = random.randint(1, 10) #CREO UN NUMERO ALEATORIO ENTRE 1-10
        print(f"ESTA ES LA MATRIZ ALEATORIA GENERADA: {matriz}") #PRUEBA DE ESCRITORIO
        print(f"ESTE ES EL NUMERO ALEATORIO: {escalar}") #PRUEBA DE ESCRITORIO
        resultado = escalarPorMatriz(escalar, matriz)
    elif operacion == "b":
        f1, c1, f2, c2 = map(int, input("Introduce las dimensiones de las matrices (f1 c1 f2 c2): ").split()) ##CONVIERTO LOS ELEMENTOS(DE LA LISTA) EN ENTEROS
        if f1 != f2 or c1 != c2:
            resultado = "ERROR"
        else:
            # GENERO DOS MATRICES PARA SUMARLAS ENTRE SI
            matriz1 = generarMatriz(f1, c1)
            matriz2 = generarMatriz(f2, c2)
            print(f"Matriz 1 generada: {matriz1}")
            print(f"Matriz 2 generada: {matriz2}")
            resultado = sumarMatrices(matriz1, matriz2)
    elif operacion == "c": #MISMA IDEA QUE CON LA ANTERIOR PERO AHORA LLAMANDO A LA MULTIPLICACION
        f1, c1, f2, c2 = map(int, input("Introduce las dimensiones de las matrices (f1 c1 f2 c2): ").split())
        if c1 != f2:
            resultado = "ERROR"
        else:
            matriz1 = generarMatriz(f1, c1)
            matriz2 = generarMatriz(f2, c2)
            print(f"Matriz 1 generada: {matriz1}")
            print(f"Matriz 2 generada: {matriz2}")
            resultado = productoMatricial(matriz1, matriz2)
    else:
        resultado = "ERROR"
    
    resultados.append(resultado) #AGREGO LOS RESULTADOS A LA LISTA VACIA DEL INICIO

# Imprimir resultados
for resultado in resultados:
    print(resultado)