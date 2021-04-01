'''
    Agent
    Represents an indivual person. Contains their attributes, traits, objectives, and relationships with other agents.
    Agents all have a current location, a morality, and a bias towards order or chaos.
'''
import copy
import attributes as atr
import trait as ts
import capability as cap
import objective as obj
import relations as rel
import family as fm
import attributes as atr
import enum
import relations as rel

class Gender(enum.Enum):
    Female = 0
    Male = 1
    NonBinary = 2 


class SexOrientation(enum.Enum):
    Straight = 0
    Gay = 1
    Bi = 2
    ASexual = 3


class Agent():
    # First Name
    name = "Agent Name"
    # Family
    family = None
    # Current location
    location = None
    # Age
    age = 18
    # Gender
    gender = Gender.Female
    # Sexual Orientation
    sex_orientation = SexOrientation.Straight
    # Traits
    traits = []
    # Attributes
    attributes = atr.Attributes()
    # Morality, 0 = Evil, 100 = Good
    morality = 50
    # lawful, 0 = Chaotic, 100 = Lawful
    lawful = 80

    parents = None
    children = None
    siblings = None
    relations = None
    

    def AddParent(self, parent_agent):
        self.parents.append(parent_agent)
        relation = fm.child_of("")
        relation.target_agent = parent_agent
        relation.owner_agent = self
        self.AddRelation(relation)

    def AddSibling(self, sibling_agent):
        self.siblings.append(sibling_agent)
        self.AddRelation(rel.Relation("Sibling of Agent"))

    def AddChild(self, child_agent):
        for sibling in self.children:
            sibling.AddSibling(child_agent)
            child_agent.AddSibling(sibling)
        child_agent.AddParent(self)
        self.children.append(child_agent)
        relation = fm.parent_of("")
        relation.target_agent = child_agent
        relation.owner_agent = self
        self.AddRelation(relation)

    def AddRelation(self, relation):
        self.relations.append(relation)

    def __init__(self, first_name = "Default",location = None, age = 18, traits = [], attributes = atr.Attributes(), morality = 50, lawful = 50, gender=Gender.Female, orientation=SexOrientation.Straight):
        self.name = first_name
        self.location = location
        self.age = age
        self.gender = gender
        self.sex_orientation = orientation
        self.traits = traits
        self.attributes = attributes
        self.morality = morality
        self.lawful = lawful
        self.children = list()
        self.siblings = list()
        self.parents = list()
        self.relations = list()

    def GetFullName(self):
        return self.name + " " + fm.FAMILIES[self.family].name

    def display(self):
        print(self.name, fm.FAMILIES[self.family].name)
        print("")
        print("Parents:")
        for p in self.parents:
            print("\t" + p.GetFullName())
        print("Siblings:")
        for sb in self.siblings:
            print("\t" + sb.GetFullName())
        print("Children:")
        for ch in self.children:
            print("\t" + ch.GetFullName())
        print("Relations:")
        for relation in self.relations:
            print("\t" + relation.display())
        print("")