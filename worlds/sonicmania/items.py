from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SonicManiaPlusWorld

ITEM_NAME_TO_ID = {
    "Phantom Ruby Fragment": 1, # Figure how to make multiples
    "Green Chaos Emerald": 2,
    "Yellow Chaos Emerald": 3,
    "Blue Chaos Emerald": 4,
    "Purple Chaos Emerald": 5,
    "White Chaos Emerald": 6,
    "Cyan Chaos Emerald": 7,
    "Red Chaos Emerald": 8,
    "Green Hill Key": 9,
    "Chemical Plant Key": 10,
    "Studiopolis Key": 11,
    "Flying Battery Key": 12,
    "Press Garden Key": 13,
    "Stardust Speedway Key": 14,
    "Hydro City Key": 15,
    "Mirage Saloon Key": 16,
    "Oil Ocean Key": 17,
    "Lava Reef Key": 18, 
    "Metallic Madness Key": 19,
    "Titanic Monarch Key": 20,
    "Extra Life": 21,
    "Bubble Shield": 22,
    "Fire Shield": 23,
    "Hyper Ring": 24,
    "Invincible": 25,
    "Lightning Shield": 26,
    "Power Sneakers": 27,
    "Shield": 28,
    "Super Ring": 29
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Phantom Ruby Fragment": ItemClassification.progression,
    "Green Chaos Emerald": ItemClassification.progression | ItemClassification.useful,
    "Yellow Chaos Emerald": ItemClassification.progression | ItemClassification.useful,
    "Blue Chaos Emerald": ItemClassification.progression | ItemClassification.useful,
    "Purple Chaos Emerald": ItemClassification.progression | ItemClassification.useful,
    "White Chaos Emerald": ItemClassification.progression | ItemClassification.useful,
    "Cyan Chaos Emerald": ItemClassification.progression | ItemClassification.useful,
    "Red Chaos Emerald": ItemClassification.progression | ItemClassification.useful,
    "Green Hill Key": ItemClassification.progression,
    "Chemical Plant Key": ItemClassification.progression,
    "Studiopolis Key": ItemClassification.progression,
    "Flying Battery Key": ItemClassification.progression,
    "Press Garden Key": ItemClassification.progression,
    "Stardust Speedway Key": ItemClassification.progression,
    "Hydro City Key": ItemClassification.progression,
    "Mirage Saloon Key": ItemClassification.progression,
    "Oil Ocean Key": ItemClassification.progression,
    "Lava Reef Key": ItemClassification.progression,
    "Metallic Madness Key": ItemClassification.progression,
    "Titanic Monarch Key": ItemClassification.progression,
    "Extra Life": ItemClassification.filler,
    "Bubble Shield": ItemClassification.filler,
    "Fire Shield": ItemClassification.filler,
    "Hyper Ring": ItemClassification.filler,
    "Invincible": ItemClassification.filler,
    "Lightning Shield": ItemClassification.filler,
    "Power Sneakers": ItemClassification.filler,
    "Shield": ItemClassification.filler,
    "Super Ring": ItemClassification.filler
}

class SonicManiaPlusItem(Item):
    game = "Sonic Mania Plus"

def get_random_filler_item_name(world: SonicManiaPlusWorld) -> str:
    random = world.random.randint(1, 9)

    match random:
        case 1:
            return "Extra Life"
        case 2:
            return "Bubble Shield"
        case 3:
            return "Fire Shield"
        case 4:
            return "Hyper Ring"
        case 5:
            return "Invincible"
        case 6:
            return "Lightning Shield"
        case 7:
            return "Power Sneakers"
        case 8:
            return "Shield"
        case 9:
            return "Super Ring"


def create_item_with_correct_classification(world: SonicManiaPlusWorld, name: str) -> SonicManiaPlusItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return SonicManiaPlusItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: SonicManiaPlusWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Green Chaos Emerald"),
        world.create_item("Yellow Chaos Emerald"),
        world.create_item("Blue Chaos Emerald"),
        world.create_item("Purple Chaos Emerald"),
        world.create_item("White Chaos Emerald"),
        world.create_item("Cyan Chaos Emerald"),
        world.create_item("Red Chaos Emerald"),
        world.create_item("Green Hill Key"),
        world.create_item("Chemical Plant Key"),
        world.create_item("Studiopolis Key"),
        world.create_item("Flying Battery Key"),
        world.create_item("Press Garden Key"),
        world.create_item("Stardust Speedway Key"),
        world.create_item("Hydro City Key"),
        world.create_item("Mirage Saloon Key"),
        world.create_item("Oil Ocean Key"),
        world.create_item("Lava Reef Key"),
        world.create_item("Metallic Madness Key"),
        world.create_item("Titanic Monarch Key"),
    ]

    # The appending of the total amount of phantom ruby fragments from the player's options
    fragments_total = world.options.phantom_ruby_total
    itempool += [world.create_item("Phantom Ruby Fragment") for _ in range(fragments_total)]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool