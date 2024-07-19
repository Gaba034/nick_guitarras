from classes.Guitar import Guitar
from classes.Inventory import Inventory
from classes.structure.Builder import Builder
from classes.structure.Wood import Wood
from classes.structure.TypeG import TypeG
from classes.utils.Logger import Logger as Log

# Set up Rick’s guitar inventory
inventory = Inventory()
# Adiciona guitarras ao estoque
inventory.add_guitar("V95693", 1499.95, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
# inventory.add_guitar("11277", 3999.95, Builder.COLLINGS.value, "Stratocastor", TypeG.ACOUSTIC.value, Wood.INDIAN_ROSEWOOD.value, Wood.INDIAN_ROSEWOOD.value)

# Buscando por uma guitarra que o Erin gosta: Fender Stratocastor elétrica com corpo de Alder e tampo de Alder
whatErinLikes = Guitar(" ", 0, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
guitar = inventory.search_guitar(whatErinLikes)

if guitar:
    msg = f"Erin, talvez você goste desta: {guitar.get_builder()} {guitar.get_model()} {guitar.get_typeg()} guitar:\n{guitar.get_back_wood()} na traseira e laterais, \n{guitar.get_top_wood()} no tampo.\nEla pode ser sua por apenas US${guitar.get_price()}!"
else:
    msg = "Não encontramos nada no estoque, sinto muito."

logger = Log(guitar, msg)
logger.log()
