import json
from Scripts import pokeAPI_scraper
from Scripts import scraped_access

if __name__ == '__main__':
    # Generates folders to store data
    pokeAPI_scraper.generate_folders()

    # Downloads Pokemon Data for all Pokemon forms (if uncommented)
    # pokeAPI_scraper.download_all_pokemon()

    # Downloads Species Data for all Pokemon Species (if uncommented)
    # pokeAPI_scraper.download_all_species()

    # Download Official Artwork + Home Sprites + Maingame sprites etc. Takes a very long time! (Especially the main game
    # sprites) (if uncommented)
    # pokeAPI_scraper.download_all_pokemon_sprites()

    name = 'Rhydon'
    scraped_access.access(name)
