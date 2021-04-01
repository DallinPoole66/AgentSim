'''
Family
    Tracks where the family house is from, hereditary traits, and name
'''
import agent
import relations as rel

class parent_of (rel.Relation):
    def display(self): 
        return "Parent of " + self.target_agent.GetFullName()

class child_of (rel.Relation):
    def display(self): 
        return "Child of " + self.target_agent.GetFullName()

class spouse_of (rel.Relation):
    def display(self): 
        return "Spouse of " + self.target_agent.GetFullName()
    def __init__(self, owner, target):
        self.owner_agent = owner
        self.target_agent = target

def MarryAgents(agent_a, agent_b):
    rel_a = spouse_of(agent_a, agent_b)
    agent_a.AddRelation(rel_a)
    rel_b = spouse_of(agent_b, agent_a)
    agent_b.AddRelation(rel_b)

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