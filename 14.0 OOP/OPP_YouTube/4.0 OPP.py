# Suppose you want a class that have insurance

from OPP import Health


class Insurance(Health):
    def __init__(self, insure: bool, name, age, height, weight):  # this takes all the initial attributes
        super().__init__(name, age, height, weight)  # repeat the attributes is will inherit here
        self.insure = insure

    def is_insured(self):
        if self.insure:
            Health.discount = 0.5
            return True


segun = Insurance(True, age=17, name='segun', weight=88, height=1.77)

print(segun.is_insured())
print(segun.is_child(17))
print(segun.discount)
print(segun.developer)  # will make sure it is constant
segun.name = 'adesina'

print(segun.name)
