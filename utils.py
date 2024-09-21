# utils.py
import matplotlib.pyplot as plt

def plot_convergence(logbook):
    gen = logbook.select("gen")
    min_fits = logbook.select("min")
    plt.plot(gen, min_fits, label="Minimum Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.show()
