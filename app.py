import streamlit as st
import numpy as np
from collections import Counter

# Fonction de prédiction simplifiée (remplace par tes modèles IA)
def predict_euromillions():
    numbers = np.random.randint(1, 51, 5).tolist()
    stars = np.random.randint(1, 13, 2).tolist()
    return sorted(numbers), sorted(stars)

# Interface utilisateur Streamlit
st.title("Prédiction EuroMillions avec IA")
st.write("Cliquez sur le bouton pour générer une prédiction.")

if st.button("Générer mes numéros"):
    numbers, stars = predict_euromillions()
    st.success(f"Numéros : {numbers}")
    st.success(f"Étoiles : {stars}")
