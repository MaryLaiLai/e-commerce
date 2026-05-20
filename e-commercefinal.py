import json

def add_cart():
    products=[]
    with open("products.json","r",encoding="utf-8") as fichier:
        products=json.load(fichier)
    name=input("entrer le nom du produit : ")
    new_products={"name":name}
    products.append(new_products)
    with open("products.json","w",encoding="utf-8") as fichier:
            json.dump(products,fichier,indent=4)
def add_products(): # ajouter des produits dans le fichier products
    name=input("entrer le nom du produit : ")
    with open("products.json","r",encoding="utf-8") as fichier:
        products=json.load(fichier)
        for item in products:
            if item["name"]==name:
                name=input("new name : ")
                price=float(input("new price : "))
                item["name"]=name
                item["price"]=price
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
    new_products=[]
    name=input("entrer le nom du produit : ")
    with open("products.json","r",encoding="utf-8") as fichier:
        products=json.load(fichier)
        for item in products :
            if name!=item["name"]:
                new_products.append(item)
    with open("cart.json","w",encoding="utf-8") as fichier1:
        json.dump(new_products,fichier1,indent=4)

def display(): #show products
    file = open ("products.json","r")
    products = json.load(file)
    print(products)
    file.close()

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
        print("0_break")
        choix=int(input("enter your choice : "))
        if choix ==1:
            add_cart()
        elif choix ==2:
            add_products()
        elif choix ==3:
            delete_cart()
        elif choix ==0:
            