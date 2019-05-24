
lista_uni = open("C:/Users/scalfarino/Desktop/listaUni.txt", "r")
keyword = input("search here: ")


for uni in lista_uni.readlines():
    if keyword.lower() in uni.lower():
        print(uni)


lista_uni.close()