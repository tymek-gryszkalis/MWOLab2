import db

def dbInit():
    db.init()

def getClientById(id):
    return db.select("client", id)

def getProductById(id):
    return db.select("product", id)

def getOrderById(id):
    return db.select("product", id)

def getAllClients():
    return db.select("client", all = True)

def getAllProducts():
    return db.select("product", all = True)

def getAllOrders():
    return db.select("order", all = True)

def addClient(name, surname, email):
    d = {"Name" : name, "Surname" : surname, "Email" : email}
    db.insert("client", d)

def addProduct(name, price, magstate):
    d = {"Name" : name, "Price" : price, "MagazineState" : magstate}
    db.insert("product", d)

def addOrders(clientID, productList, status):
    d = {"ClientID" : clientID, "ProductList" : ",".join(productList), "OrderStatus" : status}
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
    d = {"ClientID" : clientID, "ProductList" : ",".join(productList), "OrderStatus" : status}
    for i in d:
        if d[i] == "":
            d.pop(i)
    db.update("order", d, id)
    

    