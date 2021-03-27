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

    def GenerateObjective(self):
        pass

    def GetDisplayName(self):
        return "empty trait"

    def GetAttributeModifiers(self):
        return self.attribute_modifier

    def GetCapabilities(self):
        return self.capabilities