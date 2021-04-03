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
import random
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
    traits = None
    # Attributes
    attributes = {
        "vitality" :10,
        "strength" : 10,
        "inteligence" : 10,
        "education" : 0,
        "charisma" : 10,
        "perception" : 10,
        "deception" : 10,
        "stealth" : 10,
        "attack_physical" : 10,
        "attack_magical" : 0,
        "defense_physical" : 10,
        "defense_magical" : 10,
        "morality":50,
        "lawful":80
    }

    parents = None
    children = None
    siblings = None
    relations = None
    objectives = None
    

    def AddParent(self, parent_agent):
        self.parents.append(parent_agent)
        self.AddTrait(ts.trait_child_of_agent(self, parent_agent))

    def AddSibling(self, sibling_agent):
        self.siblings.append(sibling_agent)

    def AddChild(self, child_agent):
        for sibling in self.children:
            sibling.AddSibling(child_agent)
            child_agent.AddSibling(sibling)
        child_agent.AddParent(self)
        self.children.append(child_agent)
        self.AddTrait(ts.trait_parent_of_agent(parent_agent= self,child_agent=child_agent))

    def AddRelation(self, relation):
        self.relations.append(relation)

    def AddTrait(self, new_trait):
        self.traits.append(new_trait)

    def __init__(self, first_name = "Default",location = None, age = 18, traits = [], gender=Gender.Female, orientation=SexOrientation.Straight):
        self.name = first_name
        self.location = location
        self.age = age
        self.gender = gender
        if random.randrange(100) < 5:
            print("*********************************************************************************************")
            if random.randint(0, 1):
                self.sex_orientation = SexOrientation.Bi
            else:
                self.sex_orientation = SexOrientation.Gay
        else:
            self.sex_orientation = orientation

        self.traits = traits
        self.children = list()
        self.siblings = list()
        self.parents = list()
        self.relations = list()
        self.traits = list()
        self.objectives = list()

    def GetFullName(self):
        return self.name + " " + fm.FAMILIES[self.family].name

    def display(self):
        print(self.name, fm.FAMILIES[self.family].name, self.age,self.sex_orientation, self.gender)
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
        print("Traits:")
        for trait in self.traits:
            print("\t" + trait.GetDisplayName())
        print("Objectives:")
        for objective in self.objectives:
            print("\t" + objective.GetDisplayName())
        print("")

    def GetListOfObjectives(self):
        possible_objectives = list()
        for trait in self.traits:
            possible_objectives += trait.GenerateObjectives()
        self.objectives = possible_objectives
        return possible_objectives

    def CheckForCompletedObjectives(self):
        completed = list()
        for objective in self.objectives:
            if objective.CheckIfCompleted():
                completed.append(objective)
        
        for i in completed:
            self.objectives.remove(i)

    def IncreaseAtribute(self):
        pass
