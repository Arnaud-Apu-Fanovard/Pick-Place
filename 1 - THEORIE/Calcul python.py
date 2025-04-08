import math
import pandas as pd

# Importation des bibliothèques nécessaires

# Définition des constantes globales
g = 9.81  # Accélération gravitationnelle (m/s^2)
module = 2  # Module de la poulie
N_steps = 200  # Nombre de steps par tour
f_max = 25/3  # Fréquence maximale (Hz)
Rpm = f_max * 60  # Vitesse de rotation (tr/min)

# Définition des paramètres initiaux
T = 1.0  # Couple du moteur (Nm)
a = 20  # Accélération maximale (m/s^2)
v = 2  # Vitesse cible (m/s)
ratio = 1  # Ratio du jeu d'engrenage
nombre_dents = 60  # Nombre de dents de la poulie

# Calculs de base
diametre = round((module * nombre_dents) / math.pi, 2)
rayon_poulie = diametre / 2
vitesse_rad_s = 2 * math.pi * f_max
vitesse_lin = (vitesse_rad_s * rayon_poulie) / ratio
distance_par_step = (math.pi * diametre) / N_steps
F = (T / (rayon_poulie / 1000)) * ratio
m_total = F / (a + v * g) * 1000

# Affichage des résultats de base
# print("Calcul moteur avec comme paramètre :")
# print(f"Couple moteur : {T} Nm")
# print(f"Accélération maximale : {a} m/s^2")
# print(f"Vitesse cible : {v} m/s")
# print(f"Nombre de steps par tour : {N_steps}")
# print(f"Nombre de dents du poulie : {nombre_dents}")
# print(f"Fréquence maximale : {f_max} Hz")
# print(f"Vitesse de rotation : {Rpm} Tr/min")
# print("-----------------------------")
print(f"Diamètre de la poulie : {diametre} mm")
print(f"Rayon de la poulie : {rayon_poulie} mm")
# print(f"Vitesse angulaire : {vitesse_rad_s:.2f} rad/s")
# print(f"Vitesse linéaire : {vitesse_lin:.2f} mm/s")
# print(f"Distance parcourue par step : {distance_par_step:.2f} mm")
# print(f"Force maximale disponible : {F:.2f} N")
# print(f"Masse maximale : {m_total:.2f} g")
# print("-----------------------------")

# Exploration des valeurs multiples
T_values = [0.5,0.6, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
nombre_dents_values = [16, 20,30, 36, 40, 60, 80,100 ,110,120]
results = []

for T in T_values:
    for nombre_dents in nombre_dents_values:
        diametre = round((module * nombre_dents) / math.pi, 2)
        rayon_poulie = diametre / 2
        vitesse_rad_s = 2 * math.pi * f_max
        vitesse_lin = (vitesse_rad_s * rayon_poulie) / ratio
        distance_par_step = (math.pi * diametre) / N_steps
        F = (T / (rayon_poulie / 1000)) * ratio
        m_total = F / (a + v * g) * 1000

        results.append({
            "T (Nm)": T,
            "Nombre de dents": nombre_dents,
            "Diamètre (mm)": diametre,
            "Rayon (mm)": rayon_poulie,
            "Vitesse angulaire (rad/s)": round(vitesse_rad_s, 2),
            "Vitesse linéaire (mm/s)": round(vitesse_lin, 2),
            "Distance par step (mm)": round(distance_par_step, 4),
            "Force maximale (N)": round(F, 2),
            "Masse maximale (g)": round(m_total, 2)
        })

# Création d'un DataFrame pour stocker les résultats
df_results = pd.DataFrame(results)

# Affichage des résultats complets
print(df_results)

# Filtrage des résultats selon des seuils
masse_min = 1900  # Masse minimale en grammes
vitesse_min = 1000  # Vitesse linéaire minimale en mm/s

# Définition de la fonction pour filtrer les résultats
def filtrer_resultats(df, masse_min, vitesse_min):
    """
    Filtre les résultats d'un DataFrame en fonction des seuils de masse minimale et de vitesse linéaire minimale.

    Paramètres:
    - df (DataFrame): Le DataFrame contenant les résultats à filtrer.
    - masse_min (float): La masse minimale en grammes pour le filtrage.
    - vitesse_min (float): La vitesse linéaire minimale en mm/s pour le filtrage.

    Retourne:
    - DataFrame: Un DataFrame contenant uniquement les lignes qui respectent les critères de filtrage.
    """
    # Appliquer les conditions de filtrage
    return df[
        (df["Masse maximale (g)"] >= masse_min) & 
        (df["Vitesse linéaire (mm/s)"] >= vitesse_min)
    ]

df_filtre = filtrer_resultats(df_results, masse_min, vitesse_min)


print("Calcul moteur avec comme paramètre :")
print(f"Accélération maximale : {a} m/s^2")
print(f"Vitesse cible : {v} m/s")
print(f"Nombre de steps par tour : {N_steps}")
print(f"Fréquence maximale : {f_max} Hz")
print(f"Vitesse de rotation : {Rpm} Tr/min")
print("-----------------------------")
# Affichage des résultats filtrés
print("Résultats filtrés :")
print(df_filtre)