import numpy as np

class GeneticOptimizer:
    def __init__(self, population_size=50, mutation_rate=0.1, crossover_rate=0.8):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

    def initialize_population(self, dimension):
        return np.random.rand(self.population_size, dimension)

    def select(self, population, fitness):
        idx = np.argsort(fitness)
        return population[idx[:self.population_size//2]]

    def crossover(self, parents):
        offspring = []
        for i in range(0, len(parents)-1, 2):
            child = (parents[i] + parents[i+1]) / 2
            offspring.append(child)
        return np.array(offspring)

    def mutate(self, offspring):
        noise = np.random.normal(0, self.mutation_rate, offspring.shape)
        return offspring + noise
