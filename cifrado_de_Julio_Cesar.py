import string
minusculas=string.ascii_lowercase #Este es mi abecedario en minusculas
mayusculas=string.ascii_uppercase #Este es mi abecedario en Mayusculas
minusculas+="abc" #Agrego 'abc' a ambas para los casos de 'xyz'
mayusculas+="ABC"
texto=input("Ingresa el texto a cifrar: ")
cifrado=""
for letra in texto: #Paso por cada letra del texto a cifrar
    if letra in mayusculas: #Verifico que esté en algun conjunto de abecedarios
        letra_cifrada=mayusculas[mayusculas.index(letra)+3] #Le asigno a la letra original una nueva moviendo la letra 3 posociones usando indices
        cifrado+=letra_cifrada #Agrego la letra ya cifrada a la frase vacía 
    elif letra in minusculas:
        letra_cifrada=minusculas[minusculas.index(letra)+3]
        cifrado+=letra_cifrada
    else: #Este considera los caracteres dieferente a una letra
        cifrado+=letra
print(f"Este es el cifrado: {cifrado}")