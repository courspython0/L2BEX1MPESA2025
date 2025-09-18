# ==== Données de départ ====
APP_NAME = "Kin Money"
CURRENCY = "CDF"

stored_msisdn = "0999999999"
kyc_verified  = True
pin_code      = "1234"
balance       = 300000
daily_limit   = 1000000
today_spent   = 200000

tel     = "0999999999"
agent   = "AG1234"
montant = 50000

MIN_OP = 1000
MAX_OP = 1000000

# ==== Fonction utilitaire ====
def sep_thousands(n):
    return "{:,}".format(n).replace(",", " ")

# ==== Simulation statique ====
frais = 1000
total = montant + frais
new_balance = balance - total

print("==== {} — Reçu Retrait (M-PESA) ====".format(APP_NAME))
print("Référence : KM-RT-DEMO-0001")
print("Date/Heure : 2025-09-15 12:00:00")
print("Agent :", agent)
print("Client : Glodi Testeur ({})".format(tel))
print("Montant :", "{} {}".format(sep_thousands(montant), CURRENCY))
print("Frais : %s %s" % (sep_thousands(frais), CURRENCY))
print(f"Total débité : {sep_thousands(total)} {CURRENCY}")
print(f"Solde restant : {sep_thousands(new_balance)} {CURRENCY}")
print("Statut : SUCCESS")
print("===========================================")
print("===========================================")