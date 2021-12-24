from ea_functions import EvoDeliveryEaFunctions
from pyeasyga import pyeasyga


def eval_string(config):
    ga = pyeasyga.GeneticAlgorithm(seed_data=config["seed_data"],
                                   population_size=config["population_size"],
                                   generations=config["generations"],
                                   crossover_probability=config["crossover_probability"],
                                   mutation_probability=config["mutation_probability"],
                                   elitism=config["elitism"],
                                   maximise_fitness=config["maximise_fitness"])

    ga.create_individual = EvoDeliveryEaFunctions.create_individual
    ga.crossover_function = EvoDeliveryEaFunctions.crossover
    ga.mutate_function = EvoDeliveryEaFunctions.mutate
    ga.selection_function = EvoDeliveryEaFunctions.selection
    ga.fitness_function = EvoDeliveryEaFunctions.fitness

    ga.run()

    return ga.best_individual()

    # for individual in ga.last_generation():
    #     print(individual)
