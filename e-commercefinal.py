import json

def add_cart():
    name=input("entrer le nom du produit : ")
    quantity=int(input("entrer la quantité : "))
    with open("products.json","r",encoding="utf-8") as fichier:
        products=json.load(fichier)
    found=None
    for item in products:
        if item["name"]==name:
            found=item
            break
    if found is None:
        print("produit non trouvé")
        return
    with open("cart.json","r",encoding="utf-8") as fichier:
        cart=json.load(fichier)
    for item in cart:
        if item["name"]==name:
            item["quantity"]+=quantity
            break
    else:
        new_product={"name":name,"price":found["price"],"quantity":quantity}
        cart.append(new_product)
    with open("cart.json","w",encoding="utf-8") as fichier:
        json.dump(cart,fichier,indent=4)

def add_products(): # ajouter des produits dans le fichier products
    name=input("entrer le nom du produit : ")
    price=float(input("entrer le prix : "))
    with open("products.json","r",encoding="utf-8") as fichier:
        products=json.load(fichier)
    for item in products:
        if item["name"]==name:
            print("produit déjà existant")
            return
    new_product={"name":name,"price":price}
    products.append(new_product)
    with open("products.json","w",encoding="utf-8") as fichier:
        json.dump(products,fichier,indent=4)

def delete_products():
    new_products=[]
    name=input("entrer le nom du produit : ")
    with open("products.json","r",encoding="utf-8") as fichier:
        products=json.load(fichier)
        for item in products :
            if name!=item["name"]:
                new_products.append(item)
    with open("products.json","w",encoding="utf-8") as fichier:
        json.dump(new_products,fichier,indent=4)

def delete_cart():
    new_cart=[]
    name=input("entrer le nom du produit : ")
    with open("cart.json","r",encoding="utf-8") as fichier:
        cart=json.load(fichier)
        for item in cart :
            if name!=item["name"]:
                new_cart.append(item)
    with open("cart.json","w",encoding="utf-8") as fichier1:
        json.dump(new_cart,fichier1,indent=4)

def display(): #show products
    file = open ("products.json","r")
    products = json.load(file)
    print(products)
    file.close()

def display_cart():
    total=0
    with open("cart.json","r",encoding="utf-8") as fichier:
        cart=json.load(fichier)
    print("Panier :")
    for item in cart:
        print(item["name"]," - ",item["price"]," x ",item["quantity"])
        total+=item["price"]*item["quantity"]
    print("Total à payer :",total)

def checkout():
    display_cart()
    with open("cart.json","w",encoding="utf-8") as fichier:
        json.dump([],fichier,indent=4)
    print("Commande validée !")

def menu():
    print("Are you an admin or a user?")
    print("1_Admin")
    print("2_User")
    choice=int(input("enter your choice : "))
    if choice ==1:
        print("1_Add products")
        print("2_delete products")
        choix=int(input("enter your choice : "))
        if choix ==1:
            add_products()
        elif choix ==2:
            delete_products()
        else:
            menu()
    elif choice ==2:
        display()
        print("1_Add to cart")
        print("2_delete from cart")
        print("3_display cart")
        print("4_checkout")
        print("0_break")
        choix=int(input("enter your choice : "))
        if choix ==1:
            add_cart()
        elif choix ==2:
            delete_cart()
        elif choix ==3:
            display_cart()
        elif choix ==4:
            checkout()
        elif choix ==0:
            return

# start the program
menu()
