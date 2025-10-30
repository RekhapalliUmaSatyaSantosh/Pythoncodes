class a:
    def __init__(self,s1):
        self.s1=s1
        # self.s2=s2
    def __iadd__(self,other):
        other.s1 -= self.s1
        return other.s1
o2=a(21)
o3=a(3)
o2+=o3
print(o2)