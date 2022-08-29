from datetime import date

today = date.today()
today = today.strftime("%d/%m/%Y")

print("Bonjour [UTILISATEUR]")
print("Nous sommes aujourd'hui le", today)