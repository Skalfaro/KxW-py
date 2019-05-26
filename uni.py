class university:
    def __init__(self, name, region, city, faculty, number_of_students, prestige, is_public):
        self.name = name
        self.region = region
        self.city = city
        self.faculty = faculty
        self.number_of_students = number_of_students
        self.prestige = prestige
        self.is_public = is_public


uni1 = university("Università di Pavia", 'Lombardia', 'Pavia', ('medicina', 'ingegneria', 'giurisprudenza'), 22000, 1, True)

print(uni1.city)