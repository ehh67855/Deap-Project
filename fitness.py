# fitness.py
def himmelblau(individual):
    x, y = individual
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2,

def penalty(individual):
    # Constraint: x + y < 0
    x, y = individual
    return max(0, x + y)
