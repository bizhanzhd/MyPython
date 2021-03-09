from car import Car
from distributore import DistributoreBenzina

eni= DistributoreBenzina(1.5)
eni.rifornisci(500)

mercedes=Car(10)

eni.vendi(50,mercedes)

print(mercedes.getGas())
