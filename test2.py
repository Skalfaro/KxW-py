p = []

with open('C:/Users/scalfarino/Desktop/shortunilist.txt', 'r') as f:
    for line in f:
        values = line.split('-')
        p.append((values[0], values[1], values[2], values[3]))


class university:
    def __init__(self, name, city, region, number_of_students):
        self.name = name
        self.city = city
        self.region = region
        self.number_of_students = number_of_students

objects_uni = []
n = 0
for line in p:
    obj = university(p[n][0], p[n][1], p[n][2], p[n][3])
    objects_uni.append(obj)
    n = n + 1

i = 0
keyword = input("insert city here: ")
for line in p:
    if objects_uni[i].city == keyword:
        print(p[i])
        i = i + 1
    else:
        i = i + 1


