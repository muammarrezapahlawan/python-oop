
class Pc:
  
  # class variabel / attribute
  jumlah=0
  
  def __init__(self, inputName, inputBB):
    # instance attribute / instance variabel
    self.name = inputName
    self.bb = inputBB
    Pc.jumlah +=1    
    print("membuat object dengan nama " + inputName)
  

pc1 = Pc("Reza", 60)
print(Pc.jumlah)
pc2 = Pc("xx", 177)
print(Pc.jumlah)




