# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop['name']


def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount


def get_stock_count(pet_shop):
    counter = len(pet_shop["pets"])
    return counter


def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
        

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].pop(pet_shop["pets"].index(pet))
            pass


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    customer_wallet = customer["cash"]
    pet_value = new_pet["price"]
    if customer_wallet >= pet_value:
        return True
    else:
        return False
    

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None:
        if customer_can_afford_pet(customer, pet) == True:
            customer["pets"].append(pet)
            pet_shop["admin"]["pets_sold"] += 1
            customer["cash"] -= pet["price"]
            pet_shop["admin"]["total_cash"] += pet["price"]
    else:
        pass