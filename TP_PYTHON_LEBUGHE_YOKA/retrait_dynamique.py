# ==== Données de départ ====
APP_NAME = "Kin Money"
CURRENCY = "CDF"

stored_msisdn = "0999999999"
kyc_verified  = True
pin_code      = "1234"
balance       = 300000
daily_limit   = 1000000
today_spent   = 200000

MIN_OP = 1000
MAX_OP = 1000000

# ==== Fonction utilitaire ====
def sep_thousands(n):
    return "{:,}".format(n).replace(",", " ")

# ==== Entrées utilisateur ====
tel = input("Entrez votre numéro : ")
if tel != stored_msisdn:
    print("[ECHEC] Numéro inconnu.")
    exit()

pin = input("Entrez votre code PIN : ")
if pin != pin_code:
    print("[ECHEC] PIN incorrect.")
    exit()

montant = int(input("Montant à retirer (CDF) : "))

# ==== Vérifications ====
if montant < MIN_OP or montant > MAX_OP:
    print("[ECHEC] Montant hors limites.")
    exit()

frais = 1000
total = montant + frais

if total > balance:
    print("[ECHEC] Solde insuffisant. Solde : {} {} — Requis : {} {}".format(
        sep_thousands(balance), CURRENCY, sep_thousands(total), CURRENCY))
    exit()

# ==== Mise à jour du solde ====
new_balance = balance - total

# ==== Affichage du reçu ====
print("==== {} — Reçu Retrait (M-PESA) ====".format(APP_NAME))
print("Référence : KM-RT-DEMO-0002")
print("Agent : AG1234")
print("Client : {} ({})".format("Utilisateur", tel))
print("Montant :", "{} {}".format(sep_thousands(montant), CURRENCY))
print("Frais : %s %s" % (sep_thousands(frais), CURRENCY))
print(f"Total débité : {sep_thousands(total)} {CURRENCY}")
print(f"Solde restant : {sep_thousands(new_balance)} {CURRENCY}")
print("Statut : SUCCESS")
print("===========================================")