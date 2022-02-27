from VNEPy.VNEPy.words import *
from VNEPy.VNEPy.character import Character

from VNEPy.VNE2D.interactions import ExampleButton

a = Character("10", (255, 0, 0))

fragment = Fragment('123')
fragment.add(Phrase("ghvhvghvv", a))
fragment.add(Phrase("fjkgbnjfgjk", a))
fragment.add(Choice(ExampleButton, ('10', '30'), ('20', '30')))

fragment2 = Fragment('30')
fragment2.add(Phrase("3423424", a))
fragment2.add(Phrase("343242343432423", a))

plot = compile_plot(fragment, fragment2)
print(plot)
