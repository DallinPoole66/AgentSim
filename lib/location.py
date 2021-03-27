'''
    Location
    Contains the location's information about what agent's are there, where it connects and what kind of structures are there.
    Also provides geographically relevant info. A lumberjack cant work in a place with no trees
'''
import structure as st

class Location:
    name = "Location Name"
    structures = []
    population = []
    
    # how forested the area is. 0 = no trees, 100 = dense forest
    forest = 50
    # mineral wealth
    minerals = 50
    # Lake Nearby
    has_lake = False
    # river nearby
    has_river = True
    # Humidity, represents the overall aridness of the are. 0 = absolute desert, 100 = rain forest
    humidity = 50
    # Elevation, affects the length of growing season. 0 = sea level, 100 = high mountains
    elevation = 20
    # longitude, affects length of growing season, 0 = normal length, 100 = tundra w/ perma frost
    longitude = 20



