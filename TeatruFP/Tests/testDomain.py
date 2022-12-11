from Repository.peisaRepository import PiesaRepo

def genereaza_input():
    pr = PiesaRepo("/Users/valentinserban/PycharmProjects/TeatruFP/Data/piese_de_teatru_test.txt")
    piese = pr.load_from_file()

    return piese

def test_get_titlu():
    piese = genereaza_input()
    titlu = piese[0].get_titlu()
    titlu_corect = "Capra cu trei iezi"
    assert titlu == titlu_corect

def test_get_regizor():
    piese = genereaza_input()
    regizor = piese[0].get_regizor()
    regizor_corect = "Vlad Gabriel"
    assert regizor == regizor_corect

def test_get_gen():
    piese = genereaza_input()
    gen = piese[0].get_gen()
    gen_corect = "Drama"
    assert gen == gen_corect

def test_get_durata():
    piese = genereaza_input()
    durata = piese[0].get_durata()
    durata_corect = 8
    assert durata == durata_corect

def test_set_titlu():
    piese = genereaza_input()
    titlu = "Salut"
    piese[0].set_titlu(titlu)
    titlu_curent = piese[0].get_titlu()
    assert titlu == titlu_curent

def test_set_regizor():
    piese = genereaza_input()
    regizor = "Salut"
    piese[0].set_regizor(regizor)
    regizor_curent = piese[0].get_regizor()
    assert regizor == regizor_curent

def test_set_gen():
    piese = genereaza_input()
    gen = "Comedie"
    piese[0].set_gen(gen)
    gen_curent = piese[0].get_gen()
    assert gen == gen_curent

def test_set_durata():
    piese = genereaza_input()
    durata = 1
    piese[0].set_durata(durata)
    durata_curent = piese[0].get_durata()
    assert durata == durata_curent

def test_all_domain():
    test_get_titlu()
    test_get_regizor()
    test_get_gen()
    test_get_durata()
    test_set_titlu()
    test_set_regizor()
    test_set_gen()
    test_set_durata()