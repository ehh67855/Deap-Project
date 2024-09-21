# genetic_operators.py
from deap import tools

def crossover(ind1, ind2):
    return tools.cxTwoPoint(ind1, ind2)

def mutation(ind):
    return tools.mutFlipBit(ind, indpb=0.05)

def selection(population, k):
    # k is the number of individuals to select
    return tools.selTournament(population, k, tournsize=3)
