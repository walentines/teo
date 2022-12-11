from Service.piesaService import piesaService
from UI.print_functions import *

def print_piese(piese):
    for piesa in piese:
        print(piesa)

class UI:
    def __init__(self):
        self.__piesaS = piesaService()

    def adauga_piesa(self):
        titlu = input("Introdu titlul: ")
        regizor = input("Introdu numele regizorului: ")
        gen = input("Introdu genul: ")
        durata = input("Introdu durata piesei in ore: ")
        self.__piesaS.adauga_piesa(titlu, regizor, gen, durata)

    def modificare_piesa(self):
        titlu = input("Introdu titlul: ")
        regizor = input("Introdu numele regizorului: ")
        gen = input("Introdu genul nou: ")
        durata = input("Introdu durata noua a piesei in ore: ")
        self.__piesaS.modificare_piesa(titlu, regizor, gen, durata)

    def genereaza_piese(self):
        num_piese = input("Introdu numarul de piese: ")
        piese = self.__piesaS.genereaza_piese(num_piese)
        print_piese(piese)

    def exporta_piese_sortate(self):
        filename = input("Introdu numele fisierului")
        self.__piesaS.export_piese(filename)

    def run(self):
        print_menu()
        while True:
            comanda = input("Introdu comanda: ")
            if(comanda == "ap"):
                self.adauga_piesa()
            elif(comanda == "mp"):
                self.modificare_piesa()
            elif(comanda == "cp"):
                self.genereaza_piese()
            elif(comanda == "ep"):
                self.exporta_piese_sortate()
            elif(comanda == "exit"):
                break