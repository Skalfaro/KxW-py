
lista_uni = open("C:/Users/scalfarino/Desktop/listaUni.txt", "r")
keyword = input("search here: ")


for uni in lista_uni.readlines():
    if keyword in uni:
        print(uni)

lista_uni.close()