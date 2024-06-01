class gustina:
    def __init__(self, povZemlje, BrStan):
        self.povZemlje=povZemlje
        self.BrStan=BrStan
    def IzracunajGustinu(self):
        return self.povZemlje/self.BrStan
gustina1 = gustina(100000,1584867)
gustina2 = gustina(2000,1056)
gustina3 = gustina(17567,67000)
print("Gustina prve zemlje je : ", gustina1.IzracunajGustinu())
print("Gustina druge zemlje je : ", gustina2.IzracunajGustinu())
print("Gustina trece zemlje je : ", gustina2.IzracunajGustinu())

