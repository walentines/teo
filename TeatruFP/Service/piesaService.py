from Repository.peisaRepository import PiesaRepo
from Validate.validators import *

class piesaService:
    def __init__(self):
        self.__piese = PiesaRepo("/Users/valentinserban/PycharmProjects/TeatruFP/Data/piese_de_teatru.txt")

    def adauga_piesa(self, titlu, regizor, gen, durata):
        erori = list()
        if(not validate_title(titlu)):
            erori.append("Titlul trebuie sa contina cel putin 2 caractere")
        if(not validate_regizor(regizor)):
            erori.append("Numele regizorului trebuie sa contina cel putin 2 caractere")
        if(not validate_gen(gen)):
            erori.append("Genul trebuie sa fie unul dintre urmatoarele: Comedie, Drama, Satira, Altele")
        if(not validate_durata(durata)):
            erori.append("Durata trebuie sa fie intreg pozitiv")
        if(len(erori) > 0):
            for eroare in erori:
                print(eroare)
            return
        durata = int(durata)
        self.__piese.adauga_piesa(titlu, regizor, gen, durata)

    def modificare_piesa(self, titlu, regizor, gen_nou, durata_noua):
        erori = list()
        if (not validate_title(titlu)):
            erori.append("Titlul trebuie sa contina cel putin 2 caractere")
        if (not validate_regizor(regizor)):
            erori.append("Numele regizorului trebuie sa contina cel putin 2 caractere")
        if (not validate_gen(gen_nou)):
            erori.append("Genul trebuie sa fie unul dintre urmatoarele: Comedie, Drama, Satira, Altele")
        if (not validate_durata(durata_noua)):
            erori.append("Durata trebuie sa fie intreg pozitiv")
        if (len(erori) > 0):
            for eroare in erori:
                print(eroare)
            return
        durata_noua = int(durata_noua)
        self.__piese.modificare_piesa(titlu, regizor, gen_nou, durata_noua)

    def get_piese(self):
        return self.__piese.load_from_file()

    def store_piese(self, piese):
        self.__piese.save_to_file(piese)

    def genereaza_piese(self, num_piese):
        if(not validate_num_piese(num_piese)):
            raise ValueError("Numarul de piese trebuie sa fie un numar pozitiv.")
        num_piese = int(num_piese)
        piese = self.__piese.genereaza_piese(num_piese)
        return piese

    def export_piese(self, filename):
        if(not validate_filename(filename)):
            raise ValueError("Fisierul trebuie sa fie de tip .txt")
        self.__piese.export_piese(filename)