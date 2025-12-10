# code/api_test.py

# Import (come "use" in PHP)
import requests
import json

print("=== CHIAMATA API - Esempio Base ===\n")

# 1. GET Request semplice
print("1. GET Request - Ottieni un utente casuale")
response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# Controlla se la richiesta è andata a buon fine
if response.status_code == 200:
    # Converti JSON in dizionario Python (come json_decode in PHP)
    utente = response.json()
    
    print(f"Nome: {utente['name']}")
    print(f"Email: {utente['email']}")
    print(f"Città: {utente['address']['city']}")
else:
    print(f"Errore: {response.status_code}")

print("\n" + "="*50 + "\n")

# 2. GET Request con parametri
print("2. GET con parametri - Cerca post di un utente")
parametri = {
    'userId': 1
}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=parametri)

posts = response.json()
print(f"Trovati {len(posts)} post")
print(f"Primo post: {posts[0]['title']}")

print("\n" + "="*50 + "\n")

# 3. POST Request - Crea una risorsa
print("3. POST Request - Crea un nuovo post")
dati_nuovi = {
    'title': 'Il mio primo post da Python',
    'body': 'Sto imparando Python dopo 20 anni di PHP!',
    'userId': 1
}

response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=dati_nuovi  # Converte automaticamente in JSON
)

if response.status_code == 201:  # 201 = Created
    nuovo_post = response.json()
    print(f"Post creato con ID: {nuovo_post['id']}")
    print(f"Titolo: {nuovo_post['title']}")
else:
    print(f"Errore: {response.status_code}")

print("\n" + "="*50 + "\n")

# 4. Request con headers personalizzati
print("4. Request con headers")
headers = {
    'User-Agent': 'Python-Learning-App',
    'Accept': 'application/json'
}

response = requests.get(
    'https://jsonplaceholder.typicode.com/users/1',
    headers=headers
)

print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers['Content-Type']}")