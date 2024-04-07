country = input("\n Add country name ")
visits = int(input("\n Enter number of visits ")) 
list_of_cities = eval(input("\n Enter the list of cities you have been to and your favorite one should be the first one ")) 

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# def add_new_country(name, times_visited, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = times_visited
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)

def add_new_country(country, visits, list_of_cities):
  new_country_entry = {
      "country": country,
      "visits": visits,
      "cities": list_of_cities,
  }
  travel_log.append(new_country_entry)

add_new_country(country, visits, list_of_cities)
print(f"\nI've been to {travel_log[-1]['country']} {travel_log[-1]['visits']} times.")
print(f"My favourite city was {travel_log[-1]['cities'][0]}. \n")