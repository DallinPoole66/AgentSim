LASTNAMES = list()
MALE_NAMES = list()
FEMALE_NAMES = list()

with open('lib/names_last.txt') as f:
    for line in f:
        LASTNAMES.append( line.split()[0] )

with open('lib/names_first_male.txt') as f:
    for line in f:
        MALE_NAMES.append( line.split()[0] )

with open('lib/names_first_female.txt') as f:
    for line in f:
        FEMALE_NAMES.append( line.split()[0] )

print(len(LASTNAMES))
print(len(MALE_NAMES))
print(len(FEMALE_NAMES))