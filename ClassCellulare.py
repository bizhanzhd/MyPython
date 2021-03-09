class Cellulare:

    def __init__(self,carica=10):
        self.carica=carica
        self.numeroChiamate=0

    def ricarica(self, unaricarica):
        self.carica=self.carica + unaricarica

    def chiamata(self, minutiDurata):
        self.carica=self.carica - (0.2*minutiDurata)
        self.numeroChiamate+=1

    def numero404(self):
        print("la carica disponibile: "+str(self.carica))

    def getNumeroChiamate(self):
        print("tot. numero chiamate sono: ", str(self.numeroChiamate))

    def azzeraChiamate(self):
        self.numeroChiamate=0
