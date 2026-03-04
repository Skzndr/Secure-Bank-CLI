import config
from auth import verifier_mdp
from operations import gerer_compte
import logging 

def main():
    if verifier_mdp():
        while True:
            action = input("Choisissez retiré / déposé / q pour quitter " ).lower()
            choix= ["retiré", "déposé"]

            if action == "q":
                logging.info("Déconnexion")
                break

            if action not in choix:
                logging.warning("Action invalide")
                continue

            montant = input("Entrez un montant : ")
            if montant.isdigit():
                gerer_compte(action, int(montant))
            else:
                logging.error("Montant invalide, entrez un chiffre correspondant à un billet")

if __name__=="__main__":
    main()         
