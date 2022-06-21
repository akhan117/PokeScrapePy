import json
from Scripts import pokeAPI_scraper
from Scripts import scraped_access


if __name__ == '__main__':
    # Downloads Pokemon Data for all Pokemon forms
    # pokeAPI.downloadAllPokemon()

    # Downloads Species Data for all Pokemon Species
    # pokeAPI.downloadAllSpecies()

    # Download Official Artwork + Home Sprites + Maingame sprites etc. Takes a very long time! (Especially the main game
    # sprites)
    # pokeAPI.downloadAllSprites()

    name = 'Rhydon'
    scraped_access.access(name)


