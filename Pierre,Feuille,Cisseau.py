from random import *

class jeu:
    """
    le jeu bien connue du pierre,feuille, cisseau amélioré par BBT

    """

    def __init__(self):
        """init"""


    def cpu(self, user):
        """
        return random choice and prevent ties
            parameters :
                user (int) : the choice from user

            return:
                choix_cpu (int) : random integer numbre in 0 to 4
        """
        choix_cpu = randint(0,4)
        while user == choix_cpu: # prevent ties
             choix_cpu = randint(0,4)
        return choix_cpu

    def victoire(self, choix_user):
        """
        defini la victoire

            parameters :
                choix_user (int): a decimal integer, player choice


        """

        list_move = ["pierre","feuille","ciseau","lezard","spock"]
        dict_vict = {
                    "pierre":["ciseau","lezard"],
                    "feuille":["pierre","spock"],
                    "ciseau":["feuille","lezard"],
                    "lezard":["feuille","spock"],
                    "spock":["pierre","ciseau"]
                    }

        user_to_int = int(choix_user) - 1

        choix_user = list_move[user_to_int] # return to index
        choix_user = dict_vict[choix_user]

        choix_cpu = list_move[self.cpu(user_to_int)] # return to index

        if choix_cpu in choix_user:
            print("bravo !!")
        else:
            print("dommage")





    def play(self):
        """
        the main part, the game

        """
        print("message bienvenue jeu")
        while True:

            choix_user = int(input('choisi ton signe \n 1 - pierre \n 2 - feuille \n 3 - cisseau \n 4 - lezard \n 5 - spock \n'))
            self.victoire(choix_user)

            print("tu n'a le droit qu aux nombre de 1 a 5")


            continu = input('veux tu continuer ? y/n')
            if continu == "y" or continu == "Y":
                pass
            elif continu == "n" or continu == "N":
                break
            else:
                break


play = jeu()

play.play()
