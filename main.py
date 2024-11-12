from exercice1 import Polynome

p=Polynome([1.2,-0.1,-1.3,0.1,0.1])
print('Le polynome a cette forme : ')
p.afficher()
print('Valeur pour x=2 : ', end='')
print(p.get_valeur(2))
print('Valeur pour x=1 : ', end='')
print(p.get_valeur(1))
print('Valeur pour x=4 : ', end='')
print(p.get_valeur(4))