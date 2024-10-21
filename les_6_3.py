class Human:

    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Privet, mena zovut {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} u4itsa v gruppe {self.group}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        # self.name = name
        # Human.__init__(self, name)
        super().__init__(name, group)  # super() == Human.
        self.place = place
        super().info()


# human = Human('Den')
# print(human.name)
student = Student('Max', 'Urban', 'Pyton 1')
print(Student.mro())  # Цепочка наследований
