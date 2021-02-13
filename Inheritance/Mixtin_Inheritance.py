from statistics import mean


class CalculateAverageMixing:
    def get_average(self, values):
        return mean(values)


class MathUtils:
    def get_average(self, value):
        return mean(value)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Students(Person, CalculateAverageMixing):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_average_grade(self):
        return MathUtils().get_average(self.grade)


class Employee(Person, CalculateAverageMixing):
    def __init__(self, name, age, daily_working_hours):
        super().__init__(name, age)
        self.daily_working_hours = daily_working_hours


st = Students('Pesho', 3, [2, 2, 3, 4, 6])
print(st.get_average(st.grade))
print(st.get_average_grade())