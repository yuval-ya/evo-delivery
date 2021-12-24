

# import random
# import string
# from pyeasyga import pyeasyga


# EXPECTED_RESULT = [c for c in "hello world"]
# LETTERS = list(string.ascii_lowercase) + \
#     list(string.whitespace)  # list(string.printable)

# evo_delivery_ea_config = {
#     "seed_data": [],
#     "population_size": 100,
#     "generations": 1000,
#     "crossover_probability": 0.8,
#     "mutation_probability": 0.2,
#     "elitism": True,
#     "maximise_fitness": True
# }


# class EvoDeliveryEaFunctions():
#     @staticmethod
#     def create_individual(data):
#         return [random.choice(LETTERS) for _ in range(11)]

#     @staticmethod
#     def crossover(parent_1, parent_2):
#         crossover_index = random.randrange(1, len(parent_1))
#         child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
#         child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
#         return child_1, child_2

#     @staticmethod
#     def mutate(individual):
#         mutate_index = random.randrange(len(individual))
#         individual[mutate_index] = random.choice(LETTERS)

#     @staticmethod
#     def selection(population):
#         return random.choice(population)

#     @staticmethod
#     def fitness(individual, data):
#         fitness = 0

#         for c1, c2 in zip(individual, EXPECTED_RESULT):
#             if c1 == c2:
#                 fitness += 1
#         return fitness


# def eval_string():
#     ga = pyeasyga.GeneticAlgorithm(seed_data=evo_delivery_ea_config["seed_data"],
#                                    population_size=evo_delivery_ea_config["population_size"],
#                                    generations=evo_delivery_ea_config["generations"],
#                                    crossover_probability=evo_delivery_ea_config["crossover_probability"],
#                                    mutation_probability=evo_delivery_ea_config["mutation_probability"],
#                                    elitism=evo_delivery_ea_config["elitism"],
#                                    maximise_fitness=evo_delivery_ea_config["maximise_fitness"])

#     ga.create_individual = EvoDeliveryEaFunctions.create_individual
#     ga.crossover_function = EvoDeliveryEaFunctions.crossover
#     ga.mutate_function = EvoDeliveryEaFunctions.mutate
#     ga.selection_function = EvoDeliveryEaFunctions.selection
#     ga.fitness_function = EvoDeliveryEaFunctions.fitness

#     ga.run()
#     print(ga.best_individual())

#     # for individual in ga.last_generation():
#     #     print(individual)


# eval_string()
