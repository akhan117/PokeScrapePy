import requests
import json
import os


# Fetch Pokemon data of all Pokemon
def download_all_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon')
    pokemon_data = response.json()
    total_count = pokemon_data['count']

    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=' + str(total_count))
    pokemon_data = response.json()

    with open('PokeAPI Data/pokemon.json', 'w') as f:
        json.dump(pokemon_data, f)

    for i in pokemon_data['results']:
        name = i['name']
        url = i['url']
        response_1 = requests.get(url)
        if response_1.status_code != 200:
            print(name + ": FAILED")

        data = response_1.json()
        save_to = 'PokeAPI Data/Pokemon Data/' + name + '.json'
        with open(save_to, 'w') as r:
            json.dump(data, r)


# Download Species data of all Pokemon
def download_all_species():
    response = requests.get('https://pokeapi.co/api/v2/pokemon-species')
    pokemon_data = response.json()
    total_count = pokemon_data['count']

    response = requests.get('https://pokeapi.co/api/v2/pokemon-species?limit=' + str(total_count))
    pokemon_data = response.json()
    with open('PokeAPI Data/pokemon-species.json', 'w') as f:
        json.dump(pokemon_data, f)

    for i in pokemon_data['results']:
        name = i['name']
        url = i['url']
        response_1 = requests.get(url)
        if response_1.status_code != 200:
            print(name + ": FAILED")

        data = response_1.json()

        save_to = 'PokeAPI Data/Pokemon Species Data/' + name + '.json'
        with open(save_to, 'w') as r:
            json.dump(data, r)


