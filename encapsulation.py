class NTA:
    ceo_of_nigerian_prince='Dharemendra Pardhan'
    def __init__(self,name,rollno,life_status,sra):
        self.name=name
        self.rollno=rollno
        self.life_status=life_status
        self.__sra=sra
    @property
    def pinget(self):
        return self.__sra
    @pinget.setter
    def pinget(self, value):
        self.__sra=value
    
s1=NTA('Paresh',123456,'alive',56)
s1.pinget=120
print(s1.pinget)