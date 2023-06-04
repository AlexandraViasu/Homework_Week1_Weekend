# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, num):
    pet_shop["admin"]["total_cash"] += num

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number_sold):
    pet_shop["admin"]["pets_sold"] += number_sold

def get_stock_count(pet_shop):
   total_stock = len(pet_shop["pets"])
   return total_stock

def get_pets_by_breed(pet_shop, breed_name):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            pets.append(pet)
    return pets

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    else:
        return None

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(cust):
    return cust["cash"]

def remove_customer_cash(cust, cash):
    new_cash = cust["cash"] - cash
    cust["cash"] = new_cash
    # OR EITHER:
   # cust["cash"] -= cash
   # cust["cash"] = cust["cash"] - cash

def get_customer_pet_count(cust):
    return len(cust["pets"])

def add_pet_to_customer(cust, pet):
    cust["pets"].append(pet)
