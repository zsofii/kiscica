class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return ""

    def __add__(self, other):
        if isinstance(other, complex):
            print("other is complex")
        else:
            print("other is not complex")
        # TODO: leellenőrizni, hogy az 'other' csak valós vagy egy másik complex szám lehessen
        # valós: type(other) == float
   # def __sub__(self,other):

    # TODO: megírni a kivonás függvényt
def main():
    elso = Complex(10, 10)
    masodik = Complex(0, 2)

    print(elso)
    print(masodik)
    harmadik = elso + masodik
    print(harmadik)

def kivonas():
    a_szam=Complex(5,5)
    b_szam=Complex(0,1)
    c_szam=a_szam-b_szam
    print (c_szam)



if __name__ == "__main__":
    main()
