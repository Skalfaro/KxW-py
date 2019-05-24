
keyword = input("search here: ")

with open("listaUni.txt") as lista_uni:
    if keyword.lower() in lista_uni.read().lower():
        lista_uni.seek(0)
        for uni in lista_uni.readlines():
            if keyword.lower() in uni.lower():
                print(uni)
    else:
       print("there is not")


lista_uni.close()