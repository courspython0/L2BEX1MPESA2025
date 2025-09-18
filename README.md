Tp de Python Membres :

Mutombo Kanyinda Gedeon :ETUL2PY005 (CHEF)
Luhusu bontel : ETUL2PY007
Mufenge Barthélémy : ETUL2PY014
Cimbalanga Mbuyi : 
Lunangu biselu
awete mboyo : ETUL2PY003
muyika mazenga : ETUL2PY023






# ===== Données de départ =====
APP_NAME = "Kin Money"
CURRENCY = "CDF"

# Profil utilisateur (fictif)
stored_msisdn = "0830881856"
kyc_verified  = True
pin_code      = "2004"
balance       = 300000     # solde initial (CDF)
daily_limit   = 1000000    # plafond journalier (CDF)
today_spent   = 200000     # déjà dépensé aujourd'hui (CDF)

# Paramètres opération (modifiables pour tester)
tel     = input("Veuillez saisir votre numéro de téléphone : ")
agent   = input("Veuillez saisir votre numéro agent : ")
montant = int(input("Veuillez saisir le montant à retirer en CDF : "))

# Limites opération
MIN_OP = 1000
MAX_OP = 1000000
FEE = 1000  # frais fixes

# ===== Fonction pour séparer les milliers =====
def sep_thousands(n):
    i = 0
    mont_avec_espace = str(n)
    mont_avec_espace1 = ""
    if len(str(n)) <= 3:
        mont_avec_espace1 = str(n)
    else:
        for index in range(1, len(mont_avec_espace) + 1):
            dernier = mont_avec_espace[-int(index)]
            i += 1
            mont_avec_espace1 += dernier
            if i == 3 and index != len(mont_avec_espace):  # éviter espace au début
                mont_avec_espace1 += " "
                i = 0
    mont_avec_espace1 = mont_avec_espace1[::-1]
    return mont_avec_espace1

# ===== Vérifications =====
if tel != stored_msisdn:
    print("[ECHEC] Numéro invalide.")
else:
    # Vérification PIN
    pin_input = input("Entrez votre PIN : ")
    if pin_input != pin_code:
        print("ECHEC : PIN incorrect.")
    else:
        # Vérification montant
        if montant < MIN_OP:
            print(f"ECHEC : Vous ne pouvez pas retirer un montant inférieur à ({sep_thousands(MIN_OP)} CDF).")
        elif montant > MAX_OP:
            print(f"ECHEC : Vous ne pouvez pas retirer un montant supérieur à ({sep_thousands(MAX_OP)} CDF).")
        elif today_spent + montant > daily_limit:
            print(f"ECHEC : Plafond journalier dépassé. Limite : {sep_thousands(daily_limit)} CDF")
        elif balance < montant + FEE:
            print("ECHEC : Solde insuffisant. Solde : {} CDF — Requis : {} CDF".format(
                sep_thousands(balance), sep_thousands(montant + FEE)))
        else:
            # Tout est OK → mise à jour du solde
            total_debite = montant + FEE
            balance -= total_debite

            #===== Reçu formaté =====
            
            print("==== Kin Money — Reçu Retrait (M-PESA) ====")
            print(f"Référence : KM-RT-DEMO-0001")
            print("Date/Heure : 2025-09-15 12:00:00")
            print("Agent : %s" % agent)
            print("Client : {} ({})".format("Gedeon Mutombo", stored_msisdn))
            print("Montant : {} CDF".format(sep_thousands(montant)))
            print("Frais : %s CDF" % sep_thousands(FEE))
            print(f"Total débité : {sep_thousands(total_debite)} CDF")
            print(f"Solde restant : {sep_thousands(balance)} CDF")
            print("Statut : SUCCESS")
            print("===========================================")
            
