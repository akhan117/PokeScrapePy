import json


def access(name):
    open_this = 'PokeAPI Data/Pokemon Data/' + name + '.json'
    with open(open_this, 'r') as f:
        data = json.load(f)

    print(name.capitalize())
    # Pokedex Number
    poke_number = data["id"]
    print("Pokedex Number: " + str(poke_number))

    # Types
    if len(data["types"]) == 1:
        print("Type: " + (data["types"][0]["type"]["name"]).capitalize())
    else:
        print("Types: " + (data["types"][0]["type"]["name"]).capitalize() + ", " +
              (data["types"][1]["type"]["name"]).capitalize())

    # Stats
    base_stat_total = 0
    for i in data["stats"]:
        print((i["stat"]["name"]).capitalize() + ": " + str(i["base_stat"]))
        base_stat_total += i["base_stat"]
    print("BST: " + str(base_stat_total))

    # Abilities
    for i in data["abilities"]:
        if i["is_hidden"] is False:
            print("Ability " + str(i["slot"]) + ": " + (i["ability"]["name"]).capitalize())

        else:
            print("Hidden Ability: " + (i["ability"]["name"]).capitalize())

    # Weight/Height
    height = data["height"] / 10
    print("Height: " + str(height) + " Meters")

    weight = data["weight"] / 10
    print("Weight: " + str(weight) + " Kg")
