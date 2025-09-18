APP_NAME = "Kin Money"
CURRENCY = "CDF"

# Profil utilisateur (fictif)
client_phone_number = "0999999999"
is_identity_verified = True
user_security_pin = "1234"
account_balance_cdf = 300000  # solde initial (CDF)
daily_withdrawal_limit = 1000000  # plafond journalier (CDF)
daily_expense_total = 200000  # déjà dépensé aujourd'hui (CDF)

# Paramètres opération (modifiables pour tester)
input_phone_number = input("Entrez votre numéro de téléphone: ")
m_pesa_agent_id = input("Entrez l'ID de l'agent M-PESA: ")
transaction_amount = int(input("Entrez le montant à rétirer (CDF) : "))  # CDF

# Limites opération
MINIMUM_OPERATION_AMOUNT = 1000
MAXIMUM_OPERATION_AMOUNT = 1000000


# Fonction pour afficher les milliers avec espaces
def sep_thousands(n):
    return "{:,}".format(n).replace(",", " ")


# Vérifications simples
if not is_identity_verified:
    print("[ECHEC] KYC non vérifié.")
elif input_phone_number != client_phone_number:
    print("[ECHEC] Numéro de téléphone incorrect.")
elif transaction_amount < MINIMUM_OPERATION_AMOUNT or transaction_amount > MAXIMUM_OPERATION_AMOUNT:
    print(f"[ECHEC] Montant doit être entre {sep_thousands(MINIMUM_OPERATION_AMOUNT)} et {sep_thousands(MAXIMUM_OPERATION_AMOUNT)} {CURRENCY}.")
elif (daily_expense_total + transaction_amount) > daily_withdrawal_limit:
    print("[ECHEC] Plafond journalier dépassé.")
elif transaction_amount + 1000 > account_balance_cdf:  # frais fixe 1000
    print(f"[ECHEC] Solde insuffisant. Solde : {sep_thousands(account_balance_cdf)} {CURRENCY} --- Requis : {sep_thousands(transaction_amount+1000)} {CURRENCY}")
else:
    # Retrait autorisé
    fee = 1000
    total_debited = transaction_amount + fee
    account_balance_cdf -= total_debited
    daily_expense_total += transaction_amount

    print("==== {} --- Reçu Retrait (M-PESA) ====\nRéférence : KM-RT-DEMO-0001".format(APP_NAME))
    print(f"Date/Heure : 2025-09-15 12:00:00")
    print(f"Agent : {m_pesa_agent_id}")
    print(f"Client : Glodi Testeur ({input_phone_number})")
    print("Montant : {} {}".format(sep_thousands(transaction_amount), CURRENCY))
    print("Frais : %s %s" % (sep_thousands(fee), CURRENCY))
    print(f"Total débité : {sep_thousands(total_debited)} {CURRENCY}")
    print(f"Solde restant : {sep_thousands(account_balance_cdf)} {CURRENCY}")
    print("Statut : SUCCESS")
    print("===========================================")

    print(f"[INFO] OTP : 123456 (simulé) --- validé")
    print(f"[INFO] PIN : {user_security_pin} (simulé) --- validé")