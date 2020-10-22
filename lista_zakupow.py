store = {"biedronka":"chleb"}

for key,values in store.items():
    print("ide do " +key.capitalize()+ " i kupuje " + values.capitalize())
print("\n")
"""problem jest gdy w slowniku do klucza podajemy wiele wartosci
jak zrobic piersza dużą litere dla krotki lub listy w słowniku??
"""

sotre1 = {"biedronka":["chleb","bulki","przyprawy"], 'lidl': ['skarpety', 'playstation5']}

sum_of_products = 0
for store_name, products in sotre1.items():
    im_going_to = store_name.capitalize()
    # capitalized_products = []
    # for product in products:
    #     capitalized_products.append(product.capitalize())
    capitalized_products = [asd.capitalize() for asd in products]
    i_want_to_buy = ', '.join(capitalized_products)
    
    #sum_of_products = sum_of_products + len(products)
    sum_of_products += len(products)

    print("Idę do "+im_going_to+ " Kupić "+i_want_to_buy )  

print(f"Moja lista zakupów składa się z {sum_of_products} rzeczy" )
