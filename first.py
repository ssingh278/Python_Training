class Raman:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def use(self):
    print("Raman Caling...=",self.x+self.y)

class Sachin(Raman):
  def __init__(self,a,b):
    # super().__init__(500,500)
    self.a=a
    self.b=b
  def use(self):
    super().use()
    print("Sachin Caling...=",self.a+self.b)
    
S=Sachin(1000,1000)
S.use()