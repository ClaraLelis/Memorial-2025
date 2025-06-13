import random

def gerar_palindromo(base):  
    return base[0] + base[1] + base[2] + base[1] + base[0]

def tem_vogal(pal,VOGAIS):
    return any(c in VOGAIS for c in pal)

def fitness(ind,VOGAIS):
    pal = gerar_palindromo(ind)
    return int(tem_vogal(pal,VOGAIS))

def mutacao(ind,ALFABETO):
    i = random.randint(0, 2)
    ind[i] = random.choice(ALFABETO)
    return ind

def crossover(p1, p2):
    cut = random.randint(1, 2)
    return p1[:cut] + p2[cut:]

def criar_individuo(ALFABETO):
    return [random.choice(ALFABETO) for _ in range(3)]
