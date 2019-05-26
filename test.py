class people:
    def __init__(self, name, job, location):
        self.name = p[0]
        self.job = p[1]
        self.location = p[3]

p =  []

with open('C:/Users/scalfarino/Desktop/exlist.txt', 'r') as f:
    for line in f:
        values = line.split(' ')
        p.append((values[0], values[1], values[2]))


print(p[1].job)