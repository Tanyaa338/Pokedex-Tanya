import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!


def take():
    for pokemon in data:
        return pokemon
take()

def search():
    y = input("What language do you want?")
    if y == "Chinese":
        print("hao")
        print(pokedex[2])
    elif y == "English":
        print("okay")
        print(pokedex[1])
    elif y == "Japanese":
        print("eeeeeeeeeeeeeeeee")
        print(pokedex[3])
    elif y == "FRENCH":
        print("ouiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        print(pokedex[4])
    x = input("Which Pokemon's data do you want?")
    for pokemon in data:
        if x == data[pokemon][2]:
            print(data[pokemon][2])
search()

def name():
    pokemon = pokedex[y]
    y = (1,100000000)
    ok = input("What pokemon do you want to see?")
    sofia = len(ok)
    for i in range(1, sofia):
        if ok[i] == data[pokemon]:
            print(data[pokemon])
        else:
            print("ggs! better luck next time. the system craaaaaaaaaaaaaaaaaaaaaaaaaaaashed.")
name()

def mooves():
    pokemon = pokedex[y]
    moves = pokedex 
    y = (1,959)
    print("heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeereeee areeeeeeeeeee thee moooooves")
    if data[pokedex][2] == "normal":
        print(pokemon[moves])
    elif data[pokemon][2] == "fighting":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "flying":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "poison":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "ground":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "rock":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "bug":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "ghost":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "steel":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "fire":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "water":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "grass":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "electric":
       print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "psychic":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "ice":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "dragon":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "dark":
        print(moves[pokemon]["ename"])
    elif data[pokemon][2] == "fairy":
        print(moves[pokemon]["ename"])
    else:
        print("you're cooked.")
mooves()
563



""" def get_pokemon(pokemon):
    #finds the poke
    return poke
def get_moves(poke):
    x = get_pokemon(poke)  """