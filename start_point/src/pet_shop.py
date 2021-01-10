# WRITE YOUR FUNCTIONS HERE
cc_pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }

def get_pet_shop_name(list):
  return cc_pet_shop["name"]


def get_total_cash(list):
    return list["admin"]["total_cash"]
get_total_cash(cc_pet_shop)


def add_or_remove_cash(list, cash):
  list["admin"]["total_cash"] += cash

add_or_remove_cash(cc_pet_shop, 10)

def add_or_remove_cash(list, cash):
    list["admin"]["total_cash"] += cash

add_or_remove_cash(cc_pet_shop, -10)

def get_pets_sold(list):
    return list["admin"]["pets_sold"]

get_pets_sold(cc_pet_shop)

def increase_pets_sold(list, sale):
    list["admin"]["pets_sold"] += sale

increase_pets_sold(cc_pet_shop, 2)

def get_stock_count(list):
    return len(list["pets"])
get_stock_count(cc_pet_shop)



    







    
    







