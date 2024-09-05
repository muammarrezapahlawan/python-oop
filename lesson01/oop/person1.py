
class Person:
  
  # class attribute
  usia=35


  # Instance attribute
  def __init__(self, name):
    self.name = name



# membuat object instance
person1 = Person("Reza")
person2 = Person("Dedi")


# akses dari instance attribute
print("nama person1 adalah {}".format(person1.name))
print("nama person2 adalah {}".format(person2.name))

# akses dari class attribute
print("Usia person1 adalah {}".format(person1.__class__.usia))






