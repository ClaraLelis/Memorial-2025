import numpy as np
import matplotlib.pyplot as plt
import random

def distancia(path,coords):
    dist=0
    for i in range(len(path)-1):
        a,b=coords[path[i]],coords[path[i+1]]
        dist+=np.linalg.norm(a-b)
    return dist

def create_individual(cidade_par, cidade_impar):
    odd_perm=random.sample(cidade_impar,len(cidade_impar))
    even_perm=random.sample(cidade_par,len(cidade_par))
    return [0]+odd_perm+even_perm+[0]

def crossover(p1,p2,cidade_impar):
    o1,e1=p1[1:1+len(cidade_impar)],p1[1+len(cidade_impar):-1]
    o2,e2=p2[1:1+len(cidade_impar)],p2[1+len(cidade_impar):-1]
    cut=len(o1)//2
    child_odd=o1[:cut]+[g for g in o2 if g not in o1[:cut]]
    child_even=e1[:cut]+[g for g in e2 if g not in e1[:cut]]
    return [0]+child_odd+child_even+[0]

def mutacao(individual,cidade_impar,taxa_mutacao=0.1):
    if random.random()<taxa_mutacao:
        i,j=random.sample(range(1,1+len(cidade_impar)),2)
        individual[i],individual[j]=individual[j],individual[i]
    if random.random()<taxa_mutacao:
        i,j=random.sample(range(1+len(cidade_impar),len(individual)-1),2)
        individual[i],individual[j]=individual[j],individual[i]
    return individual