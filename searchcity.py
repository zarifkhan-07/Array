tour_city=["New York", "Toronto", "Dhaka", "Malibag", "New York", "Gulshan", "Mohakhali"]
target_city="New York"

def search_city(search_list,target_value):
    matches=[]
    for idx in range(len(search_list)):
        if search_list[idx]==target_value:
            matches.append(idx)
    if not matches:
        ValueError("Target city cannot be found.")
    else:
        return matches
tour_stops=search_city(tour_city,target_city)
print(target_city,"is present at the following positions in the list",tour_stops)