import json

def search_repair(make_model, repair_type):
    with open("repair_data.json", "r") as file:
        data = json.load(file)
    
    car = data.get(make_model.lower().replace(" ", "_"))
    if not car:
        return f"No repair info found for {make_model}"

    repair = car.get(repair_type.lower().replace(" ", "_"))
    if not repair:
        return f"No info found for {repair_type} on {make_model}"

    return repair
