'''
    Objective
    Serves as a goal for the Agent.
    Goals can be to increase a personal stat, gain a specific possession, spend time on an activity,
    interact with othert Agents and more.
    Objectives can be location based, status based, or intrinsic to the Agent.
'''

class Objective:
    # Print name of objective
    name = "objective name"
    # Owner Agent that is trying to accomplish this Objective
    owner_agent = None
    # Target Agent if needed. ex. FIGHT TARGET_AGENT
    target_agent = None
    # Amount of effort required of Agent to pursue
    effort = 50
    # Chances of successfully completing
    success_chance = 100
    # Location of Objective. None means no location needed
    location_requirments = None
    # Attributes needed
    attribute_requirements = None
    # Items needed
    item_requirements = []
    # Status needed
    traits_requirements = []

    # Requirements of the Target Agent
    target_location_requirements = None
    target_attribute_requirements = None
    target_item_requirements = []
    target_traits_requirements = []

    # Allows success to be derived from agent stats
    def CalculateSuccessChance(self):
        pass
    
    # Provide a friendly string
    def GetDisplayName(self):
        return "Object: Default"

    # Returns what requirements are needed to complete goal
    def GetRequirements(self):
        pass

    # What happens when the agent completes the objective
    def CompleteObjective(self):
        pass

