import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nbr = 256  # Vous pouvez modifier ce paramètre à tout moment

neg_df = pd.read_csv(f"/Users/apple/Desktop/DATASIM/Projets/sans R/kravchuk-no-R/csv/{nbr}_neg.csv", header=None)
pos_df = pd.read_csv(f"/Users/apple/Desktop/DATASIM/Projets/sans R/kravchuk-no-R/csv/{nbr}_pos.csv", header=None)

# Ignorer la ligne de titre et convertir en nombres flottants
neg = neg_df.iloc[1:].astype(float)
pos = pos_df.iloc[1:].astype(float)

# Obtenir la colonne des seuils (première colonne)
neg_threshold = neg.iloc[:, 0].values
pos_threshold = pos.iloc[:, 0].values

# Obtenir les statistiques résumées (deuxième colonne)
neg_stats = neg.iloc[:, 1].values
pos_stats = pos.iloc[:, 1].values

# Méthode 1 : moyenne des seuils provenant des deux fichiers
threshold = (neg_threshold.mean() + pos_threshold.mean()) / 2

# Tracer les courbes
plt.figure(figsize=(10, 6))

# Estimation de la densité (KDE)
from scipy.stats import gaussian_kde
x_grid = np.linspace(min(np.min(neg_stats), np.min(pos_stats)) - 1,
                     max(np.max(neg_stats), np.max(pos_stats)) + 1, 1000)
neg_kde = gaussian_kde(neg_stats)
pos_kde = gaussian_kde(pos_stats)

plt.plot(x_grid, neg_kde(x_grid), label='H₀ : Pas de chant d’oiseau (négatif)', color='blue')
plt.plot(x_grid, pos_kde(x_grid), label='H₁ : Chant d’oiseau (positif)', color='red')

# Remplir les zones d’erreur
# Fausse alarme : statistique négative > seuil
fa_region = x_grid[x_grid > threshold]
plt.fill_between(fa_region, 0, neg_kde(fa_region), color='blue', alpha=0.3, label='Fausse alarme')

# Échec de détection : statistique positive ≤ seuil
miss_region = x_grid[x_grid <= threshold]
plt.fill_between(miss_region, 0, pos_kde(miss_region), color='red', alpha=0.3, label='Détection manquée')

# Ligne de seuil
plt.axvline(threshold, color='black', linestyle='--', label=f'Seuil = {threshold:.2f}')

# Amélioration de l’affichage
# plt.title("Hypothesis Testing: Bird Sound Detection")
plt.title("Deux types de statistiques résumées (sur les extraits positifs)")
plt.xlabel("Valeur de la statistique")
plt.ylabel("Densité")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

## Courbe ROC
from sklearn.metrics import roc_curve, auc

# Fusionner les statistiques et les étiquettes
all_stats = np.concatenate([neg_stats, pos_stats])
all_labels = np.concatenate([np.zeros_like(neg_stats), np.ones_like(pos_stats)])

# Calculer la courbe ROC
fpr, tpr, roc_thresholds = roc_curve(all_labels, all_stats)

# Calcul de l’AUC (aire sous la courbe)
roc_auc = auc(fpr, tpr)

# Tracer la courbe ROC
plt.figure(figsize=(6, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Courbe ROC (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--', label='Hasard')
plt.xlabel('Taux de faux positifs')
plt.ylabel('Taux de vrais positifs')
plt.title('Courbe ROC pour la détection de chants d’oiseaux')
plt.legend(loc="lower right")
plt.grid(True)
plt.tight_layout()
plt.show()

from sklearn.metrics import precision_recall_curve, average_precision_score

# Calculer la courbe précision-rappel
precision, recall, pr_thresholds = precision_recall_curve(all_labels, all_stats)

# Calcul de la moyenne de la précision (AP)
ap_score = average_precision_score(all_labels, all_stats)

# Tracer la courbe PR
plt.figure(figsize=(6, 6))
plt.plot(recall, precision, color='green', lw=2, label=f'Courbe PR (AP = {ap_score:.2f})')
plt.xlabel('Rappel')
plt.ylabel('Précision')
plt.title('Courbe Précision-Rappel pour la détection de chants d’oiseaux')
plt.legend(loc="lower left")
plt.grid(True)
plt.tight_layout()
plt.show()
