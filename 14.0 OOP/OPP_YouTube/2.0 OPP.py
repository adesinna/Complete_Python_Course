# Now we create a class and initialize attributes

class Health:
    discount = 0.86  # a 23% discount on health and this is a class attribute
    charge = 9000
    weight_pill_loss = 0.05
    weight_pill_gain = 1.05

    def __init__(self, name: str, age: int, weight: float, height: float):  # giving attributes and making sure of its data type
        # We can assert data type by using  assert keyword, and give the message it must display when it fails
        # Validations
        assert age >= 0,  f'age must be greater or equal to zero'
        assert weight >= 0,  f'weight must be greater or equal to zero'
        assert height >= 0, f'height must be greater or equal to zero'

        # Attributes

        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # Methods

    def calculate_bmi(self):
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    def calculate_weight(self):
        return self.weight

    def calculate_height(self):
        return self.height

    def apply_discount(self):
        return self.discount * self.charge  # using class variable to an object you need to use self

    def apply_weight_gain(self):
        self.weight = self.weight_pill_gain * self.weight

    def apply_weight_loss(self):
        self.weight = self.weight_pill_loss * self.weight


person1 = Health('adesina', 27, 78, 1.84)

# We can tap to the person attributes
# print(person1.name)
# print(person1.age)
# print(person1.height)
# print(person1.weight)
#

# Things we can do with this person(methods)

# print(person1.calculate_height())
# print(person1.calculate_weight())
# print(person1.calculate_bmi())
#
person2 = Health('busayo', 26, 85, 1.78)
#
# print(person2.age)

# Class attribute
# print(Health.discount)  # Class itself can access it
# print(person1.discount)   # objects can also access it
# print(person2.apply_discount())

# We can see all attributes of a class using __dict__

# print(person1.__dict__)
# print(Health.__dict__)
# print(person2.__dict__)

person1.apply_weight_gain()  # it changes all the time when you apply it
print(person1.__dict__)
person1.apply_weight_gain()
print(person1.weight)
person1.apply_weight_gain()
print(person1.__dict__)

# =======================================================
