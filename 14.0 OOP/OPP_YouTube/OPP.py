import csv


class Health:
    discount = 0.86  # a 23% discount on health and this is a class attribute
    charge = 9000
    weight_pill_loss = 0.05
    weight_pill_gain = 1.05
    all = []  # The all

    def __init__(self, name: str, age: int, weight: float, height: float):  # giving attributes and making sure of its data type
        # We can assert data type by using  assert keyword, and give the message it must display when it fails
        # Validations
        assert age >= 0,  f'age must be greater or equal to zero'
        assert weight >= 0,  f'weight must be greater or equal to zero'
        assert height >= 0, f'height must be greater or equal to zero'

        # Attributes

        self.__name = name   # __ makes sure it is a private attribute
        self.age = age
        self.weight = weight
        self.height = height

    # We need a list that will have all the record of objects created
        Health.all.append(self)  # append when created

    # Methods

    # To make sure name does not change
    @property
    def name(self):
        return self.__name  # this will make sure the name at the instance does not change

    # In case you want it to change by force
    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception('The new name is too long')
        else:
            self.__name = new_name

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

    @classmethod  # changing it to class method since there is no self to work with
    def instance_from_csv(cls):  # This only reads it into the class it is the 'all' that will print it
        with open('data.csv', 'r') as file:
            reader = csv.DictReader(file)  # make it dictionary
            persons = list(reader)

            for person in persons:
                Health(
                    name=person.get('name'),
                    age=int(person.get('age')),
                    weight=float(person.get('weight')),
                    height=float(person.get('height'))
                )

    @staticmethod  # Static method are class methods that generally do use any property of the class
    def is_child(age):  # takes it
        if age < 18:
            return True
        else:
            return False

    # to make it display well
    def __repr__(self):
        return f"Health('{self.name}', {self.age}, {self.weight}, {self.height})"

    # sometimes you do not want some attribute to change like
    @property
    def developer(self):
        return 'Developer: Aladesae Adesina'


# Health.instance_from_csv()  # This is a class method it loads the csv
# print(Health.all)
#
# print(Health.is_child(17))

# Class method helps to instantiate objects
# Static method to create utility functions without using any class item

