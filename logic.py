import controller as con

def registerClient(name, surname, email):
    if "@" not in email:
        raise Exception("Wrong email")

    con.addClient(name, surname, email)

def addProduct(name, price):
    try:
        price = int(price)
    except:
        raise Exception("Price is not integer")
    
    if con.productExists(name):
        p = con.getProductByName(name)[0]
        con.updateProduct(p[0], magstate = (p[2] + 1))
    else:
        con.addProduct(name, price, 1)

def incProduct(id):
    p = con.getProductById(id)[0]
    con.updateProduct(p[0], magstate = (p[2] + 1))

def decProduct(id):
    p = con.getProductById(id)[0]
    con.updateProduct(p[0], magstate = (p[2] - 1))

def createNewOrder(clientEmail, productList):
    if not con.clientExists(clientEmail):
        raise Exception("Client not registered")
    
    clientId = con.getClientByEmail(clientEmail)

    productListIds = []
    for i in productList:
        if not con.productExists(i):
            raise Exception("Product not availible")
        productListIds.append(con.getProductByName(i)[0][0])
    
    for i in productListIds:
        if con.getProductById(id)[0][0] == 0:
            raise Exception("Product not avilible")
        decProduct(i)
        
    con.addOrder(clientId, productList, "pending")

def updateOrderStatus(orderId, status):
    if status not in ["pending", "finished"]:
        raise Exception("Wrong status")
    
    con.updateOrder(orderId, status = status)

def revertOrder(orderId):
    if not con.orderExists(orderId):
        raise Exception("Order doesn't exist")
    
    productList = list(map(con.getOrderById(orderId)[0][2].split("|"), int))
    for i in productList:
        incProduct(i)
    
