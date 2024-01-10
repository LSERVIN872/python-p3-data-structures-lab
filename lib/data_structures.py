spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food['name'] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food.get('heat_level') and food['heat_level'] > 5:
            spiciest_foods.append(food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name')
        cuisine = food.get('cuisine')
        heat_level = food.get('heat_level')

        
        heat_emojis = '🌶' * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
    return None  

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get('heat_level')
        if heat_level and heat_level > 5:
            name = food.get('name')
            cuisine = food.get('cuisine')

            heat_emojis = '🌶' * heat_level

            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    num_foods = len(spicy_foods)

    if num_foods == 0:
        return 0

    for food in spicy_foods:
        heat_level = food.get('heat_level')
        if heat_level is not None:
            total_heat += heat_level

    average_heat = total_heat / num_foods
    return int(average_heat)

def create_spicy_food(spicy_foods, new_spicy_food):
   
    modified_spicy_foods = spicy_foods.copy()
    
    modified_spicy_foods.append(new_spicy_food)
    
    return modified_spicy_foods