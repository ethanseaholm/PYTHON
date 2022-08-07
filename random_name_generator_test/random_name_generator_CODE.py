#

import random

def generate_names(randomnamegenerator):
	names = open('randomnamegenerator.txt').read().splitlines()
	return random.choice(names)

print(generate_names('randomnamegenerator.txt'))

