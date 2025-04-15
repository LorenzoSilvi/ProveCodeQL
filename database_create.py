import sqlite3

# Connessione al database (crea un nuovo database se non esiste)
conn = sqlite3.connect('example.db')

# Creazione di un cursore
cursor = conn.cursor()

# Esecuzione di una query
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Inserimento di dati
cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Alice', 30))
cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Bob', 25))

# Commit delle modifiche
conn.commit()

# Esecuzione di una query di selezione
cursor.execute('''SELECT * FROM users''')

# Recupero dei risultati
rows = cursor.fetchall()
for row in rows:
    print(row)

# Chiusura della connessione
conn.close()
