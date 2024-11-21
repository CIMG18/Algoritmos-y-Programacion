diccio={}
mensaje=input("MENSAJE: ")
menos=[',',':',';','!','?','.']
new=""
for caracter in mensaje:
    if caracter not in menos:
        new+=caracter
separados=new.split()
for i in separados:
    diccio[i]=diccio.get(i,0)+1
for palabra,cantidad in diccio.items():
    print(f"{palabra}: {cantidad}")