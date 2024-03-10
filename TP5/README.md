# TP5

## Analyse théorique de cohérence de cache

### Q1

On suppose que les matrices sont de dimensions $n*n$ où $n = k*m$.

- Pi récupère les lignes de A suivantes : i, m+i, ..., (k-1)*m + i -> shared

![alt text](image.png)

- Tous les processeurs récupèrent B -> shared

![alt text](image-1.png)

- Pi écrit sur les lignes de C suivantes : i, m+i, ..., (k-1)*m + i -> modified, mais les autres ne les avaient pas donc pas de invalid

![alt text](image-2.png)
![alt text](image-3.png)

TODO : faire dessins ou tableaux pour mieux expliquer caches


## Paramètres de l'architecture multicoeurs

### Q2 

| Paramètre      | Valeur par défault |
| -------------- | ------------------ |
| fetchQueueSize | 32                 |
| decodeWidth    | 8                  |
| issueWidth     | 8                  |
| commitWidth    | 8                  |
| LQEntries      | 32                 |
| SQEntries      | 32                 |



### Q3

| Cache   | Paramètre       | Valeur par défault   |
| ------- | --------------- | -------------------- |
| IL1     | Associativité   | 2                    |
|         | Taille          | 32KB                 |
|         | Taille ligne    | 64                   |
| ------- | --------------- | -------------------- |
| DL1     | Associativité   | 2                    |
|         | Taille          | 64KB                 |
|         | Taille ligne    | 64                   |
| ------- | --------------- | -------------------- |
| L2      | Associativité   | 8                    |
|         | Taille          | 2MB                  |
|         | Taille ligne    | 64                   |

## Architecture multicoeurs avec des processeurs superscalaires in-order (Cortex A7)

On se propose dans cette partie d’étudier une architecture multiprocesseur de type CMP à base de cœurs équivalents au Cortex A7 étudié dans le TP4. Dans notre simulateur gem5, le modèle de CPU associé à ce type de processeur est le modèle **arm_detailed** (--cpu-type=arm_detailed).

### Q4
Pour trouver le processeur exécutant toujours le plus grand nombre de cycles, on va réaliser notre simulation en fixant la taille **m** de la matrice et en faisant varier le nombre de threads parallèles de l'application, sans oublier qu'ici on a **n=ncores=nthreads**. 
On utilise donc les lignes de commande :
```
$GEM5/build/ARM/gem5.fast $GEM5/configs/example/se.py --cpu-type arm_detailed --caches -n n -c test_omp -o "n m"
nano m5out/stats.txt
```
Pour m = 4 :
| n | sim_insts | max cpu.numCycles |
|---|-----------|-------------------|
| 1 | 16577     | cpu : 80432       |
| 2 | 29651     | cpu0 : 84230      |
| 4 | 54655     | cpu0 : 85210      |

Pour m = 8 :
| n | sim_insts | max cpu.numCycles |
|---|-----------|-------------------|
| 1 | 25255     | cpu : 87302       |
| 2 | 38281     | cpu0 : 89502      |
| 4 | 64719     | cpu0 : 89610      |
| 8 | 123166    | cpu0 : 92672      |

Quelque soit la taille de la matrice, et le nombre de thread, c'est toujours le processeur de rang 0 qui effectue le plus grand nombre de cycles.





### Q5
D'après les résultats de la question 5 : 


### Q6

### Q7 
La valeur maximale de l'IPC s'obtient en calculant : 
$IPC_{max}=\frac{sim-insts}{max_{numCycles}}$

Pour m = 4 :
| n | sim_insts | max cpu.numCycles | IPC     |
|---|-----------|-------------------| --------|
| 1 | 16577     | cpu : 80432       | 0,20610 |
| 2 | 29651     | cpu0 : 84230      | 0,35202 |
| 4 | 54655     | cpu0 : 85210      | 0,64142 |

Pour m = 8 :
| n | sim_insts | max cpu.numCycles | IPC     |
|---|-----------|-------------------|---------|
| 1 | 25255     | cpu : 87302       | 0,28293 |
| 2 | 38281     | cpu0 : 89502      | 0,42771 |
| 4 | 64719     | cpu0 : 89610      | 0,72222 |
| 8 | 123166    | cpu0 : 92672      | 1,32905 |






