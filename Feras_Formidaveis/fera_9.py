import random

def create_individual(CHARS):
    length = random.randint(1, 20)
    return ''.join(random.choices(CHARS, k=length))

def fitness(ind,TARGET):
    match = sum(c1 == c2 for c1, c2 in zip(ind, TARGET))
    size_penalty = abs(len(ind) - len(TARGET))
    return match - size_penalty

def mutate(ind,CHARS):
    ind = list(ind)
    if random.random() < 0.5 and len(ind) > 1:
        ind.pop(random.randint(0, len(ind)-1))  
    elif len(ind) < 20:
        ind.insert(random.randint(0, len(ind)), random.choice(CHARS))  
    else:
        ind[random.randint(0, len(ind)-1)] = random.choice(CHARS)
    return ''.join(ind)

def crossover(p1, p2):
    min_len = min(len(p1), len(p2))
    if min_len < 2:
        return random.choice([p1, p2])
    cut = random.randint(1, min_len - 1)
    child = p1[:cut] + p2[cut:]
    return child