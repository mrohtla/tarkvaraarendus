import smtplib # Impordib smtplib mooduli

sender_email = "vikk.opilane@outlook.com" # Saatja e-maili aadress
rec_email = "kerli.lobus@vikk.ee" # küsib kasutajalt saaja e-maili
password = input(str("Please enter your password : ")) # küsib sisestatud parooli
SUBJECT = input(str("Please enter subject : ")) # küsib sisestatud teema
TEXT = input(str("Please enter body : ")) # küsib sisestatud sisu
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT) # määrab sõnumi

server = smtplib.SMTP('smtp-mail.outlook.com', 587) # Sisestab sisestatud e-maili
server.starttls() # alustab starttls protokolli
server.login(sender_email, password) # Sisestab sisestatud e-maili
print("Login success") # Annab teada et sisselogimine õnnestus
server.sendmail(sender_email, rec_email, message) # Sisestab sisestatud e-maili
print("Email has been sent to ", rec_email) # Annab teada et e-mail on saadetud

#Dokumentatsioon:
#Saadab kooli üld maililt kirja valitud saajale, mille teema ja sisu oled saanud ise valida ning kui
#kiri on saadetud annab sellest teada. Sellist koodi saab kasutada automaatvastajana kui sul on pandud kindlad sisendid, pealkirjad jms