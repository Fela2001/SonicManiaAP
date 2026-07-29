from collections.abc import Mapping
from worlds.AutoWorld import World

from . import items, locations, regions, rules
from . import options as sonicmaniaplus_options

class SonicManiaPlusWorld(World):
    """ 
    Sonic Mania Plus is a high-speed 2D action platformer. 
    Play as Sonic, Tails, Knuckles, Mighty and Ray across 28 stages to stop Dr. Eggman from taking over the world!
    """

    game = "Sonic Mania Plus"

    options_dataclass = sonicmaniaplus_options.SonicManiaPlusOptions
    options: sonicmaniaplus_options.SonicManiaPlusOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.SonicManiaPlusItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "goal_condition", "phantom_ruby_total", "phantom_ruby_required", "blue_spheres_perfects"
        )