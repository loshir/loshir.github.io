class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        # This method should return a string like "Hi, I'm John and I'm 25 years old"
        # Your code here
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        # Increase age by 1 and wish happy birthday
        self.age += 1
        return f"Congratulations on surviving last year! You are now {self.age} years old!!!"
    
    def is_adult(self):
        return self.age >= 18
    def older_than(self, other_person):
        return self.age > other_person.age
            

person1 = Person("Tazzles", 39)
person2 = Person("Lexi", 32)
print(person1.introduce())
print(person1.have_birthday())
print(person1.is_adult())

print(person1.older_than(person2))
