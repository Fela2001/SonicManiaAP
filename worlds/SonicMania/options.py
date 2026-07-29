from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class GoalCondition(Choice):
    """
    What needs to be done to finish your game. Only one for now, more coming soon!

    Chaos Emerald Hunt: Find the seven chaos emeralds and collect "x" amount of Phantom Ruby Fragments to unlock Egg Reverie. Clear it to win!
    """

    display_name = "Goal"
    option_chaos_emerald_hunt = 0
    default = 0

class PhantomRubyFragmentsTotal(Range):
    """
    The elusive Phantom Ruby has somehow shattered into many pieces after the intro sequence of the game. This setting determines how many total pieces it shattered into. 
    """

    display_name = "Total Phantom Ruby Fragments"
    range_start = 10
    range_end = 100

    default = 50

class PhantomRubyFragmentsRequired(Range):
    """
    How many Phantom Ruby fragments do you need to access Egg Reverie.
    """

    display_name = "Required amount of Phantom Ruby Fragments"
    range_start = 10
    range_end = 90

    default = 30

class BlueSpheresPerfects(Toggle):
    """
    Looking for a "Perfect" way to play more Blue Spheres in runs? Turn on Perfect clears for 32 more checks to be added to the pool. Have fun!
    """

    display_name = "Blue Spheres Perfect Clears"


class SonicManiaPlusOptions(PerGameCommonOptions):
    goal_condition: GoalCondition
    phantom_ruby_total: PhantomRubyFragmentsTotal
    phantom_ruby_required: PhantomRubyFragmentsRequired
    blue_spheres_perfects: BlueSpheresPerfects

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [GoalCondition, PhantomRubyFragmentsTotal, PhantomRubyFragmentsRequired, BlueSpheresPerfects],
    ),
]

