'''
Relation
    Represents how the agent feels towards another agent. Can be a driving force for emotional objectives that aren't derived from traits
'''
import agent as ag

class Relation:
    owner_agent = None
    target_agent = None
    # 0 =  nemisis, 100 = best friend
    relation = 50
    # is it a romantic relation from the Owner -> Target? Doesn't imply recipricated feelings
    is_romantic = False

    def AdjustRelation(self, amount):
        self.relation = max(min(self.relation + amount, 100), 0)
        if self.relation < 40: 
            self.is_romantic = False
