class Polynome:

    def __init__(self,p):
        self.coef=p

    def afficher(self):
        print(f'{self.coef[len(self.coef)-1]}X^{len(self.coef)-1}',end='')
        i = len(self.coef)-2
        while i>0:
            if (self.coef[i]<0):
                print(f' - {-self.coef[i]}X^{i}',end='')
            else:
                print(f' + {self.coef[i]}X^{i}',end='')
            i-=1
        if (self.coef[0]<0):
            print(f' - {-self.coef[0]}',end='')
        else:
            print(f' + {self.coef[0]}',end='')
        print('')

    def get_valeur(self,x):
        resultat=0
        for i in range(0, len(self.coef)):
            resultat=resultat+self.coef[i]*x**i
        return resultat

    