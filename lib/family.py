'''
Family
    Tracks where the family house is from, hereditary traits, and name
'''
import agent
import relations as rel
import trait as ts
import random

class Icon():
    name = ""
    min_count = 1
    max_count = None
    descriptors = None

    def __init__(self, name,min_count ,max_count , descriptors):
        self.name = name
        self.max_count = max_count
        self.min_count = min_count
        self.descriptors = descriptors

ICONS = (
    Icon("Crosses", max_count = 7, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Stars", max_count = 7, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Rings", max_count = 7, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Crescents", max_count = 7, min_count=2, descriptors=("Centered", "Offset", "Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Diamonds", max_count = 7, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Flowers", max_count = 7, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Lions", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Dogs", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant", "Three-Headed")),
    Icon("Rabbits", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Eagles", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant", "Displayed")),
    Icon("Wolves", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Fish", max_count = 7, min_count=1, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Owls", max_count = 6, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Elk", max_count = 4, min_count=1, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Bulls", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Horses", max_count = 6, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Ravens", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant", "Displayed")),
    Icon("Swords", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Hammers", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Daggers", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Arrows", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally")),
    Icon("Dragons", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Griffens", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Manticore", max_count = 1, min_count=1, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Cockatrice", max_count = 4, min_count=1, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Kraken", max_count = 4, min_count=1, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Badgers", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Bees", max_count = 4, min_count=2, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally", "Rampant", "Standing", "Passant")),
    Icon("Locust", max_count = 9, min_count=1, descriptors=("Centered", "Offset","Stacked Vertically", "Horizonal", "Diagonally"))
)

crest_colors = ("Gules", "Azure", "Vert", "Sable", "Purpure")
metal_colors = ("Or", "Argent")
ordinaries = ("Fess", "Pale", "Bend", "Chevron", "Cross", "Saltire", "Chief", "Bordure", "Pile")

class FamilyCrest():
    color = ""
    ordinary = ""
    ordinary_color = ""
    icon = ""
    icon_count = 1
    icon_desc = ""
    crest_desc = "{icon_count} {icon} {desc} on a {ordinary_color} {ordinary} with a background of {color}."
    def __init__(self):
        if random.randrange(1):
            self.color = crest_colors[random.randrange(len(crest_colors))]
            self.ordinary_color = metal_colors[random.randrange(len(metal_colors))]
        else:
            self.ordinary_color = crest_colors[random.randrange(len(crest_colors))]
            self.color = metal_colors[random.randrange(len(metal_colors))]
        i = ICONS[random.randrange(len(ICONS))]
        self.icon = i.name
        self.icon_count = random.randrange(i.min_count, i.max_count)
        self.icon_desc = i.descriptors[random.randrange(len(i.descriptors))]
        self.ordinary = ordinaries[random.randrange(len(ordinaries))]
    
    def GetCrestDescription(self):
        return self.crest_desc.format(icon_count = self.icon_count, desc=self.icon_desc, icon=self.icon, ordinary_color = self.ordinary_color, ordinary = self.ordinary, color = self.color)

def MarryAgents(agent_a, agent_b):
    agent_a.AddTrait(ts.trait_married_to_agent(agent_a, agent_b))
    agent_b.AddTrait(ts.trait_married_to_agent(agent_b, agent_a))

FAMILIES = list()

def AddFamily(family):
    family.index = len(FAMILIES)
    FAMILIES.append(family)
    print("Adding Family:")
    family.display()

def AddFamilyMember(familyIndex, newMember):
    if familyIndex < len(FAMILIES):
        print("Adding {0} to Family: {1}".format(newMember.name, FAMILIES[familyIndex].name))
        FAMILIES[familyIndex].members.append(newMember)
        newMember.family = familyIndex

class Family():
    index = 0
    name = "Last Name"
    # Where the family originates from
    origin_location = None
    # Hereditary Traits with chance of occurance
    inherited_traits = []
    crest = None
    members = list()

    def __init__(self, familyName = "Default", origin_location = None, traits = None):
        self.name = familyName
        self.origin_location = origin_location
        self.inherited_traits = traits
        self.members = list()
        self.crest = FamilyCrest()
        print( self.crest.GetCrestDescription())

    def display(self):
        print(self.index, self.name)
        for member in self.members:
            print(member.name)