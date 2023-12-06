#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a Dictionary / (listen können auch in listen genestet werden)
travel_log = {
    "France": {"Cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"Cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#nesting dictionary in a list
travel_log = [
    {"country": "France",
     "Cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
     },
    {"country": "Germany",
     "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5
     },
]
