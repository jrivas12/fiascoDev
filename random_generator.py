import random
def random_number_generator(l):
    output = []
    for i in range(l):
         output.append(random.randint(1, 5))
    print (output)
random_number_generator(1)
