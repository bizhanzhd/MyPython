from car import Car

class DistributoreBenzina:
    def __init__(self, prezzoGas,prezzoBen):
        self.euroPerLitroGas=prezzoGas
        self.depositoGas=0
        self.euroPerLitroBen=prezzoBen
        self.depositoBen=0

    def rifornisciGas(self,unaQuantita):
        self.deposito+=unaQuantita
    def rifornisciBen(self,unaQuantita):
        self.deposito+=unaQuantita

    def vendiGas(self,euro,unaAutomobile:Car):
        litri=euro/self.euroPerLitroGas
        unaAutomobile.addGas(litri)
        self.depositoGas-=litri
    def vendiBen(self,euro,unaAutomobile:Car):
        litri=euro/self.euroPerLitroBen
        unaAutomobile.addCarburante(litri)
        self.depositoBen-=litri

    def aggiornaGas(self,unPrezzoPerLitro):
        self.euroPerLitroGas=unPrezzoPerLitro
    def aggiornaBen(self,unPrezzoPerLitro):
        self.euroPerLitroBen=unPrezzoPerLitro
