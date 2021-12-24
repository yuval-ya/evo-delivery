import string

EXPECTED_RESULT = "hello world"
LETTERS = list(string.ascii_lowercase) + \
    list(string.whitespace)  # list(string.printable)

DEFAULT_CONFIG = {
    "seed_data": [],
    "population_size": 1000,
    "generations": 10000,
    "crossover_probability": 0.8,
    "mutation_probability": 0.2,
    "elitism": True,
    "maximise_fitness": True
}
