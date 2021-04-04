'''
A data structure to help referencing what territory a kingdom holds and who holds the major offices.
'''

'''
A king rules a Kingdom. No where to go but down. Chooses advisors based on relationships. May also lift up any agent to a higher class if relationship high enough.
A lord rules a territory. May become King if the current monarch is dethroned. May initiate civil wars, work with other lords to ensure loyalty and engage in international plots.
A vassal rules a town. A vassal can become a lord if they marry into a noble family, have a good relationship to the king. Capable of choosing sides in a conflict.
A Merchant can move between towns. A Merchant can become a vassal if close to a lord or king and has enough wealth.
A peasant is bound to the lord of the territory and is assigned their work. A child may escape the Peasant class if taken on as an apprentice to a Merchant.
'''

'''
Structure
Provides functionality to a location
'''
class Structure():
    name = ""
    max_workers = None
    def GenerateResources(self, location):
        pass


'''
Location
Smallest unit of location class.
tracks a bare minimum
may be used to represent old ruins, camps, wilderness
can be upgraded into a town with enough population and a town center

Town
Tracks the general terrain surrounding the location.
Size can change over time as population increases.
If the location cannot afford the upkeep the town will decay into partial ruins
Ruins don't offer any additional services but can be more easily repaired than building from scratch
During combat, the town will lose parts to ruins and ruins to desolation.
Desolation requires resources to clear away before the town can once again use that area.

'''
class Location():
    name = ""
    # What territory this location is in
    territory = None
    # list of the current agents in the town
    agents = list()
    # Structures is a list of buildings in the town. A town hall is the first building to be built
    structures = None
    # Wealth within the town's vaults. Abstracts gold, gems and other valuables
    wealth = None

    # Materials
    # Keep track of basic resources like wood, food, stone
    wood = None
    stone = None
    food = None
    metal = None

    # The vassal is the ruler of the town
    vassal = None

    # Policies are set by the vassal and determine some general laws for the town
    # Things like taxes, prison time for minor crimes, and current employment strategy.
    policies = None

    # Employment strategy can be things like focusing villager efforts towards Agriculture, Mining, Lumber
    # Can also be for things like increasing the number of Guards, or raising men that are of military age to arms for their Nobility
    employment_strategy = None





'''
Defines a general area that can contain multiple towns
'''
class territory():
    name = ""
    kingdom = None
    lord = None
    locations = None


'''
A political oranization that claims locations
The capitol is a town that acts as the royal center. Storing the kingdoms wealth and houses the kings family
Uses the Monarch's crest as the kingdom's crest.
'''
class kingdom():
    name = ""
    monarch = None
    royal_family = None
    capitol = None
    territories = None
    # if True, the claim to the throne goes to the monarch's oldest son, or to the husband of the oldest daughter if no son.
    # if false, the claim to the throne goes to the monarch's oldest daughter, or to the wife of the oldest son if no daughters.
    # if no children, the monarchy is up for grabs by the noble families. Once one noble has 2/3 support of the nobile family heads they are made monarch.
    is_paternal = True