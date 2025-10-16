class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        
    @property
    def name(self):
        return self._name   
        
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def surname(self):
        return self._surname   
    
    @surname.setter
    def surname(self, value):
        self._surname = value
        
    @property
    def fullname(self):
        return f"{self._name} {self._surname}"
    
    @fullname.setter
    def fullname(self, value=str):
        self._name, self._surname = value.split(' ', 1)
        
        
# Input 1
"""person = Person('Меган', 'Фокс') 
print(person.name) 
print(person.surname) 
print(person.fullname)

# Input 2
person = Person('Меган', 'Фокс') 
person.name = 'Стефани' 
print(person.fullname) 
print(person.name)"""

# Input 3
"""person = Person('Алан', 'Тьюринг') 
person.surname = 'Вирт' 
print(person.fullname) """

# Input 4
person = Person('Джон', 'Маккарти') 
person.fullname = 'Алан Тьюринг' 
print(person.name) 
print(person.surname) 
print(person.fullname)