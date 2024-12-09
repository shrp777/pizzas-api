# Docker + FastAPI (Python)

Projet modèle pour l'emploi de Docker dans la mise en place d'une architecture Back End basée sur un environnement Python avec le framework FastAPI (<https://fastapi.tiangolo.com/>).

- Attention le projet FastAPI mis en place n'est qu'une base de travail à améliorer. Il est recommandé d'organiser le code de l'API à travers différents fichiers spécifiques, en séparant les modèles de la logique métier (cf. <https://fastapi.tiangolo.com/tutorial/bigger-applications/>).

- Tutoriel officiel :
<https://fastapi.tiangolo.com/deployment/docker/>

- PostgreSQL + Docker
<https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/>

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

<http://localhost:8080/>

- Route items :

<http://localhost:8080/items>

<http://localhost:8080/items/10>

<http://localhost:8080/items/10?q=test>

- Documentation Swagger générée automatiquement
<http://localhost:8080/docs>

--

!["Logotype Shrp"](https://sherpa.one/images/sherpa-logotype.png)

__Alexandre Leroux__  
_Enseignant / Formateur_  
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

<https://shrp.dev>
