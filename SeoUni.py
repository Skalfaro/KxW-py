keyword = input("search: ")

i = 0
if keyword.lower() in people:
    people.seek(0)
    for line in people.readlines():
        if keyword.lower() in people:
            print(line)
else:
    print("there is not")


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




print(lista_uni)