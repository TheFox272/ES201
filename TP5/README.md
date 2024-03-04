# TP5

## Q1

On suppose que les matrices sont de dimensions $n*n$ où $n = k*m$.

- Pi récupère les lignes de A suivantes : i, m+i, ..., (k-1)*m + i -> shared

![alt text](image.png)

- Tous les processeurs récupèrent B -> shared

![alt text](image-1.png)

- Pi écrit sur les lignes de C suivantes : i, m+i, ..., (k-1)*m + i -> modified, mais les autres ne les avaient pas donc pas de invalid

![alt text](image-2.png)
![alt text](image-3.png)

TODO : faire dessins ou tableaux pour mieux expliquer caches



