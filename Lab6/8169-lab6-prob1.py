class Teacher:

    def __init__(self, study, name, room, en, work):
        self.study = study
        self.name = name
        self.room = room
        self.en = en
        self.work = work


    def print_office_no(self):
        print(f"{self.study} has the office at {self.name}")

    
    def print_office_research_work(self):
        print(f"{self.study} is doing research in these topics  {self.room}')")  

    
    def print_courses_work(self):
        print(f"{self.study} teach these courses ('{self.en}', '{self.work}')")  

if  __name__ == '__main__':
    manee = Teacher("manee", "Rm, 4203", "Artificial Intelligence", "EN842004", "EN813701")
    mana = Teacher("mana", "Rm, 4203", "Internet of Things", "EN813703", "EN813701")
    manee.print_office_no()
    manee.print_office_research_work()
    manee.print_courses_work()
    mana.print_office_no()
    mana.print_office_research_work()
    mana.print_courses_work()

