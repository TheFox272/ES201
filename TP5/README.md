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


