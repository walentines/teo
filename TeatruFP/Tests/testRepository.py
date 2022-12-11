from Repository.peisaRepository import PiesaRepo

def genereaza_input():
    pr = PiesaRepo("/Users/valentinserban/PycharmProjects/TeatruFP/Data/piese_de_teatru_test.txt")

    return pr

def test_adauga_piesa():
    pr = genereaza_input()
    piese_prev = pr.load_from_file()
    lungime1 = len(piese_prev)
    titlu = "Ce mai faci"
    regizor = "Ce mai faci"
    gen = "Comedie"
    durata = 1
    pr.adauga_piesa(titlu, regizor, gen, durata)
    lungime2 = len(pr.load_from_file())
    pr.save_to_file(piese_prev)

    assert lungime1 + 1 == lungime2

def test_modificare_piesa():
    pr = genereaza_input()
    piese_prev = pr.load_from_file()
    titlu = "Capra cu trei iezi"
    regizor = "Vlad Gabriel"
    gen = "Comedie"
    durata = 6
    pr.modificare_piesa(titlu, regizor, gen, durata)
    assert pr.load_from_file()[0].get_gen() == gen
    assert pr.load_from_file()[0].get_durata() == durata
    pr.save_to_file(piese_prev)

def test_genereaza_piese():
    pr = genereaza_input()
    piese_prev = pr.load_from_file()
    lungime1 = len(piese_prev)
    num_piese = 3
    pr.genereaza_piese(num_piese)
    assert lungime1 + num_piese == len(pr.load_from_file())
    pr.save_to_file(piese_prev)

def test_all_repo():
    test_adauga_piesa()
    test_modificare_piesa()
    test_genereaza_piese()
