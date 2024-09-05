
# class Person:
  

#   def __init__(self, nama, usia):
#     self.name = nama
#     self.age=usia

# orang1 = Person("Reza",35)


# print("Nama Orang pertama {} ".format(orang1.name))
# print("Usia Orang pertama {} ".format(orang1.age))


class Person:
  # class attribute 
  t_badan=170

  # constructor
  def __init__(self, nama, usia):
    self.nama=nama
    self.usia=usia

  def show(self):
    print("Nama {} ".format(self.nama))
    print("Usia {}".format(self.usia))


# membuat object instance
Orang1 = Person("Reza", 34)
Orang2 = Person("Yaya", 32)

# Output
# menggunakan function Show
Orang1.show()
print("memiliki tinggi badan {}".format(Orang1.__class__.t_badan))
Orang2.show()

print("Orang1 bernama", Orang1.nama) 
# or
print("Orang 1 Bernama {}".format(Orang1.nama))
# or
print("Orang 1 bernama " + Orang1.nama)




