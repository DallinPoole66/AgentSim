'''
Tasks represent actions taken by agents to pursue objectives.
They cost effort and are assigned to an agent based on capabilities and objective needs.
Held as actions within capabilities.
Ex. Educate Child Objective -> Agent with Educator Capability -> Agent is assigned Educate Task
Tasks have an estimated value used in the bartering of Agents. The agent has a stat that modifies this cost, aswell as the relationship between the agents. 
Bartering will also try to allow the exchange of tasks in addition to resources.
'''

class Task():
    owning_agent = None
    target_agent = None
    target_location = None
    effort = 25

    def __init__(self, owner, target, location):
        self.owning_agent = owner
        self.target_agent = target
        self.target_location = location

    def DoTask(self):
        pass
    

class task_increase_atribute(Task):
    skill = ""
    improve_amount = 1

    def __init__(self, owner, target, skill):
        self.owning_agent = owner
        self.target_agent = target
        self.skill = skill

    def DoTask(self):
        self.target_agent.attributes[self.skill] += self.improve_amount

