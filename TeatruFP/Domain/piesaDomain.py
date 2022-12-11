class Piesa:
    def __init__(self):
        self.__titlu = ""
        self.__regizor = ""
        self.__gen = ""
        self.__durata = -1

    def __eq__(self, other):
        if(self.__titlu == other.get_titlu() and self.__regizor == other.get_regizor() and self.__gen == other.get_gen() and self.__durata == other.get_durata()):
            return True
        return False

    def __str__(self):
        return "TITLU: " + self.__titlu + "\n" + "REGIZOR: " + self.__regizor + "\n" + "GEN: " + self.__gen + "\n" + "DURATA: " + str(self.__durata) + "\n"

    def get_titlu(self):
        return self.__titlu

    def get_regizor(self):
        return self.__regizor

    def get_gen(self):
        return self.__gen

    def get_durata(self):
        return self.__durata

    def set_titlu(self, titlu):
        self.__titlu = titlu

    def set_regizor(self, regizor):
        self.__regizor = regizor

    def set_gen(self, gen):
        self.__gen = gen

    def set_durata(self, durata):
        self.__durata = durata
