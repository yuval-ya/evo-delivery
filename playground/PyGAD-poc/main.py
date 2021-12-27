import pygad

# Distance between each pair of cities
w0 = [999, 1, 999, 999]
w1 = [999, 999, 1, 999]
w2 = [999, 999, 999, 1]
w3 = [1, 999, 999, 999]

distances = {0: w0, 1: w1, 2: w2, 3: w3}

# ----------------------------------------------------------------


def calculate_length(route):
    length = 0
    for previous, current in zip(route, route[1:]):
        length += distances[previous][current]
    return length


def fitness_func(solution, solution_idx):
    print("sol:")
    print(solution)
    pen = (max(ga_instance.lengths) - calculate_length(solution)) / max(ga_instance.lengths)
    return pen * 100


fitness_function = fitness_func


def on_start(ga_instance):
    print("on_start()")
    lengths = []
    for sol in ga_instance.population:
        lengths.append(calculate_length(sol))

    ga_instance.lengths = lengths
    print(ga_instance.population)
    print(ga_instance.lengths)


def on_generation(ga_instance):
    print("on_generation()")
    lengths = []
    for sol in ga_instance.population:
        lengths.append(calculate_length(sol))

    ga_instance.lengths = lengths
    print(ga_instance.population)
    print(ga_instance.lengths)


def on_stop(ga_instance, last_population_fitness):
    print("on_stop()")


ga_instance = pygad.GA(num_generations=10,
                       num_parents_mating=3,
                       initial_population=[[3, 1, 0, 2], [0, 2, 1, 3], [2, 0, 1, 3], [2, 0, 3, 1]],
                       fitness_func=fitness_function,
                       allow_duplicate_genes=False,
                       gene_space=range(0, len(distances)),
                       sol_per_pop=4,
                       gene_type=int,
                       num_genes=len(distances),
                       on_start=on_start,
                       on_generation=on_generation,
                       mutation_num_genes=2,
                       mutation_type='random',
                       )

ga_instance.run()
ga_instance.plot_fitness()
print(ga_instance.best_solution())

# def on_fitness(ga_instance, population_fitness):
#     print("on_fitness()")
#
# def on_parents(ga_instance, selected_parents):
#     print("on_parents()")
#
# def on_crossover(ga_instance, offspring_crossover):
#     print("on_crossover()")
#
# def on_mutation(ga_instance, offspring_mutation):
#     print("on_mutation()")
