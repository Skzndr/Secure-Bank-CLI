import logging
import hashlib

PASSWORD_HASH = hashlib.sha256("1234".encode()).hexdigest()

def verifier_mdp():
    max_tentatives = 3 
    tentatives = 0

    while tentatives < max_tentatives:
        user_password = input("Entrez votre mot de passe : ")
        hash_user = hashlib.sha256(user_password.encode()).hexdigest()

        logging.debug(f"Hash saisi: {hash_user}")

        if hash_user == PASSWORD_HASH:
            logging.info("Authentification réussie")
            return True
        else:
            tentatives += 1
            reste = max_tentatives - tentatives
            logging.warning(f"Mot de passe incorrect. Tentatives restantes : {reste}")
    
    logging.error("Accès bloqué après 3 tentatives")
    return False
