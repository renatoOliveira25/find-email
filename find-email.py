import re
import csv

csv_colunas = ["email"]
conteudo = []

texto = "Olá, meu nome é Renato, tenho 30 anos e meu e-mail é rEnato@EMAIL.com.br, meu email secundário é renato2@email.com"

emails = re.findall('\S+@\S+[.com.br]', texto.lower())

for email in emails:
	info = {"email": email}
	content.append(info)
	
print(content)

try:
	with open('files/emails.csv', mode='w') as emails_file:
		writer = csv.DictWriter(emails_file, fieldnames=csv_colunas)
		writer.writeheader()
		for email in conteudo:
			writer.writerow(email)
except IOError:
	print("I/O error")
