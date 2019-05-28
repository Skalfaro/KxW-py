uni_list = []

with open('listaUni.txt', 'r') as lista_uni:
    for line in lista_uni:
        values = line.split(',')
        uni_list.append((values[0], values[1], values[2], values[3]))


class University:
    def __init__(self, name, city, region, number_of_students):
        self.name = name
        self.city = city
        self.region = region
        self.number_of_students = number_of_students


obj_list = []
n = 0

for line in uni_list:
    obj_uni = University(uni_list[n][0], uni_list[n][1], uni_list[n][2], uni_list[n][3])
    obj_list.append(obj_uni)
    n = n + 1


#location = input("search here: ")


#with open("listaUni.txt") as lista_uni:
    #if keyword.lower() in lista_uni.read().lower():
       # lista_uni.seek(0)
      #  for uni in lista_uni.readlines():
          # if keyword.lower() in uni.lower():
            #    print(uni)
  # else:
   #    print("there is not")


print(lista_uni)