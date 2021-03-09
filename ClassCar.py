class Car:
    def __init__(self,resa,tipo):
        self.resa=resa
        self.serbatoio=0
        self.carburante=tipo

    def drive(self,distanza):
        serbatoio-=distanza*self.resa

    def getCarburante(self):
        return self.serbatoio

    def addCarburante(self,quantita):
        self.serbatoio+=quantita

    def usaBenzina(self):
        if self.carburante=="benzina":
            return True
        else:
            retuen False
    def usaGasolio(self):
        if self.carburante=="benzina":
            return True
        else:
            return False
