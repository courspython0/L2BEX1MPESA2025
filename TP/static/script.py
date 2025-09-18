APP_NAME = "Global business"
CURRENCY = "CDF"

# Profil utilisateur
client_tel = "0981961965"
kyc_verified = True
solde_compte = 580000         # anciennement balance (solde initial)
plafond_journalier = 900000   # anciennement daily_limit (plafond journalier)
depenses_aujourdhui = 10000  # anciennement today_spent (dépensé aujourd'hui)

# Paramètres opération
tel = "0981961965"
agent_id = "DEL0120"          # anciennement agent
montant = 200000              # Montant entre MIN_OP et MAX_OP

# Limites opération
MIN_OPERATION = 20000          # anciennement MIN_OP
MAX_OPERATION = 300000          # anciennement MAX_OP

# Frais fixe
frais_operation = 2000        # anciennement fees

# Date/heure simulée
datetime_str = "2025-09-15 12:00:00"

# Vérifications simples
if tel != client_tel:
    statut = "FAILURE - Numéro client incorrect"
elif not kyc_verified:
    statut = "FAILURE - KYC non vérifié"
elif montant < MIN_OPERATION or montant > MAX_OPERATION:
    statut = "FAILURE - Montant hors limites"
elif montant + frais_operation + depenses_aujourdhui > plafond_journalier:
    statut = "FAILURE - Dépassement plafond journalier"
elif montant + frais_operation > solde_compte:
    statut = "FAILURE - Solde insuffisant"
else:
    statut = "SUCCESS"
    solde_compte -= montant + frais_operation
    depenses_aujourdhui += montant + frais_operation

reference = "KM-RT-DEMO-0001"
client_name = "Prosper kwon"

print("==== {} — Reçu Retrait (M‑PESA) ====".format(APP_NAME))
print("Référence : %s" % reference)
print(f"Date/Heure : {datetime_str}")
print(f"Agent : {agent_id}")
print("Client : {} ({})".format(client_name, tel))
montant_str = f"{montant:n}".replace(",", " ")
print(f"Montant : {montant_str} {CURRENCY}")
frais_str = f"{frais_operation:n}".replace(",", " ")
print("Frais : %s %s   (exemple)" % (frais_str, CURRENCY))
total = montant + frais_operation
total_str = f"{total:n}".replace(",", " ")
print(f"Total débité : {total_str} {CURRENCY}")
solde_str = f"{solde_compte:n}".replace(",", " ")
print(f"Solde restant : {solde_str} {CURRENCY}")
print("Statut : %s" % statut)
print("="*35)
