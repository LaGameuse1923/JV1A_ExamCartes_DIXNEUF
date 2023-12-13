class Mage:

    def __init__(self,nom,point_de_vie,total,valeur_mana) -> None:

        self.__name = nom
        self.__PV = point_de_vie
        self.__total = total
        self.__mana =valeur_mana

    def getname(self):
        return self.__name
    
    def getMana(self):
        return self.__mana

    def PerdrePV(self,attack):

        self.__PV -= attack

        if(self.__PV <= 0):
            self.__PV = 0
            print("Vous avez gagner")
        else:
            print("Les PV de ",self.__name ," sont à ",self.__PV)
    
    def EtatDuMage(self):
        if (self.__PV > 0):
            return False
        else:
            return True
        

    def rechargeMana(self):

        self.__mana += 20

        print("Vous avez recharger votre mana")


class Carte: 

    def __init__(self,mana,nom,descrition) -> None:
        self.__cout_mana = mana
        self.__name = nom
        self.__descrition = descrition
    
    def getname(self):
        return self.__name
    
    def getMana(self):
        return self.__cout_mana

class Cristal(Carte):

    def __init__(self, mana, nom, descrition,valeur) -> None:
        super().__init__(mana, nom, descrition)
        self.__valeur = valeur


class Creature(Carte):

    def __init__(self, mana, nom, descrition,point_de_vie,score_attack) -> None:
        super().__init__(mana, nom, descrition)
        self.__PV = point_de_vie
        self.__Attack = score_attack

    
    def PerdrePV(self,attack):
        
        self.__PV -= attack


        if (self.__PV <= 0):
            print("Le monstre est vaincu")
        else:
            print("Les PV de ",self.getname() ," sont à ",self.__PV)


    

    def attack(self,cible):
        
        cible.PerdrePV(self.__Attack)

        

class Blast(Carte):

    def __init__(self, mana, nom, descrition,valeur) -> None:
        super().__init__(mana, nom, descrition)
        self.__valeur = valeur

    def Lancercarte(self,cible):
        
        if(Bob.getMana() > self.getMana()):

            cible.PerdrePV(self.__valeur)

        else:
            print("Pas assez de Mana")


Bob = Mage("Bob",20,0,25)
Demon = Creature(10,"Demon","und demon pas content",10,5)
Magic = Cristal(5,"Magic","un cristal magic ",10)
FireBolt = Blast(5,"BouleDeFeu","une boule de feu",10)


main = { 1: Cristal(5,"Magic","un cristal magic ",10),
         2: Creature(10,"Demon","und demon pas content",10,5),
         3: Blast(5,"BouleDeFeu","une boule de feu",10)}

Mechant = Mage("Mechant",20,0,25)
monstreDuMechant = Creature(10,"monsre","non",25,0)


MortDuMageAdvers = False

while (MortDuMageAdvers == False):

    choix = int(input("Que voulez vous faire ? \n 1/ jouer une carte \n 2/ recuperer Mana \n 3/ attaquer une cible\n"))

    if(choix ==1):

        Choix3 = int(input("Quelle carte jouer ? \n 1/Magic \n 2/ Demon \n 3/ BouleDeFeu \n \n"))

        if(Choix3 == 1):

            Bob.getname()

        if(Choix3 == 2):
            
            Bob.getname()

        if(Choix3 == 3):
                Choix2 = int(input("Quelle cible ? \n1/ Mage \n2/Creature\n"))

        if(Choix2 == 1):
            FireBolt.Lancercarte(Mechant)
        
        if(Choix2 == 2):
            FireBolt.Lancercarte(monstreDuMechant)



    if(choix == 2):
        Bob.rechargeMana()

    if(choix == 3):
        Choix2 = int(input("Quelle cible ? \n1/ Mage \n2/Creature\n"))

        if(Choix2 == 1):
            Demon.attack(Mechant)
        
        if(Choix2 == 2):
            Demon.attack(monstreDuMechant)
    
    MortDuMageAdvers = Mechant.EtatDuMage()










