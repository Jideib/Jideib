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
def update_record_damages(damages):
  # Update Recorded Damages
  conversion = {"M": 1000000,
              "B": 1000000000}
  updated_damages = list()
  for damage in damages:
    if damage[-1] == 'M':
      damage_i = damage.replace("M", "")
      updated_damages.append(float(damage_i) * conversion["M"])
    elif damage[-1] == 'B':
     damage_ii = damage.replace("B", "") 
     updated_damages.append(float(damage_ii) * conversion["B"])
    else:
      updated_damages.append(damage)
  return updated_damages

updated_damages = update_record_damages(damages)
# print(updated_damages)

# 2 
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  cd_list = zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

  hurricanes = {name: {'Name': name, 'Month': month, 'Year': year, 'Max Sustained Winds': max_sustained_wind, 'Areas Affected': areas, 'Damage': updated_damage, 'Death': death} for name, month, year, max_sustained_wind,  areas, updated_damage, death in cd_list}

  return hurricanes

# Create and view the hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# print(hurricanes)

# 3
# Organizing by Year
def create_dictionary_year(hurricanes):
  hurricanes_by_year = {}
  for cane in hurricanes:
    current_year = hurricanes[cane]['Year']
    current_cane = hurricanes[cane]
    if current_year not in hurricanes_by_year:
      hurricanes_by_year[current_year] = current_cane
    else:
      hurricanes_by_year[current_year].update(current_cane) 
  return hurricanes_by_year
  
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = create_dictionary_year(hurricanes)
#print(hurricanes_by_year)

# 4
# Counting Damaged Areas
def count_damaged_areas(hurricanes):
  areas_affected_count = {}
  for name in hurricanes.values():
    for area in name['Areas Affected']:
      if area not in areas_affected_count:
        areas_affected_count[area] = 1
    else:
      areas_affected_count[area] += 1
  return areas_affected_count
# create dictionary of areas to store the number of hurricanes involved in
areas_affected_count = count_damaged_areas(hurricanes)
# print(areas_affected_count)

# 5 
# Calculating Maximum Hurricane Count
def most_affected_area_count(areas_affected_count):
  most_affected = {}
  count = 0
  for key, value in areas_affected_count.items():
    if value > count:
      count = value
      most_affected[key] = value
  return most_affected 

# find most frequently affected area and the number of hurricanes involved in
most_affected = most_affected_area_count(areas_affected_count)
# print(most_affected)

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes):
  max_hurricane_death = ''
  count = 0
  for name in hurricanes:
    if hurricanes[name]['Death'] > count:
      max_hurricane_death = name
      count = hurricanes[name]['Death']
  return max_hurricane_death, count

# find highest mortality hurricane and the number of deaths
max_hurricane_death, count = deadliest_hurricane(hurricanes)
# print(deadliest_hurricane(hurricanes))
# 7
# Rating Hurricanes by Mortality
def rating_hurricane_mortality(hurricanes):
  hurricane_death_rating = {0:[],1:[],2:[],3:[],4:[],5:[]}
  death_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for name in hurricanes:
    if hurricanes[name]['Death'] == death_scale[0]:
      hurricane_death_rating[0].append(name)
    elif hurricanes[name]['Death'] <= death_scale[1]:
      hurricane_death_rating[1].append(name)
    elif hurricanes[name]['Death'] <= death_scale[2]:
      hurricane_death_rating[2].append(name)
    elif hurricanes[name]['Death'] <= death_scale[3]:
      hurricane_death_rating[3].append(name)
    elif hurricanes[name]['Death'] <= death_scale[4]:
      hurricane_death_rating[4].append(name)
    else:
      hurricane_death_rating[5].append(name)
  return hurricane_death_rating

# categorize hurricanes in new dictionary with mortality severity as key
hurricane_death_rating = rating_hurricane_mortality(hurricanes)
# print(hurricane_death_rating)


# 8 
# Calculating Hurricane Maximum Damage
def dangerous_hurricane(hurricanes):
  dangerous_hurricane_damage = 0
  cane = ''
  for name in hurricanes:
    if hurricanes[name]["Damage"] == "Damages not recorded":
      continue
    elif hurricanes[name]["Damage"] > dangerous_hurricane_damage:
      dangerous_hurricane_damage = hurricanes[name]["Damage"]
      cane = name 
  return cane, dangerous_hurricane_damage 

  # find highest damage inducing hurricane and its total cost
highest_damage_hurricane = dangerous_hurricane(hurricanes)
print(dangerous_hurricane(hurricanes))

# 9
# Rating Hurricanes by Damage
def dangerous_hurricane_rating(hurricanes):
  hurricanes_damage_rating = {0:[],1:[],2:[],3:[],4:[],5:[]}
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
  for name in hurricanes:
    total_damage = hurricanes[name]['Damage']
    if total_damage == "Damages not recorded":
      hurricanes_damage_rating[0].append(name)
    elif total_damage <= damage_scale[1]:
      hurricanes_damage_rating[1].append(name)
    elif total_damage <= damage_scale[2]:
      hurricanes_damage_rating[2].append(name)
    elif total_damage <= damage_scale[3]:
      hurricanes_damage_rating[3].append(name)
    elif total_damage <= damage_scale[4]:
      hurricanes_damage_rating[4].append(name)
    else:
      hurricanes_damage_rating[5].append(name)
  return hurricanes_damage_rating
# categorize hurricanes in new dictionary with damage severity as key
damage_rating = dangerous_hurricane_rating(hurricanes)
# print(damage_rating)