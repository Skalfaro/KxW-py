p = []

with open('C:/Users/scalfarino/Desktop/listaUni.txt', 'r') as lista_uni:
    for line in lista_uni.readlines():
        p.append(line)



print(p)