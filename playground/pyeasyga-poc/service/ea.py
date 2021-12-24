import random
from pyeasyga import pyeasyga
import string

EXPECTED_RESULT = "hello world"
LETTERS = list(string.ascii_lowercase) + \
    list(string.whitespace)  # list(string.printable)

DEFAULT_CONFIG = {
    "seed_data": [],
    "population_size": 100,
    "generations": 1000,
    "crossover_probability": 0.8,
    "mutation_probability": 0.2,
    "elitism": True,
    "maximise_fitness": True
}


class HelloWorldEa():
    expected_result = [c for c in EXPECTED_RESULT]

    def __init__(self, expected_result=EXPECTED_RESULT, config=DEFAULT_CONFIG):
        self.config = config
        expected_result = EXPECTED_RESULT if expected_result is None else expected_result
        HelloWorldEa.expected_result = [c for c in expected_result]
        self.ga = pyeasyga.GeneticAlgorithm(seed_data=self.config["seed_data"],
                                            population_size=self.config["population_size"],
                                            generations=self.config["generations"],
                                            crossover_probability=self.config["crossover_probability"],
                                            mutation_probability=self.config["mutation_probability"],
                                            elitism=self.config["elitism"],
                                            maximise_fitness=self.config["maximise_fitness"])

        self.ga.create_individual = self.create_individual
        self.ga.crossover_function = self.crossover
        self.ga.mutate_function = self.mutate
        self.ga.selection_function = self.selection
        self.ga.fitness_function = self.fitness

    def run(self):
        self.ga.run()

    def result(self):
        return {"best_individual": self.ga.best_individual(), "expected result": self.expected_result}

    def best_individual(self):
        return self.ga.best_individual()

    def last_generation(self):
        return self.ga.last_generation()

    @staticmethod
    def create_individual(data):
        return [random.choice(LETTERS) for _ in range(len(HelloWorldEa.expected_result))]

    @staticmethod
    def crossover(parent_1, parent_2):
        crossover_index = random.randrange(1, len(parent_1))
        child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
        child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
        return child_1, child_2

    @staticmethod
    def mutate(individual):
        mutate_index = random.randrange(len(individual))
        individual[mutate_index] = random.choice(LETTERS)

    @staticmethod
    def selection(population):
        return random.choice(population)

    @staticmethod
    def fitness(individual, data):
        fitness = 0

        for c1, c2 in zip(individual, HelloWorldEa.expected_result):
            if c1 == c2:
                fitness += 1
        return fitness
