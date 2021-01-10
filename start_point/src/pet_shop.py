# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]




def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]



def add_or_remove_cash(pet_shop, cash):
  pet_shop["admin"]["total_cash"] += cash



def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash



def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]



def increase_pets_sold(pet_shop, sale):    
    pet_shop["admin"]["pets_sold"] += sale
    #alternative
    # pets_sold = get_pets_sold(pet_shop)
    # pets_sold += sale



def get_stock_count(pet_shop):
    return len(pet_shop["pets"])



def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet ["breed"] == breed:
            pets.append(pet)
    return pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

def remove_pet_by_name(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop ["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    stock = get_stock_count(pet_shop)
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_removed):
    customer["cash"] -= cash_removed
    
    
def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    count = get_customer_pet_count(customer)
    customer["pets"].append(new_pet)
    

    
    
    





    







    
    







