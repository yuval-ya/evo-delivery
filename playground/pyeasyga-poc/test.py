# import random
# import string

# letters = list(string.printable)

# # def mutate(individual):
# #     mutate_index = random.randrange(len(individual))
# #     individual[mutate_index] = random.choice(letters)


# # result = [c for c in "hello world"]

# # print(result)
# # mutate(result)
# # mutate(result)
# # mutate(result)
# # print(result)

# expected_result = [c for c in "hello world"]


# def fitness(individual, data):
#     fitness = 0

#     for c1, c2 in zip(individual, expected_result):
#         if c1 == c2:
#             fitness += 1
#     return fitness


# print(letters)
