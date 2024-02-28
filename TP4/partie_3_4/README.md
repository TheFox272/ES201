
Q6 
On récupère l'archive 
wget "https://hpl.hp.com/research/cacti/cacti65.tgz" --no-check-certificate
On y trouve un fichier 'cache.cfg'

Les valeurs qui y sont utilisées sont :
Une taille de cache de 128Mio
Une taille de bloc de 64o
Et une associativité de 1
La technologie par défaut est de 0.032µm




Q7

Pour chaqu processeur et chaque cache, on crée un fichier de configuration correspondant à notre modèle :
En indiquant la taille de la mémoire, taille de bloc, associativité, et qu'il s'agit dune mémoire de type 'cache' et non 'main memory' comme par défaut.

On laisse les autres paramètres comme dans l'exemple, y compris la technologie par défaut de 0.032µm, puisque cacti6.5 ne supporte pas le 0.028µm

On somme les valeurs d'aire des sections 'Data array' et 'Tag array' récupèrées dans le texte emis par cacti
L'aire du processeur est calculé

 --- Processeur Cortex A7  --- 
Surface processeur sans caches : 0.373mm²
Surface de chaque cache L1 : 0.0384mm²
Surface du cache L2 : 0.446mm²
Les caches L1 occupent 17.1% de l'ensemble coeur + caches L1

--- Processeur Cortex A15  --- 
Surface processeur sans caches : 1.93mm²
Surface de chaque cache L1 : 0.0346mm²
Surface du cache L2 : 0.399mm²
Les caches L1 occupent 3.5% de l'ensemble coeur + caches L1

Q8

# Area.png

Q9

# Efficiency.png