from Service.piesaService import piesaService

def genereaza_input():
    pr = piesaService()

    return pr

def test_adauga_piesa():
    pr = genereaza_input()
    prev_piese = pr.get_piese()
    lungime1 = len(prev_piese)
    titlu = "Ce mai faci"
    regizor = "Ce mai faci"
    gen = "Comedie"
    durata = 10
    pr.adauga_piesa(titlu, regizor, gen, durata)
    piese = pr.get_piese()
    lungime2 = len(piese)
    pr.store_piese(prev_piese)
    assert lungime1 + 1 == lungime2

def test_modificare_piesa():
    pr = genereaza_input()
    prev_piese = pr.get_piese()
    titlu = "Capra cu trei iezi"
    regizor = "Vlad Gabriel"
    gen = "Comedie"
    durata = 100
    pr.modificare_piesa(titlu, regizor, gen, durata)
    piese = pr.get_piese()
    assert piese[0].get_gen() == gen
    assert piese[0].get_durata() == durata
    pr.store_piese(prev_piese)

def test_genereaza_piese():
    pr = genereaza_input()
    prev_piese = pr.get_piese()
    lungime1 = len(prev_piese)
    num_piese = 3
    pr.genereaza_piese(num_piese)
    assert len(pr.get_piese()) - num_piese == lungime1
    pr.store_piese(prev_piese)

def test_all_service():
    test_adauga_piesa()
    test_modificare_piesa()
    test_genereaza_piese()