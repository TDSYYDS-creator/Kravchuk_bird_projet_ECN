## Kravchuk_bird_projet_ECN

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

### Fichiers ajoutés

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

(1) Nous remercions chaleureusement **Monsieur Vincent Lostanlen** et ses collaborateurs  
pour la mise à disposition du jeu de données BirdVox-70k : 🔗 [https://zenodo.org/records/1226427](https://zenodo.org/records/1226427)

Le lien ci-dessus contient une description complète de la structure du jeu de données,  
ainsi que des informations sur la taille et le format des fichiers `.hdf5`.

(2) Nous avons mis à disposition **quatre dossiers** : 🔗 [https://drive.google.com/drive/folders/18cDxAXZJbh4XTTbLQEua-LANR5nROBO3?usp=sharing](https://drive.google.com/drive/folders/18cDxAXZJbh4XTTbLQEua-LANR5nROBO3?usp=sharing)

- Trois d'entre eux contiennent des bruits générés par **simulation de Monte Carlo**, avec des fenêtres de longueur :
  - `samples_256`
  - `samples_512`
  - `samples_1024`

- Le quatrième dossier, `sample_real_neg_256`, contient des bruits **réels**, extraits à partir d'enregistrements annotés `0` (c’est-à-dire sans chant d’oiseau, uniquement du bruit ambiant naturel).

Cela permet de comparer la distribution des valeurs de la **fonction de Ripley** entre :
- les bruits générés artificiellement,
- et les bruits réels issus de l’environnement.

---

### Pour exécuter les scripts de détection :

1. Téléchargez l’ensemble du dépôt GitHub (`Code` → `Download ZIP` ou via `git clone`) ;
2. Dans le répertoire principal du projet, créez un dossier nommé `data/`,  
   situé au même niveau que les dossiers `csv/`, `demo/`, `include/`, etc. ;
3. Placez les fichiers `.hdf5` téléchargés depuis Zenodo dans ce dossier `data/`.
4. Placez le dossier choisi (`samples_256`, `samples_512`, etc.) dans le **répertoire principal** du projet (au même niveau que `csv`, `demo`, `scripts`, etc.)  
5. Renommez ce dossier en `samples`, pour que les scripts puissent l’utiliser automatiquement.

💡 **Exemple** :  
Si vous souhaitez tester avec une **fenêtre de 1024**, prenez le dossier `samples_1024`  
et **supprimez le suffixe `_1024`** → cela devient `samples`.

Ensuite, vous pouvez exécuter le notebook `detection-test-Kravchuk-zeros.ipynb`, et générer des données ainsi que des figures qui vous intéressent.

### Personnalisation de la génération de bruit

Vous êtes encouragé à modifier les paramètres et tester d’autres générations de bruit.

Dans le notebook `detection-test-Kravchuk-zeros.ipynb`, vous pouvez activer l’une des lignes suivantes pour générer les échantillons vous-même :

```python
# Génération de bruit de type Monte Carlo :
alpha, m, folder = noise_samples(N=512, m=m, time_t=time_t, folder='samples')

# Génération de bruit à partir de vrais extraits négatifs :
alpha, m, folder = noise_samples_from_real_negatives(
    h5_path='../data/BirdVox-70k_unit01.hdf5',
    keys_negative=keys_negative,
    N=256,
    m=199,
    time_t=np.arange(257),  # en accord avec ton STFT
    folder='samples'
)
