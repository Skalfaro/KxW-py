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


people = []
n = 0
for line in p:
    content = person(p[n][0], p[n][1], p[n][2])
    people.append(content)
    n = n + 1




i = 0
for line in p:
    if people[i].name == "erika":
        print(p[i])
        i = i + 1
    else:
        i = i + 1