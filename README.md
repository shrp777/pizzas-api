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

- Initialisation des services Docker en mode détaché (reprise de la main dans le terminal) :
`docker compose up -d`

- Initialisation des services Docker avec reconstruction de l'image :
`docker compose up --build`

- Initialisation des services Docker avec activation du mode watch (= hot reloading) :
`docker compose up --watch`

- Démarrage des services Docker :
`docker compose start`

- Consultation des services Docker actifs :
`docker compose ps`

- Clôture des services Docker :
`docker compose stop`

## Routes l'API

### Racine

```sh
curl http://localhost:8080
```

### Collection pizzas

#### Création d'une pizza

```sh
curl --request POST \
  --url http://localhost:8080/pizzas \
  --header 'content-type: application/json' \
  --data '{
  "name": "Margherita",
  "ingredients": "Basilic, Mozzarella",
  "price": 6
}'
```

```http
"POST /pizzas HTTP/1.1" 201
```

```JSON
{
  "name": "Margherita",
  "ingredients": "Basilic, Mozzarella",
  "price": 6,
  "id": 1
}
```

#### Lecture de toutes les pizzas

```sh
curl --request GET \
  --url http://localhost:8080/pizzas
```

```http
"GET /pizzas HTTP/1.1" 200
```

```JSON
[
  {
    "name": "Margherita",
    "ingredients": "Basilic, Mozzarella",
    "price": 6,
    "id": 1
  }
]
```

#### Lecture de 1 pizza par son id

```sh
curl --request GET \
  --url http://localhost:8080/pizzas/1
```

```http
"GET /pizzas/1 HTTP/1.1" 200
```

```JSON
{
  "name": "Margherita",
  "ingredients": "Basilic, Mozzarella",
  "price": 6,
  "id": 1
}
```

### Mise à jour d'1 pizza par son id

```sh
curl --request PUT \
  --url http://localhost:8080/pizzas/1 \
  --header 'content-type: application/json' \
  --data '{
  "id":1,
  "name": "Margherita",
  "ingredients": "Mozzarella, Basilic",
  "price": 6
}'
```

```http
"PUT /pizzas/1 HTTP/1.1" 200
```

```json
{
  "name": "Margherita",
  "ingredients": "Mozzarella, Basilic",
  "price": 7,
  "id": 1
}
```

#### Suppression d'une pizza selon son id

```sh
curl --request DELETE \
  --url http://localhost:8080/pizzas/1
```

```http
"DELETE /pizzas/1 HTTP/1.1" 204
```

- Documentation Swagger générée automatiquement par FastAPI
<http://localhost:8080/docs>

## Adminer

<http://localhost:8181>

--

!["Logotype Shrp"](https://sherpa.one/images/sherpa-logotype.png)

__Alexandre Leroux__  
_Enseignant / Formateur_  
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

<https://shrp.dev>
