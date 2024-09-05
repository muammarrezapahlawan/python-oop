
# membuat class 

class cat:
  
  # class attribute
  color = 'cokelat'

  # Instance attribute
  def __init__(self,name):
    self.name = name


# membuat object instance / intansiasi
cat1 = cat("kitty")
cat2= cat("melly")


# akses class attribute
print("Kitty berwarna {}".format(cat1.__class__.color))
print("Melly juga berwarna {} ".format(cat2.__class__.color))

# akses class instance
print("Nama dari kucing adalah {}".format(cat1.name))





