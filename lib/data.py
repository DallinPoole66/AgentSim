import family as fam
import agent
import task
import names
import random
'''
Montagues = fam.Family(familyName="Montague")
Capulets = fam.Family(familyName="Capulet")

fam.AddFamily(Montagues)
fam.AddFamily(Capulets)

pa_mont = agent.Agent(first_name="Father",age=43, gender=agent.Gender.Male, orientation=agent.SexOrientation.Straight)
ma_mont = agent.Agent(first_name="Mother",age=38, gender=agent.Gender.Female, orientation=agent.SexOrientation.Straight)
romeo = agent.Agent(first_name="Romeo",age=18, gender=agent.Gender.Male, orientation=agent.SexOrientation.Straight)
ben = agent.Agent(first_name="Benvolio",age=17, gender=agent.Gender.Male, orientation=agent.SexOrientation.Straight)

fam.AddFamilyMember(0, pa_mont)
fam.AddFamilyMember(0, ma_mont)
fam.AddFamilyMember(0, romeo)
fam.AddFamilyMember(0, ben)

fam.MarryAgents(pa_mont, ma_mont)
pa_mont.AddChild(romeo)
ma_mont.AddChild(romeo)


pa_cap = agent.Agent(first_name="Father",age=44, gender=agent.Gender.Male, orientation=agent.SexOrientation.Straight)
ma_cap = agent.Agent(first_name="Mother",age=36, gender=agent.Gender.Female, orientation=agent.SexOrientation.Straight)
juliet = agent.Agent(first_name="Juliet",age=18, gender=agent.Gender.Female, orientation=agent.SexOrientation.Straight)
ty = agent.Agent(first_name="Tybalt",age=17, gender=agent.Gender.Male, orientation=agent.SexOrientation.Straight)


fam.AddFamilyMember(1, pa_cap)
fam.AddFamilyMember(1, ma_cap)
fam.AddFamilyMember(1, juliet)
fam.AddFamilyMember(1, ty)
fam.MarryAgents(pa_cap, ma_cap)
pa_cap.AddChild(juliet)
ma_cap.AddChild(juliet)

pa_mont.GetListOfObjectives()
romeo.display()
pa_mont.display()

ed = task.task_increase_atribute(pa_mont, romeo, "education")
ed.DoTask()

pa_mont.CheckForCompletedObjectives()
pa_mont.display()

'''
AGENTS = list()

KINGDOMS = list()



def GenerateKingdoms():
    pass





for x in range(13):
    name = names.LASTNAMES[ random.randrange(x * int(88799 / 13), (x + 1) * int(88799 / 13))]
    new_family = fam.Family(name)
    fam.AddFamily(new_family)
    father = agent.Agent(names.MALE_NAMES[random.randrange(1219)] )
    mother = agent.Agent(names.FEMALE_NAMES[random.randrange(1000)] )
    fam.AddFamilyMember(new_family.index, father)
    fam.AddFamilyMember(new_family.index, mother)
    fam.MarryAgents(father, mother)
    for c in range(random.randrange(9)):
        if (random.randrange(1) == 1):
            kid = agent.Agent(names.MALE_NAMES[random.randrange(1219)])
        else:
            kid = agent.Agent(names.FEMALE_NAMES[random.randrange(1000)])
        fam.AddFamilyMember(new_family.index, kid)
        father.AddChild(kid)
        mother.AddChild(kid)

    father.display()
