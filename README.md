# LEGGIMI

Avviare docker a seguito di una modifica
> docker-compose build

Avviare prompt Python
> docker-compose run --rm python-dev python

Entrare nella bash del mio container Docker
> docker-compose run --rm python-dev bash

## Aggiungere nuove librerie
bash# 1. Aggiungi la libreria al requirements.txt
Da dentro il container Docker 
> echo "pandas>=2.1.0" >> requirements.txt

# 2. Rebuilda il container
> docker-compose build

# 3. Usa la nuova libreria
> docker-compose run --rm python-dev python
>>> import pandas