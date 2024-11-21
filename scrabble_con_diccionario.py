valores={"aeilnorstu":1,
        "dg":2,
        "bcmp":3,
        "fhwy":4,
        "k":5,
        "jx":8,
        "qz":10} 
cont=0
veces=int(input("NUMERO DE PALABRAS A PROCESAR: "))
for n in range(veces):
    x=input("PALABRA/S: ")
    mensaje=x.lower() 
    for e in valores.keys():
        for i in mensaje:
            if i in e:
                cont+=valores[e]
    print(cont)
    cont=0