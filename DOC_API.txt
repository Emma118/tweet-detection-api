Bienvenue dans l’API de détection de tweets suspects !
Cette API utilise un modèle de machine learning entraîné pour prédire si un tweet est suspect ou non. Elle combine un modèle Word2Vec pour transformer les tweets en vecteurs et un modèle Random Forest pour la classification.

Configuration de l’environnement
Prérequis :

Python 3.9

Bibliothèques nécessaires :
pip install flask gensim joblib numpy

Cloner le projet ou télécharger les fichiers nécessaires :

Inclure les fichiers app.py, random_forest_model.pkl, et word2vec.model dans un répertoire local.

Lancer l’API :

Exécutez la commande suivante dans le terminal : python app.py

L’API sera disponible à l’adresse : http://127.0.0.1:5000 si vous l'exécution est faite en local


Endpoints disponibles


1. Endpoint racine (GET /)
Description : Affiche un message de bienvenue pour vérifier que l’API fonctionne.
Méthode : GET

Exemple : curl http://127.0.0.1:5000/ --Sur POSTMAN PAR EXEMPLE

Réponse : "Bienvenue sur l'API de détection de tweets suspects !"


2. Endpoint de prédiction (POST /predict)
Description : Prédire si un tweet est suspect ou non.
Méthode : POST
Corps attendu : JSON avec une clé tweet

{
    "tweet": "Voici un exemple de texte"
}

Réponse : 

{
    "tweet": "Voici un exemple de texte",
    "prediction": "non suspect"
}


Exemple avec curl : 

curl -X POST -H "Content-Type: application/json" \
     -d '{"tweet": "Voici un exemple suspect"}' \
     http://127.0.0.1:5000/predict

