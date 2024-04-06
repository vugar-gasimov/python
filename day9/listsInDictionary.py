capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Azerbaijan": "Baku",
    "Ukraine": "Kiev"
}

# travel_log = {
#     "France": {
#         "visited_cities": ["Paris", "Lille", "Dijon"],
#         "total_visits": [3, 1, 1]
#         },
#     "Germany": {
#         "visited_cities": ["Berlin", "Hamburg", "Stuttgart", "Frankfurt"],
#         "total_visits": [5, 2, 3]
#         },
#     "Azerbaijan": {
#         "visited_cities": ["Baku", "Oguz", "Qebele", "Ismayilli", "Naxhcivan"],
#         "total_visits": [100, 50, 50, 2, 3]
#         },
#     "Ukraine": {
#         "visited_cities": ["Kyiv", "Lviv", "Kharkov", "Odessa"],
#         "total_visits": [11, 3, 0, 0]
#         },
# }

travel_log = [
    {
        "country": "France", 
        "visited_cities": ["Paris", "Lille", "Dijon"],
        "total_visits": [3, 1, 1]
    },
    {
        "country": "Germany", 
        "visited_cities": ["Berlin", "Hamburg", "Stuttgart", "Frankfurt"],
        "total_visits": [5, 2, 3]
    },
    {
        "country": "Azerbaijan", 
        "visited_cities": ["Baku", "Oguz", "Qebele", "Ismayilli", "Naxhcivan"],
        "total_visits": [100, 50, 50, 2, 3]
    },
    {
        "country": "Ukraine", 
        "visited_cities": ["Kyiv", "Lviv", "Kharkov", "Odessa"],
        "total_visits": [11, 3, 0, 0]
    },
]

["A", "B", ["C", "D"]]

print(travel_log["France"], ["visited_cities"])