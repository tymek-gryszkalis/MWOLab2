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