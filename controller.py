import db

def dbInit():
    db.init()

def getClientById(id):
    return db.select("client", by = id)

def getProductById(id):
    return db.select("product", by = id)

def getOrderById(id):
    return db.select("order", by = id)

def getAllClients():
    return db.select("client", all = True)

def getAllProducts():
    return db.select("product", all = True)

def getAllOrders():
    return db.select("order", all = True)

def getClientByEmail(email):
    return db.select("client", check = "Email", by = email)

def getProductByName(name):
    return db.select("product", check = "Name", by = name)

def addClient(name, surname, email):
    d = {"Name" : name, "Surname" : surname, "Email" : email}
    db.insert("client", d)

def addProduct(name, price, magstate):
    d = {"Name" : name, "Price" : price, "MagazineState" : magstate}
    db.insert("product", d)

def addOrder(clientID, productList, status):
    d = {"ClientID" : clientID, "ProductList" : "|".join(productList), "OrderStatus" : status}
    db.insert("order", d)

def removeClient(id):
    db.delete("client", id)

def removeProduct(id):
    db.delete("product", id)

def removeOrder(id):
    db.delete("product", id)

def updateClient(id, name = "", surname = "", email = ""):
    d = {"Name" : name, "Surname" : surname, "Email" : email}
    for i in d:
        if d[i] == "":
            d.pop(i)
    db.update("client", d, id)

def updateProduct(id, name = "", price = "", magstate = ""):
    d = {"Name" : name, "Price" : price, "MagazineState" : magstate}
    for i in d:
        if d[i] == "":
            d.pop(i)
    db.update("product", d, id)

def updateOrder(id, clientID = "", productList = "", status = ""):
    d = {"ClientID" : clientID, "ProductList" : "|".join(productList), "OrderStatus" : status}
    for i in d:
        if d[i] == "":
            d.pop(i)
    db.update("order", d, id)
    
def clientExists(email):
    if getClientByEmail(email) == []:
        return False
    return True

def productExists(name):
    if getProductByName(name) == []:
        return False
    return True

def orderExists(id):
    if getProductById(id) == []:
        return False
    return True
    