

# membuat class

class Person:
  usia1 = 35


 
  
# membuat object
person1 = Person()
person2 = Person()


person1.name="Reza"
person1.address="tanukila"

person2.name="Yaya"
person2.address="Balaikota"

print(person1)
print(person1.__dict__)



# cara akses 1
print(person2.name)
print(person2.address)

# cara akses 2
print("Nama dari person1 adalah {}".format(person1.name))
print("Nama dari person2 adalah {}".format(person2.name))


# cara akses class attribute 
print("Person 1 berusia {}".format(person1.__class__.usia1))
print("Person 2 berusia {}".format(person2.__class__.usia1))


