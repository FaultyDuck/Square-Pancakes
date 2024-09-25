class Person:
    name = '';
    age = 0;
    hobby = '';
    
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_hobby(self):
        return self.hobby
    
P1 = Person('Ryan', 18, 'Game')
P2 = Person('Sam', 19, 'Swim')
P3 = Person('James', 14, 'Ski')
print(P1.get_name(),P2.get_age(),P3.get_hobby())