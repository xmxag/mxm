class Student:
    def __init__(self, name, age, group, marks):
        self.__name = name
        self.__age = age
        self.__group = group
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def avg_marks(self, marks):
        avg = sum(marks)/len(marks)
        return avg

student1 = Student("Пупуня", 16,"ИС(ПРО)-31",[3,3,2,5])
print(student1.avg_marks(student1.get_marks()))
