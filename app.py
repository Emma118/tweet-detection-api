from flask import Flask, request, jsonify
import joblib
import numpy as np
from gensim.models import Word2Vec

# Charger le modèle Random Forest
rf_model = joblib.load("model/random_forest_model.pkl")
print("Random Forest chargé avec succès.")

# Charger le modèle Word2Vec
word2vec = Word2Vec.load("model/word2vec.model")
print("Word2Vec chargé avec succès.")

# Créer l'application Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur l'API de détection de tweets suspects !"

@app.route("/predict", methods=["POST"])
def predict():
    # Récupérer le tweet envoyé
    data = request.json
    if "tweet" not in data:
        return jsonify({"error": "Veuillez fournir un texte avec la clé 'tweet'"}), 400

    tweet = data["tweet"]

    # Tokenisation simple
    tokens = tweet.lower().split()

    # Créer un vecteur moyen pour le tweet
    vector = np.mean(
        [word2vec.wv[token] for token in tokens if token in word2vec.wv.index_to_key],
        axis=0
    ).reshape(1, -1)

    # Vérifier que le vecteur n'est pas vide
    if vector.size == 0:
        return jsonify({"error": "Le texte fourni ne contient aucun mot valide"}), 400

    # Faire une prédiction
    prediction = rf_model.predict(vector)

    # Retourner le résultat
    return jsonify({
        "tweet": tweet,
        "prediction": "suspect" if prediction[0] == 1 else "non suspect"
    })

# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
