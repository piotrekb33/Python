import time

a=lambda x, s: [x + s, x,s]
print(a(2, 3))
print(a(2, 3)[0])
# x tablica y zmienna jako podfunkcja lambda
def mnozenie3(x, y):
    y_0 = y(x[0])
    y_1 = y(x[1])
    return [y_0, y_1]

z = mnozenie3([2,3], lambda x: x*x*x)
print(z)


# dekoratory
print("--------------------Ponizej sa dekoratoty -------------------------------")
print("-------------------------------------------------------------------------")

def dekorator_funkcja(funkcja_udekorowana):
    def funkcja_dekorujaca():
        print("To jest gorna czesc dekoratora przed wywolaniem udekorowanej funcji")
        start = time.time()
        funkcja_udekorowana()
        print("To jest dolna czesc dekoratora.")
        end = time.time()
        print("Czas wykonania funkcji:", end - start, "sekund")
    return funkcja_dekorujaca

@dekorator_funkcja
def funkcja_udekorowana():
    print("----------------------------")
    print("To jest funkcja udekorowana.")
    print("----------------------------")

@dekorator_funkcja
def funkcja_udekorowana2():
    print("----------------------------")
    print("To jest funkcja udekorowana numer dwa.")
    print("----------------------------")

funkcja_udekorowana()
funkcja_udekorowana2()