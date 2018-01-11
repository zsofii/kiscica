class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return "{}+{}j".format(self.real, self.imaginary)

    def osszead(self, masik):
        return Complex(self.real + masik.real, self.imaginary + masik.imaginary)

    def kivon(self, masik):
        return Complex(self.real - masik.real, self.imaginary - masik.imaginary)

    def __add__(self, other):
        if isinstance(other, Complex):
            return self.osszead(other)
        elif isinstance(other, float) or isinstance(other, int):
            return Complex(self.real + other, self.imaginary)
        else:
            print("A második operandus nem szám!")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return self.kivon(other)
        elif isinstance(other, float) or isinstance(other, int):
            return Complex(self.real - other, self.imaginary)
        else:
            print("A második operandus nem szám!")


def main():
    elso = Complex(10, 10)
    masodik = Complex(0, 2)

    print(elso)
    print(masodik)
    harmadik = elso + masodik
    print(harmadik)
    negyedik = harmadik + 10
    print(negyedik)
    negyedik -= harmadik
    print(negyedik)


if __name__ == "__main__":
    main()
