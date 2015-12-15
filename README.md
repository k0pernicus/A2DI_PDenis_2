# A2DI_PDenis_2

## Consignes

d1 : Romeo and Juliet
d2 : Juliet: O happy dagger
d3 : Romeo died by dagger
d4 : Live free or die, that's the New-Hampsphire motto"
d5 : Did you know, New-Hampsphire is in New England

q  : dies dagger

Q1. Créer la matrice terme-document pour d1, ..., d5 : X \in \mathbb{R}^{n \times 5} (n : taille du vocabulaire dans d1, ..., d5). X_{ij} : fréquence du mot i dans la document j.

Q2. Représenter la requête sous forme vectorielle : q \in \mathbb{R}^n.

Q3. Construire un classement sur d1, ..., d5 en termes de similarité par rapport à la requête (similarité définie comme la distance cosinus entre d_i et q). Commenter.

Q4. Faites une réduction des documents et de la requête en 2D en utilisant la SVD : Z_2 = U_2\Epsilon_2V_2^T.

Q5. Reclasser les documents en fonction de la requête, après projection dans l'espace réduit. Commenter et comparer avec le classemement original.

Q6. Visualiser documents et requête en 2D.
