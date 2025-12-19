import time
from datetime import datetime, timedelta


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
    def funkcja_dekorujaca(*args):
        print("To jest gorna czesc dekoratora przed wywolaniem udekorowanej funcji")
        start = time.time()
        result = funkcja_udekorowana(*args)
        print("To jest dolna czesc dekoratora.")
        end = time.time()
        print("Czas wykonania funkcji:", end - start, "sekund")
        return result
    return funkcja_dekorujaca

@dekorator_funkcja
def funkcja_udekorowana(a, b):
    print("----------------------------")
    print("To jest funkcja udekorowana.")
    print("----------------------------")

@dekorator_funkcja
def funkcja_udekorowana2():
    print("----------------------------")
    print("To jest funkcja udekorowana numer dwa.")
    print("----------------------------")
    return print(f"Gotowa za: {datetime.now() + timedelta(minutes=30)}")

funkcja_udekorowana(2, "w")
funkcja_udekorowana2()