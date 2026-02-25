import numpy as np
from src.ga_optimizer import GeneticOptimizer
from src.objective_function import objective_function

# Reproducibility
np.random.seed(42)

class DummyModel:
    def predict(self, solution):
        # Example prediction logic (replace with real ML model later)
        heating_load = np.sum(solution)
        cooling_load = np.sum(solution**2)
        return heating_load, cooling_load


def run_optimization():
    model = DummyModel()
    ga = GeneticOptimizer()

    population = ga.initialize_population(dimension=5)

    fitness = []
    for individual in population:
        fit = objective_function(individual, model, weather_condition="hot")
        fitness.append(fit)

    print("Initial population fitness calculated.")
    return fitness


if __name__ == "__main__":
    run_optimization()
