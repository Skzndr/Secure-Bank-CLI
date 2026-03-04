import logging
solde =200
billet = [10,20,50,100]

def gerer_compte(action,montant):
    global solde
    logging.debug(f"Le solde est de {solde}€ ,Vous avez choisi de {action}, le montant de {montant} €")

    while True:
        if action == "retiré": 
            if montant not in billet: 
                logging.error(f"Seuls les billets {billet} peuvent être retiré")
                break
            elif montant > solde:
                logging.error(f"Le solde est insuffisant pour ce montant {montant}€")
            else:
                solde -= montant
                logging.info(f"Le retrait de {montant}€ a bien été effectué")
                logging.debug(f"Le solde est de {solde}€, vous aveez retiré {montant}")
                break

        elif action == "déposé":
            if montant not in billet:
                logging.error(f"Seuls les billets {billet} peuvent être déposés")
                break
            else:
                solde += montant
                logging.info(f"Le dépot de {montant}€ a bien étè effectué")
                logging.debug(f"Le solde est de {solde}€, vous avez déposé {montant}€")
                break
