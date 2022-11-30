# Docker + FastAPI (Python)

Projet modèle d'emploi de Docker pour la mise en place d'une architecture Back End basée sur un environnement Python avec le framework FastAPI (https://fastapi.tiangolo.com/).

- Attention le projet FastAPI mis en place n'est qu'une base de travail à améliorer. Il est recommandé d'organiser le code de l'API à travers différents fichiers spécifiques, en séparant les modèles de la logique métier (cf. https://fastapi.tiangolo.com/tutorial/bigger-applications/).

- Tutoriel officiel :
https://fastapi.tiangolo.com/deployment/docker/

## Variables d'environnement

Créer les fichiers ./api/.env et ./db/.env basés sur les fichiers modèles ./api/.env.example et ./db/.env.example (à adapter librement).

## Commandes Docker utiles

- Création d'une image Docker à partir du fichier Dockerfile et des sources :
`docker build -t fastapiimage .`

- Création d'un container à partir de l'image "fastapiimage" précédemment créée :
`docker run -d --name fastapi -p 80:80 fastapiimage`

- Initialisation des services Docker :
`docker compose up`

- Démarrage des services Docker :
`docker compose start`

- Consultation des services Docker actifs :
`docker compose ps`

- Clôture des services Docker : 
`docker compose stop`

## Test de l'API

- Racine : 

http://localhost/

- Route items :

http://localhost/items

http://localhost/items/10

http://localhost/items/10?q=test

- Documentation Swagger générée automatiquement
http://localhost/docs

---

**Alexandre Leroux**

Développeur logiciel (web & mobile)<br/>
Enseignant / Formateur

Mail : alex@sherpa.one<br/>
Site : https://sherpa.one<br/>
Github : @sherpa1<br/>
Discord : sherpa#3890<br/>