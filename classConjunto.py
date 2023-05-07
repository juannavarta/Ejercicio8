class Conjunto:
    __con = []
    
    def __init__(self, lista=[]):
        self.__con = lista
    def getCon(self):
        return self.__con
    def __add__(self, otro):
        xConjunto = Conjunto(list(set(self.__con+otro.getCon())))
        return xConjunto
    def __sub__(self, otro):
        xConjunto = Conjunto([n for n in self.__con if n not in otro.getCon()])
        return xConjunto
    def __eq__(self, otro: object) -> bool:
        return self.__con == otro.getCon()