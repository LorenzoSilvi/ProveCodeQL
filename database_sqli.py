import sqlite3

# Connessione al database (crea un nuovo database se non esiste)
conn = sqlite3.connect('example.db')

# Creazione di un cursore
cursor = conn.cursor()

# input da dare per sqli injection "' or 1=1-- -"

username = input("Enter username: ")

query = f"SELECT * FROM users WHERE name = '{username}'"



cursor.execute(query)

# Recupero dei risultati
rows = cursor.fetchall()
for row in rows:
    print(row)

# Chiusura della connessione
conn.close()
