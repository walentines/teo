def validate_title(title):
    if(len(title) > 1):
        return True
    return False

def validate_regizor(regizor):
    if(len(regizor) > 1):
        return True
    return False

def validate_gen(gen):
    gen_list = ["comedie", "drama", "satira", "altele"]
    if(gen.lower() in gen_list):
        return True
    return False

def validate_durata(durata):
    try:
        durata = int(durata)
    except:
        return False
    if(durata > 0):
        return True
    return False

def validate_num_piese(num_piese):
    try:
        num_piese = int(num_piese)
    except:
        return False
    if(num_piese > 0):
        return True
    return False

def validate_filename(filename):
    return filename.endswith(".txt")