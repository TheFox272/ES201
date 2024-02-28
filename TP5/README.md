# TP5

## Q1

On suppose que les matrices sont de dimensions $n*n$ où $n = k*m$.

- Pi récupère les lignes de A suivantes : i, m+i, ..., (k-1)*m + i -> shared
- Tous les processeurs récupèrent B -> shared
- Pi écrit sur les lignes de C suivantes : i, m+i, ..., (k-1)*m + i -> modified, mais les autres ne les avaient pas donc pas de invalid

TODO : faire dessins ou tableaux pour mieux expliquer caches



