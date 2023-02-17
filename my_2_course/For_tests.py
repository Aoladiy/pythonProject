class Person:
    __allowed_characters = ["абвгдеёжзийклмнопрстуфхцчшщъыьэюя- "][0].lower()
    __allowed_characters += __allowed_characters.upper()

    def __init__(self, full_name, age, passport_data, weight):
        # self.full_name_validator(full_name)
        # self.age_validator(age)                           не нужны за присутствием методов @property
        # self.passport_validator(passport_data)
        # self.weight_validator(weight)
        self.full_name = full_name
        self.age = age
        self.passport_data = passport_data
        self.weight = weight

    @classmethod
    def full_name_validator(cls, full_name):
        if len(full_name.split()) != 3 or type(full_name) != str:
            raise TypeError("неверно введено фио")
        for element in full_name.split():
            for symbol in element:
                if symbol in cls.__allowed_characters:
                    element = element.replace(symbol, '')
            if len(element) != 0:
                raise TypeError("неверно введено фио >>> " + "\"" + element + "\"" + " в " + full_name)

    @classmethod
    def age_validator(cls, age):
        if type(age) != int or age > 120 or age < 14:
            raise TypeError("неверно введён возраст")

    @classmethod
    def passport_validator(cls, passport_data):
        if type(passport_data) != str or len(passport_data.split()) != 2:
            raise TypeError("неверно введены паспортные данные")
        elif len(passport_data.split()[0]) != 4 or len(passport_data.split()[1]) != 6:
            raise TypeError("неверно введены паспортные данные")
        elif not (passport_data.split()[0].isdigit() and passport_data.split()[1].isdigit()):
            raise TypeError("неверно введены паспортные данные")

    @classmethod
    def weight_validator(cls, weight):
        if type(weight) not in (float, int) or weight < 20:
            raise TypeError("неверно введён вес")

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.full_name_validator(full_name)
        self.__full_name = full_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.age_validator(age)
        self.__age = age

    @property
    def passport_data(self):
        return self.__passport_data

    @passport_data.setter
    def passport_data(self, passport_data):
        self.passport_validator(passport_data)
        self.__passport_data = passport_data

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.weight_validator(weight)
        self.__weight = weight


person = Person("Очиров Алдар Александрович", 19, "1234 567890", 62.2)
print(person.age)
