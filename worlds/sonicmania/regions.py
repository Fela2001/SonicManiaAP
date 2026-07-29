from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SonicManiaPlusWorld

def create_and_connect_regions(world: SonicManiaPlusWorld) -> none:
    create_all_regions(world)
    connect_regions(world)

# Defining all the regions for Sonic Mania. Special Stages and Blue Spheres are accessible in any level through Special rings or checkpoints
def create_all_regions(world: SonicManiaPlusWorld) -> none:
    menu = Region("Menu", world.player, world.multiworld)
    green_hill = Region("Green Hill", world.player, world.multiworld)
    chemical_plant = Region("Chemical Plant", world.player, world.multiworld)
    studiopolis = Region("Studiopolis", world.player, world.multiworld)
    flying_battery = Region("Flying Battery", world.player, world.multiworld)
    press_garden = Region("Press Garden", world.player, world.multiworld)
    stardust_speedway = Region("Stardust Speedway", world.player, world.multiworld)
    hydro_city = Region("Hydro City", world.player, world.multiworld)
    mirage_saloon = Region("Mirage Saloon", world.player, world.multiworld)
    oil_ocean = Region("Oil Ocean", world.player, world.multiworld)
    lava_reef = Region("Lava Reef", world.player, world.multiworld)
    metallic_madness = Region("Metallic Madness", world.player, world.multiworld)
    titanic_monarch = Region("Titanic Monarch", world.player, world.multiworld)
    special_stages = Region("Special Stages", world.player, world.multiworld)
    blue_spheres = Region("Blue Spheres", world.player, world.multiworld)
    egg_reverie = Region("Egg Reverie", world.player, world.multiworld)

    regions = [menu, green_hill, chemical_plant, studiopolis, flying_battery, press_garden, 
           stardust_speedway, hydro_city, mirage_saloon, oil_ocean, lava_reef, 
           metallic_madness, titanic_monarch, special_stages, blue_spheres, egg_reverie]

    world.multiworld.regions += regions


def connect_regions(world: SonicManiaPlusWorld) -> None:
    menu = world.get_region("Menu")
    green_hill = world.get_region("Green Hill")
    chemical_plant = world.get_region("Chemical Plant")
    studiopolis = world.get_region("Studiopolis")
    flying_battery = world.get_region("Flying Battery")
    press_garden = world.get_region("Press Garden")
    stardust_speedway = world.get_region("Stardust Speedway")
    hydro_city = world.get_region("Hydro City")
    mirage_saloon = world.get_region("Mirage Saloon")
    oil_ocean = world.get_region("Oil Ocean")
    lava_reef = world.get_region("Lava Reef")
    metallic_madness = world.get_region("Metallic Madness")
    titanic_monarch = world.get_region("Titanic Monarch")
    special_stages = world.get_region("Special Stages")
    blue_spheres = world.get_region("Blue Spheres")
    egg_reverie = world.get_region("Egg Reverie")

    # Connecting the Menu to every single zone in the game with rule of needed each zone's key to enter the level
    menu.connect(green_hill, "Menu to Green Hill")
    menu.connect(chemical_plant, "Menu to Chemical Plant")
    menu.connect(studiopolis, "Menu to Studiopolis")
    menu.connect(flying_battery, "Menu to Flying Battery")
    menu.connect(press_garden, "Menu to Press Garden")
    menu.connect(stardust_speedway, "Menu to Stardust Speedway")
    menu.connect(hydro_city, "Menu to Hydro City")
    menu.connect(mirage_saloon, "Menu to Mirage Saloon")
    menu.connect(oil_ocean, "Menu to Oil Ocean")
    menu.connect(lava_reef, "Menu to Lava Reef")
    menu.connect(metallic_madness, "Menu to Metallic Madness")
    menu.connect(titanic_monarch, "Menu to Titanic Monarch")
    menu.connect(egg_reverie, "Menu to Egg Reverie")

    # Connecting every zone to the special stages since every zone has at least one special stage ring to enter
    green_hill.connect(special_stages, "Green Hill to Special Stages")
    chemical_plant.connect(special_stages, "Chemical Plant to Special Stages")
    studiopolis.connect(special_stages, "Studiopolis to Special Stages")
    flying_battery.connect(special_stages, "Flying Battery to Special Stages")
    press_garden.connect(special_stages, "Press Garden to Special Stages")
    stardust_speedway.connect(special_stages, "Stardust Speedway to Special Stages")
    hydro_city.connect(special_stages, "Hydro City to Special Stages")
    mirage_saloon.connect(special_stages, "Mirage Saloon to Special Stages")
    oil_ocean.connect(special_stages, "Oil Ocean to Special Stages")
    lava_reef.connect(special_stages, "Lava Reef to Special Stages")
    metallic_madness.connect(special_stages, "Metallic Madness to Special Stages")
    titanic_monarch.connect(special_stages, "Titanic Monarch to Special Stages")

    # Connecting every zone to Blue Spheres because every zone has at least one checkpoint to spawn a bonus ring to enter
    green_hill.connect(blue_spheres, "Green Hill to Blue Spheres")
    chemical_plant.connect(blue_spheres, "Chemical Plant to Blue Spheres")
    studiopolis.connect(blue_spheres, "Studiopolis to Blue Spheres")
    flying_battery.connect(blue_spheres, "Flying Battery to Blue Spheres")
    press_garden.connect(blue_spheres, "Press Garden to Blue Spheres")
    stardust_speedway.connect(blue_spheres, "Stardust Speedway to Blue Spheres")
    hydro_city.connect(blue_spheres, "Hydro City to Blue Spheres")
    mirage_saloon.connect(blue_spheres, "Mirage Saloon to Blue Spheres")
    oil_ocean.connect(blue_spheres, "Oil Ocean to Blue Spheres")
    lava_reef.connect(blue_spheres, "Lava Reef to Blue Spheres")
    metallic_madness.connect(blue_spheres, "Metallic Madness to Blue Spheres")
    titanic_monarch.connect(blue_spheres, "Titanic Monarch to Blue Spheres")