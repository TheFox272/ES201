# TP4

## Profiling de l'application

### Q1

#### dijkstra_small
```
sim-profile -iprof dijkstra/dijkstra_small.ss input.dat
```

| Opcode |Format |  Count  | PDF  |
|--------|-------|---------|------|
| nop    |       | 64      | 0.00 |
| j      | J     | 17839   | 0.26 |
| jal    | J     | 27954   | 0.40 |
| jr     | s     | 28142   | 0.40 |
| jalr   | d,s   | 131     | 0.00 |
| beq    | s,t,j | 655160  | 9.41 |
| bne    | s,t,j | 361695  | 5.19 |
| blez   | s,j   | 2141    | 0.03 |
| bgtz   | s,j   | 121     | 0.00 |
| bltz   | s,j   | 7       | 0.00 |
| bgez   | s,j   | 4053    | 0.06 |
| lb     | t,o(b)| 1573    | 0.02 |
| lbu    | t,o(b)| 1954    | 0.03 |
| lhu    | t,o(b)| 61      | 0.00 |
| lw     | t,o(b)| 1676440 | 24.08|
| dlw    | t,o(b)| 89      | 0.00 |
| sb     | t,o(b)| 1364    | 0.02 |
| sw     | t,o(b)| 718789  | 10.32|
| dsw    | t,o(b)| 89      | 0.00 |
| addu   | d,s,t | 1323295 | 19.01|
| addiu  | t,s,i | 398995  | 5.73 |
| subu   | d,s,t | 9272    | 0.13 |
| mult   | s,t   | 376     | 0.01 |
| divu   | s,t   | 356     | 0.01 |
| mfhi   | d     | 376     | 0.01 |
| mflo   | d     | 732     | 0.01 |
| and    | d,s,t | 559     | 0.01 |
| andi   | t,s,u | 11867   | 0.17 |
| or     | d,s,t | 840     | 0.01 |
| ori    | t,s,u | 2467    | 0.04 |
| xor    | d,s,t | 699     | 0.01 |
| xori   | t,s,u | 62      | 0.00 |
| nor    | d,s,t | 1761    | 0.03 |
| sll    | d,t,H | 1016315 | 14.60|
| sllv   | d,t,s | 16772   | 0.24 |
| srl    | d,t,H | 8507    | 0.12 |
| srlv   | d,t,s | 2405    | 0.03 |
| sra    | d,t,H | 4277    | 0.06 |
| srav   | d,t,s | 2126    | 0.03 |
| slt    | d,s,t | 198080  | 2.84 |
| slti   | t,s,i | 212241  | 3.05 |
| sltu   | d,s,t | 24318   | 0.35 |
| sltiu  | t,s,i | 5454    | 0.08 |
| syscall|       | 70      | 0.00 |
| lui    | t,U   | 222989  | 3.20 |

#### blowfish
```
sim-profile -iprof blowfish/bf.ss e input_small.asc output_small.enc 1234567890abcdeffedcba0987654321
```

| Opcode | Format| Count | PDF  |
|--------|-------|-------|------|
| nop    |       | 5     | 0.00 |
| j      | J     | 583   | 0.28 |
| jal    | J     | 632   | 0.30 |
| jr     | s     | 642   | 0.31 |
| jalr   | d,s   | 12    | 0.01 |
| beq    | s,t,j | 938   | 0.45 |
| bne    | s,t,j | 1636  | 0.78 |
| blez   | s,j   | 1     | 0.00 |
| bgtz   | s,j   | 1     | 0.00 |
| bltz   | s,j   | 6     | 0.00 |
| bgez   | s,j   | 10    | 0.00 |
| lb     | t,o(b)| 41    | 0.02 |
| lbu    | t,o(b)| 101   | 0.05 |
| lh     | t,o(b)| 32    | 0.02 |
| lhu    | t,o(b)| 1     | 0.00 |
| lw     | t,o(b)| 46659 | 22.21|
| sb     | t,o(b)| 25    | 0.01 |
| sw     | t,o(b)| 6873  | 3.27 |
| addu   | d,s,t | 52190 | 24.84|
| addiu  | t,s,i | 5068  | 2.41 |
| subu   | d,s,t | 36    | 0.02 |
| mult   | s,t   | 1     | 0.00 |
| divu   | s,t   | 1     | 0.00 |
| mflo   | d     | 2     | 0.00 |
| and    | d,s,t | 65    | 0.03 |
| andi   | t,s,u | 25212 | 12.00|
| or     | d,s,t | 77    | 0.04 |
| ori    | t,s,u | 43    | 0.02 |
| xor    | d,s,t | 26161 | 12.45|
| xori   | t,s,u | 2     | 0.00 |
| nor    | d,s,t | 98    | 0.05 |
| sll    | d,t,H | 16899 | 8.04 |
| sllv   | d,t,s | 38    | 0.02 |
| srl    | d,t,H | 25056 | 11.93|
| sra    | d,t,H | 62    | 0.03 |
| srav   | d,t,s | 6     | 0.00 |
| slt    | d,s,t | 1     | 0.00 |
| slti   | t,s,i | 575   | 0.27 |
| sltu   | d,s,t | 131   | 0.06 |
| sltiu  | t,s,i | 88    | 0.04 |
| syscall|       | 10    | 0.00 |
| lui    | t,U   | 87    | 0.04 |


### Q2

On remarques que les instructions suivantes globalement sont les plus utilisés :

| Opcode | Description | PDF dijkstra | PDF blowfish |
|--------|-------------|--------------|---------------|
| lw     | Load Word   | 24.08 %      | 22.21 %       |
| sw     | Store Word  | 10.32 %      | 3.27 %        |
| addu   | Add Unsigned| 19.01 %      | 24.84 %       |
| sll    | Shift Left Logical | 14.60 % | 8.04 %   |

Ainsi, ces instructions semblent cruciales dans l'exécution de ces programmes, et mériteraient une optimisation plus poussée. Par exemple, rien qu'en divisant le temps de addu par 3 on obtiendrait :
$$
f_{blowfish} = 0.25
$$
$$
S_{blowfish} = \frac{1}{(1 - f) + \frac{f}{3}} = 1.2
$$


### Q3

Les résultats du TP2 révèlent des similitudes et divergences comportementales entre Dijkstra, BlowFish, SSCA2-BCS, SHA-1 et le produit de polynômes (P1). En général, Dijkstra, BlowFish, SSCA2-BCS et SHA-1 présentent une utilisation notable des instructions de calcul entier, indiquant un traitement de données entières. SSCA2-BCS se distingue par un nombre significatif d'accès mémoire, caractéristique des applications de traitement de graphes. En revanche, le produit de polynômes (P1) se démarque par une forte utilisation d'instructions flottantes, liée à la nature de l'algorithme de multiplication de polynômes. Des recommandations spécifiques émergent, telles que l'optimisation des instructions flottantes pour P1 et l'optimisation de la hiérarchie mémoire pour SSCA2-BCS.  

En conclusion, les différences de comportement reflètent la nature spécifique des algorithmes mis en œuvre, guidant ainsi les recommandations d'optimisation adaptées à chaque application.





