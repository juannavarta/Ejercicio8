from classConjunto import Conjunto

if __name__ == "__main__":
    A = Conjunto([1,2,3,4])
    B = Conjunto([3,6,9])
    C = Conjunto([1,2,3,4])
    print(f"A = {A.getCon()}\nB = {B.getCon()}\nC = {C.getCon()}")
    AaddB = A + B
    print("La union A + B = {}".format(AaddB.getCon()))
    AsubB = A - B
    print("La diferencia A - B = {}".format(AsubB.getCon()))
    if A==C and C==A:
        print(f"Los conjuntos A y C son iguales, pues ambos contienen {A.getCon()}")