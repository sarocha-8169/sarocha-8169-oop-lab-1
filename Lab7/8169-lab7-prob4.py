class ComEnStudent:
    def __init__(self, name):
        self.name = name

    def take_courses(self):
        return "has taken these courses:"

    def make_content_type(self):
        return "has taken these courses:"

    def __str__(self):
        return self.name


class CoEStudent(ComEnStudent):
    def __init__(self, com):
        super().__init__("Manee")
        self.com = com

    def take_courses(self):
        return self.com

    def make_content_type(self):
        return "specialized in creating content type:"


class DMEStudent(ComEnStudent):
    def __init__(self, dme):
        super().__init__("Mana")
        self.dme = dme


if __name__ == "__main__":
    com_student =[]
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_student.append(manee)
    com_student.append(mana)
    for com_students in com_student:
        com_students.take_courses("SC401206")
        print(com_students)
