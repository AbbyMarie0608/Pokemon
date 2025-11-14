import re
from pokeclass import Pokemon

def read_file(file):
    #Idk where to put this for now so imma just keep it here
    pokedex = []
    with open(file, 'r') as opened_file:
        for line in opened_file:
            line = re.split(r', (?=(?:[^"]*"[^"]*")*[^"]*$)', line)
            pokedex.append(Pokemon(line[0], line[1], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11]))
            print(pokedex)
        opened_file.close()

read_file("pokemon.csv")
