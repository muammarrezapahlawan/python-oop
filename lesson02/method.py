

class Player:
  pass

  def __init__(self, name, speed,totalAward ):
    self.name= name
    self.speed = speed
    self.totalAward = totalAward


  def getName(self):
    return self.name 
 
  def getSpeed(self):
    return self.speed
  
  def addAward(self, up):
    self.totalAward +=up
  

pemain1 = Player("Messi", 93, 40)
pemain1.addAward(15)
pemain2 = Player("Dybala", 86, 10)



print("Pemain dengan nama ", pemain1.getName() , " memiliki speed " , pemain1.getSpeed(), " dengan total award", pemain1.totalAward)

print("Pemain dengan nama ",  pemain2.getName() , " memiliki speed " , pemain2.getSpeed())
