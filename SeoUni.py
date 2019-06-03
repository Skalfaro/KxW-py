p = []

with open('C:/Users/scalfarino/Desktop/ListaUni.txt', 'r') as f:
    for line in f:
        values = line.split('-')
        p.append((values[0], values[1], values[2], values[3]))


class University:
    def __init__(self, name, city, region, number_of_students):
        self.name = name
        self.city = city
        self.region = region
        self.number_of_students = number_of_students


objects_uni = []
n = 0
for line in p:
    obj = University(p[n][0], p[n][1], p[n][2], p[n][3])
    objects_uni.append(obj)
    n = n + 1

i = 0
key_region = input("insert region here: ").lower()
key_city = input("insert city here: ").lower()
other_cities = []
key_valid = False


for line in p:
    if key_city == objects_uni[i].city.lower() and key_region == objects_uni[i].region.lower():
        key_valid = True
        if i < (len(p) - 1):
            print(p[i])
            i += 1
        else:
            print(p[i])
            print(other_cities)
    elif key_region == objects_uni[i].region.lower() and key_city != objects_uni[i].city.lower():
        key_valid = True
        if i < (len(p) - 1):
            if objects_uni[i].city in other_cities:
                i += 1
            else:
                other_cities.append(objects_uni[i].city)
                i += 1
        else:
            if objects_uni[i].city in other_cities:
                i += 1
                print(other_cities)
            else:
                other_cities.append(objects_uni[i].city)
                i += 1
                print(other_cities)
    else:
        if i < (len(p) - 1):
            i += 1
        else:
            if not key_valid:
                print("invalid region")
            else:
                print(other_cities)
