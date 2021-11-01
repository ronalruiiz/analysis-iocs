class Ioc:
    def __init__(self,item,value,name="",type="",reputation="",detect="",apply=""):
        self.item = item
        self.value = value
        self.name = name
        self.type = type
        self.reputation = reputation
        self.detection = detect

    def __str__(self):
        return "From str method of Test: %s, %s, %s, %s, %s, %s, %s" % (self.item, self.value,self.name,self.type,self.reputation,self.detection,self.apply)
