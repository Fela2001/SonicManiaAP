from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SonicManiaPlusWorld


LOCATION_NAME_TO_ID = {
    "Sonic Green Hill Act 1 Clear": 1,
    "Sonic Green Hill Act 2 Clear": 2,
    "Sonic Chemical Plant Act 1 Clear": 3,
    "Sonic Chemical Plant Act 2 Clear": 4,
    "Sonic Studiopolis Act 1 Clear": 5,
    "Sonic Studiopolis Act 2 Clear": 6,
    "Sonic Flying Battery Act 1 Clear": 7,
    "Sonic Flying Battery Act 2 Clear": 8,
    "Sonic Press Garden Act 1 Clear": 9,
    "Sonic Press Garden Act 2 Clear": 10,
    "Sonic Stardust Speedway Act 1 Clear": 11,
    "Sonic Stardust Speedway Act 2 Clear": 12,
    "Sonic Hydro City Act 1 Clear": 13,
    "Sonic Hydro City Act 2 Clear": 14,
    "Sonic Mirage Saloon ST Act 1 Clear": 15,
    "Mirage Saloon K Act 1 Clear": 16,
    "Sonic Mirage Saloon Act 2 Clear": 17,
    "Sonic Oil Ocean Act 1 Clear": 18,
    "Sonic Oil Ocean Act 2 Clear": 19,
    "Sonic Lava Reef Act 1 Clear": 20,
    "Sonic Lava Reef Act 2 Clear": 21,
    "Sonic Metallic Madness Act 1 Clear": 22,
    "Sonic Metallic Madness Act 2 Clear": 23,
    "Sonic Titanic Monarch Act 1 Clear": 24,
    "Sonic Titanic Monarch Act 2 Clear": 25,
    "Special Ring near Knuckles Start in Green Hill Act 1": 26, # KNUCKLES ONLY
    "Special Ring in hidden waterfall cave in Green Hill Act 1": 27,
    "Special Ring in hidden cave near the end of Green Hill Act 1": 28,
    "Special Ring above s-shaped tube in the upper path of Green Hill Act 2": 29,
    "Special Ring below lake with a bridge in Green Hill Act 2": 30,
    "Special Ring in circular waterfall cave at the end of Green Hill Act 2": 31,
    "Special Ring hidden behind spring and gated walls in the upper path of Chemical Plant Act 1": 32,
    "Special Ring inside gated walls at the bottom of the first yellow block section in Chemical Plant Act 1": 33,
    "Special Ring in leftward mini area after a ramp launch in Chemical Plant Act 1": 34,
    "Special Ring inside gated walls at the bottom of the second and longer yellow block section in Chemical Plant Act 1": 35,
    "Special Ring right beside a sticky platform lift in Chemical Plant Act 2": 36,
    "Special Ring near the start of Chemical Plant Act 2 with floating platforms, bouncy floor and a sticky platform lift": 37,
    "Special Ring in a hidden area covered with yellow blocks near the end of Chemical Plant Act 2": 38,
    "Special Ring near the start of Studiopolis Act 1 behind yellow lit windows": 39,
    "Special Ring right above a Analog TV and right before a loop-de-loop in Studiopolis Act 1": 40,
    "Special Ring on the right of a ramp up from the lower path of Studiopolis Act 1": 41,
    "Special Ring on the upper path of Studiopolis Act 2 that's under an APPLAUSE sign": 42,
    "Special Ring to the left of two falling light platforms in Studiopolis Act 2": 43,
    "Special Ring reached by bouncing off three mic drops and jumping up three falling light platforms in Studiopolis Act 2": 44,
    "Special Ring hidden in leftward pathway reached by electric shield attraction or flight in Flying Battery Act 1": 45,
    "Special Ring hidden to the left near the end of Flying Battery Act 1": 46,
    "Special Ring to the left of the beginning of the lower path in Flying Battery Act 2": 47,
    "Special Ring reached by swinging between propellers and using fan platforms to reach a pulley in Flying Battery Act 2": 48,
    "Special Ring on the right of a pulley in Flying Battery Act 2": 49,
    "Special Ring in a optional outside ship area reached through electric shield attraction or flight in Flying Battery Act 2": 50,
    "Special Ring on the lower left near the start of Press Garden Act 1": 51,
    "Special Ring behind a gate that is opened by breaking the light in presser in the previous room in Press Garden Act 1": 52,
    "Special Ring hidden to the left of a pathway of pink trees in Press Garden Act 2": 53,
    "Special Ring above a frozen red spring in Press Garden Act 2": 54,
    "Special Ring right after ice blowing machine loop-de-loop in Press Garden Act 2": 55,
    "Special Ring between two pillars on the upper path early on in Stardust Speedway Act 1": 56,
    "Special Ring found by going left in one of the speed tunnels in Stardust Speedway Act 1": 57,
    "Special Ring reached by climbing the vine grown from a broken capsule and using the mid-air launcher to launch upwards in Stardust Speedway Act 1": 58,
    "Special Ring at the start of the lower path of Stardust Speedway Act 2": 59,
    "Special Ring in small enclosed area in the lower path of Stardust Speedway Act 2": 60,
    "Special Ring in small enclosed area in the upper path of Stardust Speedway Act 2": 61,
    "Special Ring above hand speed launcher and a ramp in Hydro City Act 1": 62,
    "Special Ring to the left of wavy tunnel that you downward into the water in Hydro City Act 1": 63,
    "Special Ring at the end of taking the lower tunnel path near the end of Hydro City Act 1": 64,
    "Special Ring to the bottom left of water running section in Hydro City Act 2": 65,
    "Special Ring to the right of one of the spiral blue tubes of Hydro City Act 2": 66,
    "Special Ring at left end of Eggman's train in Mirage Saloon ST Act 1": 67,
    "Special Ring near the bottom at the start of Mirage Saloon K Act 1": 68,
    "Special Ring to the left of two swings near the top of Mirage Saloon K Act 1": 69,
    "Special Ring down left of the floating pillars and barrels in Mirage Saloon K Act 1": 70,
    "Special Ring in the lower path of Mirage Saloon Act 2 that's reached with a path of water": 71,
    "Special Ring next to a sand loop in Mirage Saloon Act 2": 72,
    "Special Ring above a water sprayer and right of wanted posters in Mirage Saloon Act 2": 73,
    "Special Ring near the start of Oil Ocean Act 1 that is above five fans": 74,
    "Special Ring hidden to the top left above the first oil slides in Oil Ocean Act 1": 75,
    "Special Ring hidden to the right of a elevator in Oil Ocean Act 1": 76,
    "Special Ring under the first checkpoint in Oil Ocean Act 2": 77,
    "Special Ring to the top right of oil slides section before the large oil lake in Oil Ocean Act 2": 78,
    "Special Ring hidden to the left of the first rising and falling spike crusher in Lava Reef Act 1": 79,
    "Special Ring above two spin dash elevators in Lava Reef Act 1": 80,
    "Special Ring right below the first checkpoint in Lava Reef Act 2": 81,
    "Special Ring above two floating platforms and below a cylinder with revolving spike balls in Lava Reef Act 2": 82,
    "Special Ring in a hidden area that is above another hidden area with two item boxes in Lava Reef Act 2": 83,
    "Special Ring guarded by iwamodokis in a hidden hallway in Lava Reef Act 2": 84,
    "Special Ring at the end of a walking platform mech section in Lava Reef Act 2": 85,
    "Special Ring reached through bouncing on a red spring to run a half loop to the ring in Metallic Madness Act 1": 86,
    "Special Ring to the left reached from the upper path or using the third launcher in a background section in Metallic Madness Act 1": 87,
    "Special Ring hidden in a small area to the top right at the end of Metallic Madness Act 1": 88,
    "Special Ring at the end of a mini ray section in Metallic Madness Act 2": 89,
    "Special Ring reached by bouncing off a hidden red spring in a background shifter section in Metallic Madness Act 2": 90,
    "Special Ring nearby the second checkpoint that is above a magnetic orb in Titanic Monarch Act 1": 91, # KNUCKLES AND TAILS ONLY, make sure to keep that in mind for logic
    "Special Ring above a magnetic orb in a hidden tunnel that is left to a mini loop-de-loop in Titanic Monarch Act 1": 92,
    "Special Ring hidden behind breakable yellow bouncy bumpers in Titanic Monarch Act 2": 93,
    "Special Stage 1 Clear": 94,
    "Special Stage 2 Clear": 95,
    "Special Stage 3 Clear": 96,
    "Special Stage 4 Clear": 97,
    "Special Stage 5 Clear": 98,
    "Special Stage 6 Clear": 99,
    "Special Stage 7 Clear": 100,
    "Blue Spheres Stage 1 Clear": 101,
    "Blue Spheres Stage 2 Clear": 102,
    "Blue Spheres Stage 3 Clear": 103,
    "Blue Spheres Stage 4 Clear": 104,
    "Blue Spheres Stage 5 Clear": 105,
    "Blue Spheres Stage 6 Clear": 106,
    "Blue Spheres Stage 7 Clear": 107,
    "Blue Spheres Stage 8 Clear": 108,
    "Blue Spheres Stage 9 Clear": 109,
    "Blue Spheres Stage 10 Clear": 110,
    "Blue Spheres Stage 11 Clear": 111,
    "Blue Spheres Stage 12 Clear": 112,
    "Blue Spheres Stage 13 Clear": 113,
    "Blue Spheres Stage 14 Clear": 114,
    "Blue Spheres Stage 15 Clear": 115,
    "Blue Spheres Stage 16 Clear": 116,
    "Blue Spheres Stage 17 Clear": 117,
    "Blue Spheres Stage 18 Clear": 118,
    "Blue Spheres Stage 19 Clear": 119,
    "Blue Spheres Stage 20 Clear": 120,
    "Blue Spheres Stage 21 Clear": 121,
    "Blue Spheres Stage 22 Clear": 122,
    "Blue Spheres Stage 23 Clear": 123,
    "Blue Spheres Stage 24 Clear": 124,
    "Blue Spheres Stage 25 Clear": 125,
    "Blue Spheres Stage 26 Clear": 126,
    "Blue Spheres Stage 27 Clear": 127,
    "Blue Spheres Stage 28 Clear": 128,
    "Blue Spheres Stage 29 Clear": 129,
    "Blue Spheres Stage 30 Clear": 130,
    "Blue Spheres Stage 31 Clear": 131,
    "Blue Spheres Stage 32 Clear": 132,
    "Blue Spheres Stage 1 Perfect Clear": 133,
    "Blue Spheres Stage 2 Perfect Clear": 134,
    "Blue Spheres Stage 3 Perfect Clear": 135,
    "Blue Spheres Stage 4 Perfect Clear": 136,
    "Blue Spheres Stage 5 Perfect Clear": 137,
    "Blue Spheres Stage 6 Perfect Clear": 138,
    "Blue Spheres Stage 7 Perfect Clear": 139,
    "Blue Spheres Stage 8 Perfect Clear": 140,
    "Blue Spheres Stage 9 Perfect Clear": 141,
    "Blue Spheres Stage 10 Perfect Clear": 142,
    "Blue Spheres Stage 11 Perfect Clear": 143,
    "Blue Spheres Stage 12 Perfect Clear": 144,
    "Blue Spheres Stage 13 Perfect Clear": 145,
    "Blue Spheres Stage 14 Perfect Clear": 146,
    "Blue Spheres Stage 15 Perfect Clear": 147,
    "Blue Spheres Stage 16 Perfect Clear": 148,
    "Blue Spheres Stage 17 Perfect Clear": 149,
    "Blue Spheres Stage 18 Perfect Clear": 150,
    "Blue Spheres Stage 19 Perfect Clear": 151,
    "Blue Spheres Stage 20 Perfect Clear": 152,
    "Blue Spheres Stage 21 Perfect Clear": 153,
    "Blue Spheres Stage 22 Perfect Clear": 154,
    "Blue Spheres Stage 23 Perfect Clear": 155,
    "Blue Spheres Stage 24 Perfect Clear": 156,
    "Blue Spheres Stage 25 Perfect Clear": 157,
    "Blue Spheres Stage 26 Perfect Clear": 158,
    "Blue Spheres Stage 27 Perfect Clear": 159,
    "Blue Spheres Stage 28 Perfect Clear": 160,
    "Blue Spheres Stage 29 Perfect Clear": 161,
    "Blue Spheres Stage 30 Perfect Clear": 162,
    "Blue Spheres Stage 31 Perfect Clear": 163,
    "Blue Spheres Stage 32 Perfect Clear": 164,
    "Tails Green Hill Act 1 Clear": 165, # Add ALL of these locations from here to locations below
    "Tails Green Hill Act 2 Clear": 166,
    "Tails Chemical Plant Act 1 Clear": 167,
    "Tails Chemical Plant Act 2 Clear": 168,
    "Tails Studiopolis Act 1 Clear": 169,
    "Tails Studiopolis Act 2 Clear": 170,
    "Tails Flying Battery Act 1 Clear": 171,
    "Tails Flying Battery Act 2 Clear": 172,
    "Tails Press Garden Act 1 Clear": 173,
    "Tails Press Garden Act 2 Clear": 174,
    "Tails Stardust Speedway Act 1 Clear": 175,
    "Tails Stardust Speedway Act 2 Clear": 176,
    "Tails Hydro City Act 1 Clear": 177,
    "Tails Hydro City Act 2 Clear": 178,
    "Tails Mirage Saloon ST Act 1 Clear": 179,
    "Tails Mirage Saloon Act 2 Clear": 180,
    "Tails Oil Ocean Act 1 Clear": 181,
    "Tails Oil Ocean Act 2 Clear": 182,
    "Tails Lava Reef Act 1 Clear": 183,
    "Tails Lava Reef Act 2 Clear": 184,
    "Tails Metallic Madness Act 1 Clear": 185,
    "Tails Metallic Madness Act 2 Clear": 186,
    "Tails Titanic Monarch Act 1 Clear": 187,
    "Tails Titanic Monarch Act 2 Clear": 188,
}

