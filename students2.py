class Student:
    
    def __init__(self, name, year, department):
        self.name = name
        self.department = department
        self.year = year
        # self._call()
    
    # def _call(self):
    #     print(f"name: {self.name}, age: {self.year}, major: {self.department}")
    
    def __str__(self):
        return f"name: {self.name}, age: {self.year}, major: {self.department}"

Beken = Student("Esenamanov Beken", 14, "Computer Science")
Sam = Student("Sam Rogers", 25, "Ecology")

print(Beken)
print(Sam)