'''
    Agent
    Represents an indivual person. Contains their attributes, traits, objectives, and relationships with other agents.
    Agents all have a current location, a morality, and a bias towards order or chaos.
'''
import attributes as atr
import trait as ts
import capability as cap
import objective as obj
import relations as rel
import family as fm
import attributes as atr

class Agent():
    # First Name
    name = "Agent Name"
    # Family
    family = None
    # Current location
    location = None
    # Age
    age = 18
    # Traits
    traits = []
    # Attributes
    attributes = atr.Attributes()
    # Morality, 0 = Evil, 100 = Good
    morality = 50
    # lawful, 0 = Chaotic, 100 = Lawful
    lawful = 80
    