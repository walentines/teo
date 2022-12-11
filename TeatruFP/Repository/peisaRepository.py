import string

from Domain.piesaDomain import Piesa
import random

def save_to_any_file(filename, piese):
    try:
        f = open(filename, 'w')
    except:
        raise ValueError("Fisierul nu poate fi deschis!")
    for piesa in piese:
        f.write(piesa.get_regizor() + ";" + piesa.get_titlu() + ";" + str(piesa.get_durata()) + ";" +
            piesa.get_gen() + "\n")
    f.close()

class PiesaRepo:
    def __init__(self, file):
        self.__filename = file

    def adauga_piesa(self, titlu, regizor, gen, durata):
        piese = self.load_from_file()
        p = self.construieste_piesa(titlu, regizor, gen, durata)
        if(p in piese):
            raise ValueError("Piesa deja exista in fisier!")
        piese.append(p)
        self.save_to_file(piese)

    def construieste_piesa(self, titlu, regizor, gen, durata):
        p = Piesa()
        p.set_titlu(titlu)
        p.set_regizor(regizor)
        p.set_gen(gen)
        p.set_durata(durata)

        return p

    def load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except:
            raise ValueError("Fisierul nu poate fi deschis!")

        piese = list()
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            titlu, regizor, gen, durata = line.split(';')
            durata = int(durata)
            p = self.construieste_piesa(titlu, regizor, gen, durata)
            piese.append(p)

        f.close()
        return piese

    def save_to_file(self, piese):
        try:
            f = open(self.__filename, 'w')
        except:
            raise ValueError("Fisierul nu poate fi deschis!")
        for piesa in piese:
            f.write(piesa.get_titlu() + ";" + piesa.get_regizor() + ";" + piesa.get_gen() + ";" + str(piesa.get_durata()) + "\n")
        f.close()

    def modificare_piesa(self, titlu, regizor, gen_nou, durata_noua):
        piese = self.load_from_file()
        ok = 0
        for piesa in piese:
            if(piesa.get_titlu().lower() == titlu.lower() and piesa.get_regizor().lower() == regizor.lower()):
                piesa.set_gen(gen_nou)
                piesa.set_durata(durata_noua)
                ok = 1
        if(not ok):
            raise ValueError("Nu exista vreo piesa cu titlul si regizorul specificat!")

        self.save_to_file(piese)

    def genereaza_piese(self, num_piese):
        len_titlu = random.randint(8, 12)
        len_regizor = random.randint(8, 12)
        piese = list()
        for i in range(num_piese):
            titlu = "".join(random.choices(string.ascii_letters, k = len_titlu))
            regizor = "".join(random.choices(string.ascii_letters, k = len_regizor))
            gen = random.choice(["Comedie", "Drama", "Satira", "Altele"])
            durata = random.randint(1, 999)
            p = Piesa()
            p.set_titlu(titlu)
            p.set_regizor(regizor)
            p.set_gen(gen)
            p.set_durata(durata)
            self.adauga_piesa(titlu, regizor, gen, durata)
            piese.append(p)

        return piese

    def export_piese(self, filename):
        piese = self.load_from_file()
        piese = sorted(piese, key = lambda x: (x.get_regizor(), x.get_titlu()))
        save_to_any_file(filename, piese)
