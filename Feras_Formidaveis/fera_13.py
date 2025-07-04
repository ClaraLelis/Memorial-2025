import random

preco={"H": 1.39,
    "He": 24,
    "Li": 85.6,
    "Be": 857,
    "B": 3.68,
    "C": 0.122,
    "N": 0.14,
    "O": 0.154,
    "F": 2.16,
    "Ne": 240,
    "Na": 3.43,
    "Mg": 2.32,
    "Al": 1.79,
    "Si": 1.7,
    "P": 2.69,
    "S": 0.0926,
    "Cl": 0.082,
    "Ar": 0.931,
    "K": 13.6,
    "Ca": 2.35,
    "Sc": 3460,
    "Ti": 11.7,
    "V": 385,
    "Cr": 9.4,
    "Mn": 1.82,
    "Fe": 0.424,
    "Co": 32.8,
    "Ni": 13.9,
    "Cu": 6,
    "Zn": 2.55,
    "Ga": 148,
    "Ge": 1010,
    "As": 1.31,
    "Se": 21.4,
    "Br": 4.39,
    "Kr": 290,
    "Rb": 15500,
    "Sr": 6.68,
    "Y": 31,
    "Nb": 85.6,
    "Mo": 40.1,
    "Tc": 100000,
    "Ru": 10600,
    "Rh": 147000,
    "Pd": 49500,
    "Ag": 521,
    "Cd": 2.73,
    "In": 167,
    "Sn": 18.7,
    "Sb": 5.79,
    "Te": 63.5,
    "I": 35,
    "Xe": 1800,
    "Cs": 61800,
    "Ba": 0.275,
    "La": 4.92,
    "Ce": 4.71,
    "Pr": 103,
    "Nd": 57.5,
    "Pm": 460000,
    "Sm": 13.9,
    "Eu": 31.4,
    "Gd": 28.6,
    "Tb": 658,
    "Dy": 307,
    "Ho": 57.1,
    "Er": 26.4,
    "Tm": 3000,
    "Yb": 17.1,
    "Lu": 643,
    "Hf": 900,
    "Ta": 312,
    "W": 35.3,
    "Re": 4150,
    "Os": 12000,
    "Ir": 56200,
    "Pt": 27800,
    "Hg": 30.2,
    "Tl": 4200,
    "Pb": 2,
    "Bi": 6.36,
    "Po": 49200000000000,
    "Ac": 29000000000000,
    "Th": 287,
    "Pa": 280000,
    "U": 101,
    "Np": 660000,
    "Pu": 6490000,
    "Am": 750000,
    "Cm": 160000000000,
    "Bk": 185000000000,
    "Cf": 185000000000,}

ELEMENTOS=list(preco.keys())

def criar_individuo():
    elementos = random.sample(ELEMENTOS, 3)
    x = random.randint(5, 90)
    y = random.randint(5, 100 - x - 5)
    z = 100 - x - y
    return {"el": elementos, "qtd": [x, y, z]}

def fitness(ind):
    custo = 0
    for el, q in zip(ind["el"], ind["qtd"]):
        custo += (q / 1000) * preco[el]
    return custo

def crossover(p1, p2):
    filho_el = list(set(random.sample(p1["el"] + p2["el"], 3)))
    while len(filho_el) < 3:
        novo = random.choice(ELEMENTOS)
        if novo not in filho_el:
            filho_el.append(novo)

    x = random.randint(5, 90)
    y = random.randint(5, 100 - x - 5)
    z = 100 - x - y
    return {"el": filho_el, "qtd": [x, y, z]}

def mutacao(ind):
    if random.random() < 0.5:
        ind["el"] = random.sample(ELEMENTOS, 3)
    else:
        x = random.randint(5, 90)
        y = random.randint(5, 100 - x - 5)
        z = 100 - x - y
        ind["qtd"] = [x, y, z]
    return ind