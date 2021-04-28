class MoComplex(complex):
    def module(self,typ=None):
        from decimal import Decimal
        m=Decimal((self.imag)**2+(self.real)**2)
        if not typ:
            return m.sqrt()
        else:
            return f"sqrt({(self.imag)**2}+{(self.real)**2})={m.sqrt()}"
    def fi(self):
        a =self.real
        b =self.imag
        retu=''
        if a>0:
            retu=f"arctg({b}/{a})"
        elif a<0 and b>=0:
            retu=f"arctg({b}/{a})+Pi"
        elif a<0 and b<0:
            retu=f"arctg({b}/{a})-Pi"
        elif a==0 and b>0:
            retu=f"Pi/2"
        elif a==0 and b<0:
            retu=f"-Pi/2"
        return retu
