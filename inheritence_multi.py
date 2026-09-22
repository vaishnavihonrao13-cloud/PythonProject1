class Division:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def divide(self):
        return self.n / self.d


class Modulus:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def mod_divide(self):
        return self.n % self.d


class Div_Mod(Division, Modulus):
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def div_mod_both(self):
        divval = Division.divide(self)
        modval = Modulus.mod_divide(self)
        return (divval, modval)


x = Div_Mod(10, 3)
print('Division := ', x.divide())
print('Modulus and Division := ', x.div_mod_both())
print('Modulus ', x.mod_divide())