# Download All Pokemon sprites and artwork
def download_all_pokemon_sprites():
    storage_path = 'PokeAPI Data/Pokemon Data/'
    file_list = os.listdir(storage_path)
    sprite_list = {'back_default', 'back_female', 'back_shiny', 'back_shiny_female', 'front_default',
                   'front_female', 'front_shiny', 'front_shiny_female'}
    for i in file_list:
        with open(storage_path + i, 'r') as f:
            data = json.load(f)

        poke_name = data['name']
        sprites = data['sprites']
        o_sprites = data['sprites']['other']
        g_sprites = data['sprites']['versions']
        # Default
        for j in sprite_list:

            img_link = sprites[j]
            if img_link is not None:
                img_data = requests.get(img_link).content
                file_name = poke_name + "_" + j

                with open('PokeAPI Data/Sprites/Pokemon Sprites/Default Sprites/' + file_name + '.png', 'wb') as f:
                    f.write(img_data)

        # Dream World
        for j in o_sprites['dream_world']:

            dw_link = o_sprites['dream_world'][j]
            if dw_link is not None:
                dw_data = requests.get(dw_link).content
                file_name = poke_name + "_" + j
                with open('PokeAPI Data/Sprites/Pokemon Sprites/Dream World/' + file_name + '.svg', 'wb') as f:
                    f.write(dw_data)

        # Home
        for j in o_sprites['home']:

            ho_link = o_sprites['home'][j]
            if ho_link is not None:
                ho_data = requests.get(ho_link).content
                file_name = poke_name + "_" + j
                with open('PokeAPI Data/Sprites/Pokemon Sprites/Home/' + file_name + '.png', 'wb') as f:
                    f.write(ho_data)

        # Official Art
        of_link = o_sprites['official-artwork']['front_default']
        if of_link is not None:
            file_name = poke_name + "_Official_Artwork"
            of_data = requests.get(of_link).content
            with open('PokeAPI Data/Sprites/Pokemon Sprites/Official Artwork/' + file_name + '.png', 'wb') as f:
                f.write(of_data)

        # Sprites from all games in every generation
        for gen in g_sprites:
            if gen == "generation-i":

                for sprite in g_sprites[gen]['red-blue']:
                    link = g_sprites[gen]['red-blue'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 1/Red Blue/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['yellow']:
                    link = g_sprites[gen]['yellow'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 1/Yellow/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

            if gen == "generation-ii":

                for sprite in g_sprites[gen]['crystal']:
                    link = g_sprites[gen]['crystal'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Crystal/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['silver']:
                    link = g_sprites[gen]['silver'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Silver/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['gold']:
                    link = g_sprites[gen]['gold'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Gold/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

            if gen == "generation-iii":

                for sprite in g_sprites[gen]['emerald']:
                    link = g_sprites[gen]['emerald'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Emerald/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['firered-leafgreen']:
                    link = g_sprites[gen]['firered-leafgreen'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Firered Leafgreen/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['ruby-sapphire']:
                    link = g_sprites[gen]['ruby-sapphire'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Ruby Sapphire/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

            if gen == "generation-iv":

                for sprite in g_sprites[gen]['diamond-pearl']:
                    link = g_sprites[gen]['diamond-pearl'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/Diamond Pearl/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['heartgold-soulsilver']:
                    link = g_sprites[gen]['heartgold-soulsilver'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/Heartgold Soulsilver/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['platinum']:
                    link = g_sprites[gen]['platinum'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/Platinum/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

            if gen == "generation-v":

                for sprite in g_sprites[gen]['black-white']:
                    link = g_sprites[gen]['black-white'][sprite]
                    if link is not None and sprite != 'animated':
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 5/Black White/' +
                                  file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['black-white']['animated']:
                    link = g_sprites[gen]['black-white']['animated'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 5/Black White/Animated/' +
                                  file_name + '.gif', 'wb') as f:
                            f.write(data)

            if gen == "generation-vi":

                for sprite in g_sprites[gen]['omegaruby-alphasapphire']:
                    link = g_sprites[gen]['omegaruby-alphasapphire'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 6/'
                                  'Omegaruby Alphasapphire/' + file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['x-y']:
                    link = g_sprites[gen]['x-y'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 6/'
                                  'X Y/' + file_name + '.png', 'wb') as f:
                            f.write(data)

            if gen == "generation-vii":

                for sprite in g_sprites[gen]['icons']:
                    link = g_sprites[gen]['icons'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 7/'
                                  'Ultra Sun Ultra Moon/Icons/' + file_name + '.png', 'wb') as f:
                            f.write(data)

                for sprite in g_sprites[gen]['ultra-sun-ultra-moon']:
                    link = g_sprites[gen]['ultra-sun-ultra-moon'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 7/'
                                  'Ultra Sun Ultra Moon/' + file_name + '.png', 'wb') as f:
                            f.write(data)

            if gen == "generation-viii":

                for sprite in g_sprites[gen]['icons']:
                    link = g_sprites[gen]['icons'][sprite]
                    if link is not None:
                        file_name = poke_name + "_" + sprite
                        data = requests.get(link).content
                        with open('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 8/'
                                  'Sword Shield/Icons/' + file_name + '.png', 'wb') as f:
                            f.write(data)


# Generate Folder Structure
def generate_folders():
    if not os.path.exists('PokeAPI Data'):
        os.makedirs('PokeAPI Data')

    if not os.path.exists('PokeAPI Data/Pokemon Data'):
        os.makedirs('PokeAPI Data/Pokemon Data')

    if not os.path.exists('PokeAPI Data/Pokemon Species Data'):
        os.makedirs('PokeAPI Data/Pokemon Species Data')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Default Sprites/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Default Sprites/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Dream World/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Dream World/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Home/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Home/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Official Artwork/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Official Artwork/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 1/Red Blue/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 1/Red Blue/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 1/Yellow/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 1/Yellow/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Crystal/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Crystal/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Silver/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Silver/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Gold/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 2/Gold/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Emerald/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Emerald/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Firered Leafgreen/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Firered Leafgreen/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Ruby Sapphire/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 3/Ruby Sapphire/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/Diamond Pearl/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/Diamond Pearl/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/ Heartgold Soulsilver/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/Heartgold Soulsilver/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/'
                          'Heartgold Soulsilver/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 4/Heartgold Soulsilver/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 5/Black White/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 5/Black White/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 5/ Black White/Animated/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 5/Black White/Animated/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 6/Omegaruby Alphasapphire/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 6/Omegaruby Alphasapphire/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 6/X Y/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 6/X Y/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 7/Ultra Sun Ultra Moon/Icons/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 7/Ultra Sun Ultra Moon/Icons/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 7/Ultra Sun Ultra Moon/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 7/Ultra Sun Ultra Moon/')

    if not os.path.exists('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 8/Sword Shield/Icons/'):
        os.makedirs('PokeAPI Data/Sprites/Pokemon Sprites/Versions/Generation 8/Sword Shield/Icons/')
