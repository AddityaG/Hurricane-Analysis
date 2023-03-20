# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
             "B": 1000000000}

# test function by updating damages
def updrec(damages):
    updated_damages = []
    for pp in damages:
        if pp == 'Damages not recorded':
            updated_damages.append('Damages not recorded')
        if pp[-1]=='M':
            updated_damages.append(float(pp.strip('M'))*conversion["M"])
        if pp[-1]=='B':
            updated_damages.append(float(pp.strip('B'))*conversion["B"])
    return updated_damages
updated_damages = updrec(damages)
print(updated_damages)

# 2
# Create a Table

# Create and view the hurricanes dictionary
def create_table(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths):
    hurricane_deets = {}
    for i in range(len(names)):
        hurricane_deets[names[i]]={'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
    return hurricane_deets
hurricane_deets = create_table(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)
print(hurricane_deets)

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def orgyr(hurricane_deets):
    hur_yr = {}
    for i in hurricane_deets.values():
        hur_yr[i['Year']]=[]
    for i in hurricane_deets.values():
        hur_yr[i['Year']].append(i)
    return hur_yr
hur_yr = orgyr(hurricane_deets)
print(hur_yr)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def cntdamar(hurricane_deets):
    damaged_areas = {}
    for iter in hurricane_deets:
        for i in hurricane_deets[iter]['Areas Affected']:
            if i in damaged_areas:
                damaged_areas[i]+=1
            else:
                damaged_areas[i] = 1
    return damaged_areas
damaged_areas = cntdamar(hurricane_deets)
print(damaged_areas)

# 5
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def maxhur(damaged_areas):
    maxx = 0
    maxpl = ""
    for i in damaged_areas:
        if damaged_areas[i]>maxx:
            maxx = damaged_areas[i]
            maxpl = i
    print("Most frequently affected area is {}".format(maxpl))
    print("Number of hits there is {}".format(maxx))
maxhur(damaged_areas)

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def deadliest(hurricane_deets):
    maxx = 0
    maxpl = ""
    for i in hurricane_deets:
        if hurricane_deets[i]['Deaths']>maxx:
            maxx = hurricane_deets[i]['Deaths']
            maxpl = i
    print("Highest mortality hurricane {}".format(maxpl))
    print("Greatest number of deaths is {}".format(maxx))
deadliest(hurricane_deets)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
1: 100,
2: 500,
3: 1000,
4: 10000}
# categorize hurricanes in new dictionary with mortality severity as key
def hurmort(hurricane_deets):
    mortality = {}
    for i in hurricane_deets:
        if hurricane_deets[i]['Deaths']>mortality_scale[0]:
            mortality[i] = 1
        if hurricane_deets[i]['Deaths']>mortality_scale[1]:
            mortality[i] = 2
        if hurricane_deets[i]['Deaths']>mortality_scale[2]:
            mortality[i] = 3
        if hurricane_deets[i]['Deaths']>mortality_scale[3]:
            mortality[i] = 4
        if hurricane_deets[i]['Deaths']>mortality_scale[4]:
            mortality[i] = 5
    return mortality
mortality = hurmort(hurricane_deets)
print(mortality)

# 8
# Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def maxdam(hurricane_deets):
    maxx = 0
    maxpl = ""
    for i in hurricane_deets:
        if hurricane_deets[i]['Damage'] == "Damages not recorded":
            continue
        if hurricane_deets[i]['Damage']>maxx:
            maxx = hurricane_deets[i]['Damage']
            maxpl = i
    print("Highest damage inducing hurricane is {}".format(maxpl))
    print("Maximum Damage is {}".format(maxx))
maxdam(hurricane_deets)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
def hurdam(hurricane_deets):
    damage_rating = {}
    for i in hurricane_deets:
        if hurricane_deets[i]['Damage'] == "Damages not recorded":
            damage_rating[i] = "Damages not recorded"
            continue
        if hurricane_deets[i]['Damage']>damage_scale[0]:
            damage_rating[i] = 1
        if hurricane_deets[i]['Damage']>damage_scale[1]:
            damage_rating[i] = 2
        if hurricane_deets[i]['Damage']>damage_scale[2]:
            damage_rating[i] = 3
        if hurricane_deets[i]['Damage']>damage_scale[3]:
            damage_rating[i] = 4
        if hurricane_deets[i]['Damage']>damage_scale[4]:
            damage_rating[i] = 5
    return damage_rating
damage_rating = hurdam(hurricane_deets)
print(damage_rating)