# l=[10,20]
# m=[30,40]
# print(*l,*m)

# d1={1:'A',2:'B'}
# d2={3:'C',4:'D'}
# d={**d1,**d2}
# print(d)

# d1={1,'A',2,'B'}
# d2={3,'C',4,'D'}
# d={*d1,*d2}
# print(d)

d={
    'cars':('Innova','audi','benz'),
    'mobiles':('samsung','realme','moto')
}
print(d['cars'][2])
print(d['mobiles'])
print(d.get('cars'))