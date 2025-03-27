import preamble
import detection_test
import numpy as np
import scipy
import statsmodels


def sliding_window_detection(
    y, time_t, 
    window_size=1200, 
    step_size=600, 
    sr=24000, 
    alpha=0.05, 
    m=199, 
    folder='samples',
    functional='K'
):
    """
    Détection des cris d'oiseaux sur un signal à l’aide d’une fenêtre glissante.
    Chaque fenêtre a une longueur de `window_size` et un pas de glissement de `step_size`.
    
    Paramètres :
    - y : signal filtré (par exemple de longueur 12000)
    - time_t : tableau des timestamps correspondants
    - window_size : taille de chaque fenêtre (recommandé : 1200)
    - step_size : pas de glissement entre deux fenêtres (fenêtres chevauchantes)
    - sr : fréquence d’échantillonnage (utilisée uniquement pour l’axe temporel)
    - alpha : niveau de signification du test d’hypothèse
    - m : nombre d’échantillons Monte Carlo
    - folder : dossier contenant les échantillons de bruit
    - functional : 'K' ou 'F' (type de statistique fonctionnelle utilisée)

    Retourne :
    - detection_results : une liste contenant les résultats pour chaque fenêtre (0 ou 1), ainsi que la statistique résumée
    """
    detection_results = []
    total_len = len(y)
    len_demi = total_len // 2
    start = len_demi - window_size
    window_id = 1

    while start + window_size <= len_demi + window_size + 1:
        end = start + window_size
        nsignal = y[start:end]
        ntime_t = time_t[start:end]

        print(f" Fenêtre de détection {window_id} : [{start}:{end}]")

        # Effectuer le test
        threshold, t_exp = detection_test.the_test(nsignal, alpha, m, folder=folder, functional=functional)

        # Décider s’il s’agit d’un cri d’oiseau
        is_bird = int(t_exp > threshold)

        detection_results.append({
            "window": window_id,
            "start": start,
            "end": end,
            "threshold": threshold,
            "summary_stat": t_exp,
            "prediction": is_bird
        })

        print(f"→ Prédiction : {'Cris d’oiseau (1)' if is_bird else 'Bruit (0)'}")
        window_id += 1
        start += step_size

    return detection_results
