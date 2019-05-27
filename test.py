p = []

with open('C:/Users/scalfarino/Desktop/exlist.txt', 'r') as f:
    for line in f:
        values = line.split(' ')
        p.append((values[0], values[1], values[2]))


class person:
    def __init__(self, name, job, location):
        self.name = name
        self.job = job
        self.location = location

object_name_contenitor = []
i = 0
for line in p:
    obj = "object" + i.__str__()
    object_name_contenitor.append(obj)
    i = i + 1

people = []
n = 0
for line in p:
    content = person(p[n][0], p[n][1], p[n][2])
    people.append(content)
    n = n + 1

dictionary_obj = {
    object_name_contenitor[0]: people[0],
    object_name_contenitor[1]: people[1],
    object_name_contenitor[2]: people[2]

}


print(people[0].name)