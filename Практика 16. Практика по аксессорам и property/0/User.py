class User:
    def __init__(self, name, age):
        if not (isinstance(name, str) and name.isalpha()):
            raise ValueError("Некорректное имя")
        if not (isinstance(age, int) and (0 <= age <= 110)):
            raise ValueError("Некорректный возраст")
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Некорректное имя")
            
    @property
    def age(self):
        return self._age
            
    @age.setter        
    def age(self, new_age):
        if isinstance(new_age, int) and (0 <= new_age <= 110):
            self._age = new_age
        else:
            raise ValueError("Некорректный возраст")
        
    
user = User('Гвидо', 67) 
print(user.name) 
print(user.age) 

user.name = 'Тимур' 
user.age = 30
print(user.name) 
print(user.age)