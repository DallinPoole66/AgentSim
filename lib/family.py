'''
Family
    Tracks where the family house is from, hereditary traits, and name
'''
import agent
import relations as rel
import trait as ts


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

    members = list()

    def __init__(self, familyName = "Default", origin_location = None, traits = None):
        self.name = familyName
        self.origin_location = origin_location
        self.inherited_traits = traits
        self.members = list()

    def display(self):
        print(self.index, self.name)
        for member in self.members:
            print(member.name)