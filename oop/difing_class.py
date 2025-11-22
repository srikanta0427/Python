class Animal:
    age = 0
    def __init__(self,name,age): # constructor 
        self.name = name
        self.age = age

    def nm(self,color):
        print(self.name+" Color: "+color.title())

dog = Animal("Dog",6)
dog.nm("red")
print(dog.age)
