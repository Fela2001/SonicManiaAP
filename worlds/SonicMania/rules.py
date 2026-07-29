from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import SonicManiaPlusWorld

HAS_KEY = Has("Key")

def set_all_rules (world: SonicManiaPlusWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: SonicManiaPlusWorld) -> None:
    menu_to_green_hill = world.get_entrance("Menu to Green Hill")
    menu_to_chemical_plant = world.get_entrance("Menu to Chemical Plant")
    menu_to_studiopolis = world.get_entrance("Menu to Studiopolis")
    menu_to_flying_battery = world.get_entrance("Menu to Flying Battery")
    menu_to_press_garden = world.get_entrance("Menu to Press Garden")
    menu_to_stardust_speedway = world.get_entrance("Menu to Stardust Speedway")
    menu_to_hydro_city = world.get_entrance("Menu to Hydro City")
    menu_to_mirage_saloon = world.get_entrance("Menu to Mirage Saloon")
    menu_to_oil_ocean = world.get_entrance("Menu to Oil Ocean")
    menu_to_lava_reef = world.get_entrance("Menu to Lava Reef")
    menu_to_metallic_madness = world.get_entrance("Menu to Metallic Madness")
    menu_to_titanic_monarch = world.get_entrance("Menu to Titanic Monarch")
    menu_to_egg_reverie = world.get_entrance("Menu to Egg Reverie")

    green_hill_to_special_stages = world.get_entrance("Green Hill to Special Stages")
    chemical_plant_to_special_stages = world.get_entrance("Chemical Plant to Special Stages")
    studiopolis_to_special_stages = world.get_entrance("Studiopolis to Special Stages")
    flying_battery_to_special_stages = world.get_entrance("Flying Battery to Special Stages")
    press_garden_to_special_stages = world.get_entrance("Press Garden to Special Stages")
    stardust_speedway_to_special_stages = world.get_entrance("Stardust Speedway to Special Stages")
    hydro_city_to_special_stages = world.get_entrance("Hydro City to Special Stages")
    mirage_saloon_to_special_stages = world.get_entrance("Mirage Saloon to Special Stages")
    oil_ocean_to_special_stages = world.get_entrance("Oil Ocean to Special Stages")
    lava_reef_to_special_stages = world.get_entrance("Lava Reef to Special Stages")
    metallic_madness_to_special_stages = world.get_entrance("Metallic Madness to Special Stages")
    titanic_monarch_to_special_stages = world.get_entrance("Titanic Monarch to Special Stages")

    green_hill_to_blue_spheres = world.get_entrance("Green Hill to Blue Spheres")
    chemical_plant_to_blue_spheres = world.get_entrance("Chemical Plant to Blue Spheres")
    studiopolis_to_blue_spheres = world.get_entrance("Studiopolis to Blue Spheres")
    flying_battery_to_blue_spheres = world.get_entrance("Flying Battery to Blue Spheres")
    press_garden_to_blue_spheres = world.get_entrance("Press Garden to Blue Spheres")
    stardust_speedway_to_blue_spheres = world.get_entrance("Stardust Speedway to Blue Spheres")
    hydro_city_to_blue_spheres = world.get_entrance("Hydro City to Blue Spheres")
    mirage_saloon_to_blue_spheres = world.get_entrance("Mirage Saloon to Blue Spheres")
    oil_ocean_to_blue_spheres = world.get_entrance("Oil Ocean to Blue Spheres")
    lava_reef_to_blue_spheres = world.get_entrance("Lava Reef to Blue Spheres")
    metallic_madness_to_blue_spheres = world.get_entrance("Metallic Madness to Blue Spheres")
    titanic_monarch_to_blue_spheres = world.get_entrance("Titanic Monarch to Blue Spheres")

    # Getting the required amount of Phantom Ruby Fragments from player's option page
    fragments_required = world.options.phantom_ruby_required

    can_play_GHZ = Has("Green Hill Key")
    can_play_CPZ = Has("Chemical Plant Key")
    can_play_SZ = Has("Studiopolis Key")
    can_play_FBZ = Has("Flying Battery Key")
    can_play_PGZ = Has("Press Garden Key")
    can_play_SSZ = Has("Stardust Speedway Key")
    can_play_HCZ = Has("Hydro City Key")
    can_play_MSZ = Has("Mirage Saloon Key")
    can_play_OOZ = Has("Oil Ocean Key")
    can_play_LRZ = Has("Lava Reef Key")
    can_play_MMZ = Has("Metallic Madness Key")
    can_play_TMZ = Has("Titanic Monarch Key")
    can_play_ERZ = (
        Has("Green Chaos Emerald") & Has("Yellow Chaos Emerald") & Has("Blue Chaos Emerald") & Has("Purple Chaos Emerald") 
        & Has("White Chaos Emerald") & Has("Cyan Chaos Emerald") & Has("Red Chaos Emerald") & Has("Phantom Ruby Fragment", count=fragments_required)
    )

    can_play_special = (
        Has("Green Hill Key") | Has("Chemical Plant Key") | Has("Studiopolis Key") | Has("Flying Battery Key") | Has("Press Garden Key") 
        | Has("Stardust Speedway Key") | Has("Hydro City Key") | Has("Mirage Saloon Key") | Has("Oil Ocean Key") | Has("Lava Reef Key") | Has("Metallic Madness Key") | Has("Titanic Monarch Key")
    )

    can_play_blue_spheres = (
        Has("Green Hill Key") | Has("Chemical Plant Key") | Has("Studiopolis Key") | Has("Flying Battery Key") | Has("Press Garden Key") 
        | Has("Stardust Speedway Key") | Has("Hydro City Key") | Has("Mirage Saloon Key") | Has("Oil Ocean Key") | Has("Lava Reef Key") | Has("Metallic Madness Key") | Has("Titanic Monarch Key")
    )

    # Key Checks for Zone Entrances
    world.set_rule(menu_to_green_hill, can_play_GHZ)
    world.set_rule(menu_to_chemical_plant, can_play_CPZ)
    world.set_rule(menu_to_studiopolis, can_play_SZ)
    world.set_rule(menu_to_flying_battery, can_play_FBZ)
    world.set_rule(menu_to_press_garden, can_play_PGZ)
    world.set_rule(menu_to_stardust_speedway, can_play_SSZ)
    world.set_rule(menu_to_hydro_city, can_play_HCZ)
    world.set_rule(menu_to_mirage_saloon, can_play_MSZ)
    world.set_rule(menu_to_oil_ocean, can_play_OOZ)
    world.set_rule(menu_to_lava_reef, can_play_LRZ)
    world.set_rule(menu_to_metallic_madness, can_play_MMZ)
    world.set_rule(menu_to_titanic_monarch, can_play_TMZ)
    world.set_rule(menu_to_egg_reverie, can_play_ERZ)

    world.set_rule(green_hill_to_special_stages, can_play_special)
    world.set_rule(chemical_plant_to_special_stages, can_play_special)
    world.set_rule(studiopolis_to_special_stages, can_play_special)
    world.set_rule(flying_battery_to_special_stages, can_play_special)
    world.set_rule(press_garden_to_special_stages, can_play_special)
    world.set_rule(stardust_speedway_to_special_stages, can_play_special)
    world.set_rule(hydro_city_to_special_stages, can_play_special)
    world.set_rule(mirage_saloon_to_special_stages, can_play_special)
    world.set_rule(oil_ocean_to_special_stages, can_play_special)
    world.set_rule(lava_reef_to_special_stages, can_play_special)
    world.set_rule(metallic_madness_to_special_stages, can_play_special)
    world.set_rule(titanic_monarch_to_special_stages, can_play_special)

    world.set_rule(green_hill_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(chemical_plant_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(studiopolis_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(flying_battery_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(press_garden_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(stardust_speedway_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(hydro_city_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(mirage_saloon_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(oil_ocean_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(lava_reef_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(metallic_madness_to_blue_spheres, can_play_blue_spheres)
    world.set_rule(titanic_monarch_to_blue_spheres, can_play_blue_spheres)


def set_all_location_rules(world: SonicManiaPlusWorld) -> None:
    menu_to_green_hill = world.get_entrance("Menu to Green Hill")


def set_completion_condition(world: SonicManiaPlusWorld) -> None:
    world.set_completion_rule(Has("Game Clear"))