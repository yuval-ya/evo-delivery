from ea import HelloWorldEa

ea_instance = HelloWorldEa()
ea_instance.run()
print(ea_instance.best_individual())


"""
ideas

seed_data = {
    "drivers": {
        1: {"capacity": 1000, "max_distance": 4000},
        2: {"capacity": 2500, "max_distance": 5000},
    },
    "orders": {
        100: {"size": 500, "distances": {200: 500, 300: 223}},
        200: {"size": 20, "distances": {100: 250, 300: 122}},
        300: {"size": 350, "distances": {100: 470, 200: 20}},
    },
}

individual1 = [(100, 1, .23), (200, 1, .34), (300, 2, .55)]

individual2 = [(100, 1, .53), (200, 2, .67), (300, 1, .15)]
   
cross = [(100, 1, .23), (200, 2, .67), (300, 2, .55)]

"""
