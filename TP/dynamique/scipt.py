APP_NAME = "Global business"
CURRENCY = "CDF"

# Profil utilisateur (valeurs 'stockées' fictives)
client_tel = "0981961965"
kyc_verified = True
solde_compte = 580000
plafond_journalier = 900000
depenses_aujourdhui = 5000

# Saisie des paramètres opération par l'utilisateur
tel = input("Entrez le numéro de téléphone du client : ")
agent_id = input("Entrez l'ID de l'agent : ")
montant = int(input("Entrez le montant à retirer : "))

# Limites opération
MIN_OPERATION = 20000
MAX_OPERATION = 300000

# Frais fixe
frais_operation = 2000

# Date/heure simulée (fixée ici, peut être remplacée par date dynamique)
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

# Affichage formaté
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

