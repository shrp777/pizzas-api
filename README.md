# Docker + FastAPI (Python)

Projet modèle d'emploi de Docker pour la mise en place d'une architecture Back End basée sur un environnement Python avec le framework FastAPI (https://fastapi.tiangolo.com/).


- Tutoriel officiel :
https://fastapi.tiangolo.com/deployment/docker/

## Commandes Docker utiles

- Création d'une image à partir du fichier Dockerfile et des sources :
`docker build -t fastapiimage .`

- Création d'un container à partir de l'image "fastapiimage" précédemment créée :
`docker run -d --name fastapi -p 80:80 fastapiimage`

- Initialisation des services :
`docker compose up`

- Démarrage des services :
`docker compose start`

- Consultation des services actifs :
`docker compose ps`

- Clôture des services : 
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