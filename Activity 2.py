class Personal( object ):

    def __init__(self, name, idnumber):

        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee(Personal):

    def __init__(self, name, idnumber, salary, post):

        self.salary = salary
        self.post = post

        Personal.__init__(self, name, idnumber)

a = Employee("Viraaj", 8012234, 1076945107, "CEO")

a.display()
