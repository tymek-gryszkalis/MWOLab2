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


