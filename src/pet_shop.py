# WRITE YOUR FUNCTIONS HERE
# 
import pprint

def get_pet_shop_name (pet_shop):
    pprint.pprint(pet_shop)
    return pet_shop["name"] 

def get_total_cash(pet_shop):
    return pet_shop ["admin"]["total_cash"]

def add_or_remove_cash (pet_shop, cash):
    pet_shop["admin"]["total_cash"] =  pet_shop["admin"]["total_cash"] + cash

def get_pets_sold(pet_shop):
    return pet_shop['admin']["pets_sold"]

def increase_pets_sold (pet_shop, sold):
    pet_shop['admin']["pets_sold"] = pet_shop['admin']["pets_sold"] + sold 

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

    #####This is how far I got on my own. 

def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)

    return found_pets

