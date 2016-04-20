class Person:
    def __init__(self, age = 1, gen = "male"):
        super(SetSystem, self).__init__()
        self.age = age
        self.gen = "male"

    def get_age(self):
        return self.age

print Person(2).get_age()