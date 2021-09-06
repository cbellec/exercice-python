from random import *

class jeu:

    def __init__(self):
        """init"""


    def cpu(self):
        choix_cpu = randint(0,4)
        return choix_cpu

    def victoire(self, choix_user):
        choix_cpu = randint(0,4)

        list_move = ["pierre","feuille","ciseau","lezard","spock"]
        dict_vict = {
                    "pierre":["ciseau","lezard"],
                    "feuille":["pierre","spock"],
                    "ciseau":["feuille","lezard"],
                    "lezard":["feuille","spock"],
                    "spock":["pierre","ciseau"]
                    }

        choix_user = list_move[int(choix_user) - 1] # return to index
        choix_user = dict_vict[choix_user]

        choix_cpu = list_move[choix_cpu] # return to index

        if choix_cpu in choix_user:
            print("bravo !!")
        else:
            print("dommage")





    def play(self):
        print("message bienvenue jeu")
        while True:
            try:
                choix_user = int(input('choisi ton signe \n 1 - pierre \n 2 - feuille \n 3 - cisseau \n 4 - lezard \n 5 - spock \n'))
            except:
                print("tu n'a le droit qu aux nombre de 1 a 5")
            self.victoire(choix_user)

            continu = input('veux tu contunuer ? y/n')
            if continu == "y" or continu == "Y":
                pass
            elif continu == "n" or continu == "N":
                break
            else:
                break


play = jeu()

play.play()
