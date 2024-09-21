import random
import matplotlib.pyplot as plt
import numpy as np
from deap import base, creator, tools, algorithms
from config import *
from fitness import himmelblau, penalty
from genetic_operators import crossover, mutation, selection

# Define the individual and fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Register all the DEAP functions in the toolbox
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, BOUNDS[0], BOUNDS[1])
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=2)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", himmelblau)
toolbox.register("mate", crossover)
toolbox.register("mutate", mutation)
toolbox.register("select", selection)

# Set up logging and statistics
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", np.min)
stats.register("max", np.max)

logbook = tools.Logbook()
logbook.header = ["gen", "nevals"] + stats.fields

hall_of_fame = tools.HallOfFame(1)

# Run the algorithm and log statistics
population = toolbox.population(n=POPULATION_SIZE)
population, log = algorithms.eaSimple(population, toolbox, cxpb=CROSSOVER_PROB, mutpb=MUTATION_PROB, 
                                      ngen=N_GENERATIONS, stats=stats, halloffame=hall_of_fame, verbose=True)

# Display the best solution
print("Best individual:", hall_of_fame[0])

# Extract statistics from the logbook for plotting
gen = logbook.select("gen")
avg_fitness = logbook.select("avg")
min_fitness = logbook.select("min")
max_fitness = logbook.select("max")

# Plotting the convergence of fitness over generations
plt.figure(figsize=(10, 6))
plt.plot(gen, min_fitness, label="Min Fitness")
plt.plot(gen, avg_fitness, label="Avg Fitness")
plt.plot(gen, max_fitness, label="Max Fitness")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Convergence of Fitness Over Generations")
plt.legend()
plt.grid(True)
plt.show()
