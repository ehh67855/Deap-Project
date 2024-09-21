# DEAP Evolutionary Algorithm for Himmelblau's Function Optimization

## Project Overview
This project implements a genetic algorithm using the DEAP (Distributed Evolutionary Algorithms in Python) framework to optimize **Himmelblau's function** within specified bounds and under a constraint \( x + y < 0 \). The project demonstrates how to apply evolutionary algorithms to continuous optimization problems and includes code for analyzing the convergence of the solution over generations.

Himmelblau's function is a multimodal function with four global minima, making it an ideal candidate for testing evolutionary optimization techniques. The goal is to minimize the function under the constraint \( x + y < 0 \) and within the bounds \([-6, 6]\) for both variables.

## Himmelblau's Function
The function being optimized is:
\[
f(x, y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
\]
This function has multiple minima, including:
- \( f(3.0, 2.0) = 0 \)
- \( f(-2.805118, 3.131312) = 0 \)
- \( f(-3.779310, -3.283186) = 0 \)
- \( f(3.584428, -1.848126) = 0 \)

Install Requirments:
```
pip install plotly deap numpy matplotlib
```

You can run the Jupyter Notebook *Himmelblau.ipynb*, or your can excecute the python program using 
```
python main.py
```

### Files
- **`config.py`**: Contains the hyperparameters for the genetic algorithm such as population size, mutation probability, and crossover probability.
- **`fitness.py`**: Defines the fitness function (Himmelblau's function) and the constraint penalty function.
- **`genetic_operators.py`**: Contains the crossover, mutation, and selection operators used by the DEAP framework.
- **`main.py`**: The main program that sets up the DEAP genetic algorithm, runs it, and plots the convergence of the solution.
- **`utils.py`**: (Optional) Contains helper functions for plotting and analyzing the results.
- **`Himmelblau.ipynb`**: Tutorial explaining each step

