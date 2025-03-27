## Contexte

Le changement climatique, la dégradation des écosystèmes naturels et les activités humaines représentent des menaces majeures pour de nombreuses espèces aviaires.

Pour mettre en place des plans de conservation adaptés, il est nécessaire de **surveiller la densité des oiseaux** sur un territoire donné, à une période donnée.  
Cela s’avère particulièrement difficile pour les espèces migratrices nocturnes, excluant le recours aux méthodes d’observation directe.

Une solution alternative consiste à **« écouter » les oiseaux** à l’aide de capteurs acoustiques installés dans la zone d’intérêt.  
La difficulté réside alors dans la **détection automatique des cris** caractéristiques des espèces ciblées, souvent **noyés dans le bruit ambiant**.

Ce projet vise à résoudre ce problème à l’aide d’une méthode originale basée sur la transformation de Kravchuk et un test statistique non paramétrique.


## 🎯 Objectif final : 
Développer un outil fiable de détection automatique de cris d’oiseaux, en combinant l’analyse de la structure des zéros de Kravchuk avec un cadre de test d’hypothèse non paramétrique, afin de surveiller l’activité aviaire à partir d’enregistrements acoustiques en milieu naturel.

### Transformation de Kravchuk

La transformation de Kravchuk est une nouvelle représentation temps-fréquence adaptée aux signaux discrets.  
Elle encode le signal sous forme d’une fonction définie sur la sphère unité, permettant l’analyse de la structure de ses **zéros**.

### Différences dans la distribution des zéros

- **Bruit seul** : les zéros de la transformation de Kravchuk sont répartis de manière uniforme ;
- **Cri d’oiseau présent** : des **trous** apparaissent dans la configuration des zéros.

### Détection via une statistique spatiale

On utilise une statistique (comme la fonction **K de Ripley**) pour quantifier les différences dans la répartition des zéros.

## Utilisation du code

Le cadre du code provient du dépôt GitHub suivant :  
🔗 [https://github.com/bpascal-fr/kravchuk-transform-and-its-zeros](https://github.com/bpascal-fr/kravchuk-transform-and-its-zeros)  
Nous remercions chaleureusement **Madame Barbara Pascal** pour avoir fourni les bibliothèques permettant l’implémentation de la **transformée de Kravchuk**, ainsi que de la **fonction de Ripley**.

Sur cette base, nous avons ajouté de nouvelles fonctions et modules pour pouvoir traiter des **jeux de données réels**.

---

### Fichiers principaux

- `sliding_window_detection.py`  
  → Un détecteur basé sur **fenêtre glissante** est conçu pour parcourir les **points centraux** des clips audio extraits du jeu de données **BirdVox-70k**,  
  et détecter automatiquement la présence de **cris d’oiseaux** dans chaque fenêtre analysée.

- `csv_generated.py`  
  → Après avoir exécuté les cellules du notebook `detection-test-Kravchuk-zeros.ipynb`, vous obtiendrez de nombreux résultats affichés dans le terminal.  
  Copiez-les et collez-les dans un fichier au format `.txt`, puis placez ce fichier dans le dossier `csv/`.  
  Ensuite, exécutez le script `csv_generated.py` (en pensant à changer le nom du fichier de sortie),  
  ce qui vous permettra de générer un fichier `.csv` utilisable pour la visualisation.

- `region.py`  
  → En utilisant deux fichiers `.csv` générés à l’avance (positifs et négatifs), ce script permet de visualiser :  
    - le **test d’hypothèse unilatéral**  
    - la **courbe ROC**  
    - la **courbe Précision-Rappel (PR)**

- `noise_samples_from_real_negatives.py`  
  → Contrairement à la fonction `noise_samples`, cette version génère des échantillons de bruit à partir de clips **négatifs réels**,  
  enregistrés dans l’environnement naturel, pour remplacer le bruit blanc simulé par Monte Carlo.



##  Données

Nous remercions chaleureusement **Monsieur Vincent Lostanlen** et ses collaborateurs  
pour la mise à disposition du jeu de données BirdVox-70k :  
🔗 [https://zenodo.org/records/1226427](https://zenodo.org/records/1226427)

Le lien ci-dessus contient une description complète de la structure du jeu de données,  
ainsi que des informations sur la taille et le format des fichiers `.hdf5`.

---

### Pour exécuter les scripts de détection :

1. Téléchargez l’ensemble du dépôt GitHub (`Code` → `Download ZIP` ou via `git clone`) ;
2. Dans le répertoire principal du projet, créez un dossier nommé `data/`,  
   situé au même niveau que les dossiers `csv/`, `demo/`, `include/`, etc. ;
3. Placez les fichiers `.hdf5` téléchargés depuis Zenodo dans ce dossier `data/`.

Ensuite, vous pouvez exécuter les notebooks ou les scripts comme indiqué dans la section “Utilisation”.
