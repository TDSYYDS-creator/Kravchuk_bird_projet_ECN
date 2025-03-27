import re
import pandas as pd

# Lire le contenu du fichier texte
with open("/Users/apple/Desktop/DATASIM/Projets/sans R/kravchuk-no-R/csv/256_real_pos.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extraire toutes les valeurs de Threshold et de Value
thresholds = re.findall(r"Threshold of rejection: ([\d.]+)", text)
values = re.findall(r"Value of the summary statistics: ([\d.]+)", text)

print(f"Seuils extraits : {len(thresholds)} ; Valeurs extraites : {len(values)}")

# Prendre la longueur minimale pour éviter les erreurs
min_len = min(len(thresholds), len(values))

# Construire le DataFrame
df = pd.DataFrame({
    "Threshold of rejection": thresholds[:min_len],
    "Value of the summary statistics": values[:min_len]
})

# Sauvegarder en CSV
csv_path = "/Users/apple/Desktop/DATASIM/Projets/sans R/kravchuk-no-R/csv/256_real_pos.csv"
df.to_csv(csv_path, index=False)

print("CSV sauvegardé dans :", csv_path)
