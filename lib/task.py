'''
Tasks represent actions taken by agents to pursue objectives.
They cost effort and are assigned to an agent based on capabilities and objective needs.
Held as actions within capabilities.
Ex. Educate Child Objective -> Agent with Educator Capability -> Agent is assigned Educate Task
Tasks have an estimated value used in the bartering of Agents. The agent has a stat that modifies this cost, aswell as the relationship between the agents. 
Bartering will also try to allow the exchange of tasks in addition to resources.
'''