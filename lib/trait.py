'''
Trait

Provides a way to adjust an Agent's Attributes, generate primary level goals, and provide some capabilities.
Also represents some relationships such as an Agent being the father of another agent.
Used in a master table of Traits contained in an enum.
'''
import objective as obj
import capability as cap

class Trait:
    name = "trait name"
    owner_agent = None
    target_agent = None
    objective = None
    attribute_modifier = None
    capabilities = []


    def SetupTrait(self, owner):
        self.owner_agent = owner

    def SetupTrait(self, owner, target):
        self.owner_agent = owner
        self.target_agent = target

    def GenerateObjectives(self):
        objectives = list()

        return objectives

    def GetDisplayName(self):
        return "empty trait"

    def GetAttributeModifiers(self):
        return self.attribute_modifier

    def GetCapabilities(self):
        return self.capabilities


class trait_child_of_agent(Trait):
    def __init__(self, child_agent, parent_agent):
        self.owner_agent = child_agent
        self.target_agent = parent_agent

    def GetDisplayName(self):
        return "Child of " + self.target_agent.GetFullName()

class trait_parent_of_agent(Trait):
    def __init__(self, child_agent, parent_agent):
        self.owner_agent = parent_agent
        self.target_agent = child_agent
        
    def GetDisplayName(self):
        return "Parent of " + self.target_agent.GetFullName()

    def GenerateObjectives(self):
        objectives = list()
        objectives.append(obj.educate_child(self.target_agent))

        return objectives

class trait_married_to_agent(Trait):
    def __init__(self, agent, spouse):
        self.owner_agent = agent
        self.target_agent = spouse
        
    def GetDisplayName(self):        
        return "Spouse of " + self.target_agent.GetFullName()