class SonicManiaPlusLocation(Location):
    game = "Sonic Mania Plus"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: SonicManiaPlusWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: SonicManiaPlusWorld) -> None:
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

    green_hill_locations = get_location_names_with_ids(
        ["Sonic Green Hill Act 1 Clear", "Sonic Green Hill Act 2 Clear", "Special Ring near Knuckles Start in Green Hill Act 1", "Special Ring in hidden waterfall cave in Green Hill Act 1", 
         "Special Ring in hidden cave near the end of Green Hill Act 1", "Special Ring above s-shaped tube in the upper path of Green Hill Act 2", "Special Ring below lake with a bridge in Green Hill Act 2",
         "Special Ring in circular waterfall cave at the end of Green Hill Act 2"]
    )
    green_hill.add_locations(green_hill_locations, SonicManiaPlusLocation)

    chemical_plant_locations = get_location_names_with_ids(
        ["Sonic Chemical Plant Act 1 Clear", "Sonic Chemical Plant Act 2 Clear", "Special Ring hidden behind spring and gated walls in the upper path of Chemical Plant Act 1",
         "Special Ring inside gated walls at the bottom of the first yellow block section in Chemical Plant Act 1", "Special Ring in leftward mini area after a ramp launch in Chemical Plant Act 1", 
         "Special Ring inside gated walls at the bottom of the second and longer yellow block section in Chemical Plant Act 1", "Special Ring right beside a sticky platform lift in Chemical Plant Act 2", 
         "Special Ring near the start of Chemical Plant Act 2 with floating platforms, bouncy floor and a sticky platform lift", "Special Ring in a hidden area covered with yellow blocks near the end of Chemical Plant Act 2"]
    )
    chemical_plant.add_locations(chemical_plant_locations, SonicManiaPlusLocation)

    studiopolis_locations = get_location_names_with_ids(
        ["Sonic Studiopolis Act 1 Clear", "Sonic Studiopolis Act 2 Clear", "Special Ring near the start of Studiopolis Act 1 behind yellow lit windows", "Special Ring right above a Analog TV and right before a loop-de-loop in Studiopolis Act 1", 
         "Special Ring on the right of a ramp up from the lower path of Studiopolis Act 1", "Special Ring on the upper path of Studiopolis Act 2 that's under an APPLAUSE sign", 
         "Special Ring to the left of two falling light platforms in Studiopolis Act 2", "Special Ring reached by bouncing off three mic drops and jumping up three falling light platforms in Studiopolis Act 2"]
    )
    studiopolis.add_locations(studiopolis_locations, SonicManiaPlusLocation)

    flying_battery_locations = get_location_names_with_ids(
        ["Sonic Flying Battery Act 1 Clear", "Sonic Flying Battery Act 2 Clear", "Special Ring hidden in leftward pathway reached by electric shield attraction or flight in Flying Battery Act 1", 
         "Special Ring hidden to the left near the end of Flying Battery Act 1", "Special Ring to the left of the beginning of the lower path in Flying Battery Act 2", 
         "Special Ring reached by swinging between propellers and using fan platforms to reach a pulley in Flying Battery Act 2", "Special Ring on the right of a pulley in Flying Battery Act 2", 
         "Special Ring in a optional outside ship area reached through electric shield attraction or flight in Flying Battery Act 2"]
    )
    flying_battery.add_locations(flying_battery_locations, SonicManiaPlusLocation)

    press_garden_locations = get_location_names_with_ids(
        ["Sonic Press Garden Act 1 Clear", "Sonic Press Garden Act 2 Clear", "Special Ring on the lower left near the start of Press Garden Act 1", 
         "Special Ring behind a gate that is opened by breaking the light in presser in the previous room in Press Garden Act 1", "Special Ring hidden to the left of a pathway of pink trees in Press Garden Act 2", 
         "Special Ring above a frozen red spring in Press Garden Act 2", "Special Ring right after ice blowing machine loop-de-loop in Press Garden Act 2"]
    )
    press_garden.add_locations(press_garden_locations, SonicManiaPlusLocation)

    stardust_speedway_locations = get_location_names_with_ids(
        ["Sonic Stardust Speedway Act 1 Clear", "Sonic Stardust Speedway Act 2 Clear", "Special Ring between two pillars on the upper path early on in Stardust Speedway Act 1", 
         "Special Ring found by going left in one of the speed tunnels in Stardust Speedway Act 1", 
         "Special Ring reached by climbing the vine grown from a broken capsule and using the mid-air launcher to launch upwards in Stardust Speedway Act 1", 
         "Special Ring at the start of the lower path of Stardust Speedway Act 2", "Special Ring in small enclosed area in the lower path of Stardust Speedway Act 2", 
         "Special Ring in small enclosed area in the upper path of Stardust Speedway Act 2"]
    )
    stardust_speedway.add_locations(stardust_speedway_locations, SonicManiaPlusLocation)

    hydro_city_locations = get_location_names_with_ids(
        ["Sonic Hydro City Act 1 Clear", "Sonic Hydro City Act 2 Clear", "Special Ring above hand speed launcher and a ramp in Hydro City Act 1", 
         "Special Ring to the left of wavy tunnel that you downward into the water in Hydro City Act 1", "Special Ring at the end of taking the lower tunnel path near the end of Hydro City Act 1", 
         "Special Ring to the bottom left of water running section in Hydro City Act 2", "Special Ring to the right of one of the spiral blue tubes of Hydro City Act 2"]
    )
    hydro_city.add_locations(hydro_city_locations, SonicManiaPlusLocation)

    mirage_saloon_locations = get_location_names_with_ids(
        ["Sonic Mirage Saloon ST Act 1 Clear", "Mirage Saloon K Act 1 Clear", "Sonic Mirage Saloon Act 2 Clear", "Special Ring at left end of Eggman's train in Mirage Saloon ST Act 1", 
         "Special Ring near the bottom at the start of Mirage Saloon K Act 1", "Special Ring to the left of two swings near the top of Mirage Saloon K Act 1", 
         "Special Ring down left of the floating pillars and barrels in Mirage Saloon K Act 1", "Special Ring in the lower path of Mirage Saloon Act 2 that's reached with a path of water", 
         "Special Ring next to a sand loop in Mirage Saloon Act 2", "Special Ring above a water sprayer and right of wanted posters in Mirage Saloon Act 2"]
    )
    mirage_saloon.add_locations(mirage_saloon_locations, SonicManiaPlusLocation)

    oil_ocean_locations = get_location_names_with_ids(
        ["Sonic Oil Ocean Act 1 Clear", "Sonic Oil Ocean Act 2 Clear", "Special Ring near the start of Oil Ocean Act 1 that is above five fans", 
         "Special Ring hidden to the top left above the first oil slides in Oil Ocean Act 1", "Special Ring hidden to the right of a elevator in Oil Ocean Act 1", 
         "Special Ring under the first checkpoint in Oil Ocean Act 2", "Special Ring to the top right of oil slides section before the large oil lake in Oil Ocean Act 2"]
    )
    oil_ocean.add_locations(oil_ocean_locations, SonicManiaPlusLocation)

    lava_reef_locations = get_location_names_with_ids(
        ["Sonic Lava Reef Act 1 Clear", "Sonic Lava Reef Act 2 Clear", "Special Ring hidden to the left of the first rising and falling spike crusher in Lava Reef Act 1",
         "Special Ring above two spin dash elevators in Lava Reef Act 1", "Special Ring right below the first checkpoint in Lava Reef Act 2", 
         "Special Ring above two floating platforms and below a cylinder with revolving spike balls in Lava Reef Act 2", 
         "Special Ring in a hidden area that is above another hidden area with two item boxes in Lava Reef Act 2", "Special Ring guarded by iwamodokis in a hidden hallway in Lava Reef Act 2", 
         "Special Ring at the end of a walking platform mech section in Lava Reef Act 2"]
    )
    lava_reef.add_locations(lava_reef_locations, SonicManiaPlusLocation)

    metallic_madness_locations = get_location_names_with_ids(
        ["Sonic Metallic Madness Act 1 Clear", "Sonic Metallic Madness Act 2 Clear", "Special Ring reached through bouncing on a red spring to run a half loop to the ring in Metallic Madness Act 1", 
         "Special Ring to the left reached from the upper path or using the third launcher in a background section in Metallic Madness Act 1", 
         "Special Ring hidden in a small area to the top right at the end of Metallic Madness Act 1", "Special Ring at the end of a mini ray section in Metallic Madness Act 2", 
         "Special Ring reached by bouncing off a hidden red spring in a background shifter section in Metallic Madness Act 2"]
    )
    metallic_madness.add_locations(metallic_madness_locations, SonicManiaPlusLocation)

    titanic_monarch_locations = get_location_names_with_ids(
        ["Sonic Titanic Monarch Act 1 Clear", "Sonic Titanic Monarch Act 2 Clear", "Special Ring nearby the second checkpoint that is above a magnetic orb in Titanic Monarch Act 1", 
         "Special Ring above a magnetic orb in a hidden tunnel that is left to a mini loop-de-loop in Titanic Monarch Act 1", 
         "Special Ring hidden behind breakable yellow bouncy bumpers in Titanic Monarch Act 2"]
    )
    titanic_monarch.add_locations(titanic_monarch_locations, SonicManiaPlusLocation)

    special_stages_locations = get_location_names_with_ids(
        ["Special Stage 1 Clear", "Special Stage 2 Clear", "Special Stage 3 Clear", "Special Stage 4 Clear", 
         "Special Stage 5 Clear", "Special Stage 6 Clear", "Special Stage 7 Clear"]
    )
    special_stages.add_locations(special_stages_locations, SonicManiaPlusLocation)

    blue_spheres_locations = get_location_names_with_ids(
        ["Blue Spheres Stage 1 Clear", "Blue Spheres Stage 2 Clear", "Blue Spheres Stage 3 Clear", "Blue Spheres Stage 4 Clear", "Blue Spheres Stage 5 Clear", 
         "Blue Spheres Stage 6 Clear", "Blue Spheres Stage 7 Clear", "Blue Spheres Stage 8 Clear", "Blue Spheres Stage 9 Clear", "Blue Spheres Stage 10 Clear", 
         "Blue Spheres Stage 11 Clear", "Blue Spheres Stage 12 Clear", "Blue Spheres Stage 13 Clear", "Blue Spheres Stage 14 Clear", "Blue Spheres Stage 15 Clear", 
         "Blue Spheres Stage 16 Clear", "Blue Spheres Stage 17 Clear", "Blue Spheres Stage 18 Clear", "Blue Spheres Stage 19 Clear", "Blue Spheres Stage 20 Clear",
         "Blue Spheres Stage 21 Clear", "Blue Spheres Stage 22 Clear", "Blue Spheres Stage 23 Clear", "Blue Spheres Stage 24 Clear" "Blue Spheres Stage 25 Clear", 
         "Blue Spheres Stage 26 Clear", "Blue Spheres Stage 27 Clear", "Blue Spheres Stage 28 Clear", "Blue Spheres Stage 29 Clear", "Blue Spheres Stage 30 Clear", 
         "Blue Spheres Stage 31 Clear", "Blue Spheres Stage 32 Clear"]
    )
    blue_spheres.add_locations(blue_spheres_locations, SonicManiaPlusLocation)

    if world.options.blue_spheres_perfects:
        perfect_spheres_locations = get_location_names_with_ids(
            ["Blue Spheres Stage 1 Perfect Clear", "Blue Spheres Stage 2 Perfect Clear", "Blue Spheres Stage 3 Perfect Clear", "Blue Spheres Stage 4 Perfect Clear", 
             "Blue Spheres Stage 5 Perfect Clear", "Blue Spheres Stage 6 Perfect Clear", "Blue Spheres Stage 7 Perfect Clear", "Blue Spheres Stage 8 Perfect Clear", 
             "Blue Spheres Stage 9 Perfect Clear", "Blue Spheres Stage 10 Perfect Clear", "Blue Spheres Stage 11 Perfect Clear", "Blue Spheres Stage 12 Perfect Clear", 
             "Blue Spheres Stage 13 Perfect Clear", "Blue Spheres Stage 14 Perfect Clear", "Blue Spheres Stage 15 Perfect Clear", "Blue Spheres Stage 16 Perfect Clear",
             "Blue Spheres Stage 17 Perfect Clear", "Blue Spheres Stage 18 Perfect Clear", "Blue Spheres Stage 19 Perfect Clear", "Blue Spheres Stage 20 Perfect Clear", 
             "Blue Spheres Stage 21 Perfect Clear", "Blue Spheres Stage 22 Perfect Clear", "Blue Spheres Stage 23 Perfect Clear", "Blue Spheres Stage 24 Perfect Clear", 
             "Blue Spheres Stage 25 Perfect Clear", "Blue Spheres Stage 26 Perfect Clear", "Blue Spheres Stage 27 Perfect Clear", "Blue Spheres Stage 28 Perfect Clear", 
             "Blue Spheres Stage 29 Perfect Clear", "Blue Spheres Stage 30 Perfect Clear", "Blue Spheres Stage 31 Perfect Clear", "Blue Spheres Stage 32 Perfect Clear"]
        )
        blue_spheres.add_locations(perfect_spheres_locations, SonicManiaPlusLocation)

def create_events():
    egg_reverie = world.get_region("Egg Reverie")

    egg_reverie.add_event(
        "Egg Reverie Clear", "Game Clear", location_type=SonicManiaPlusLocation, item_type=SonicManiaPlusItem
    )
    
