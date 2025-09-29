import math

n = int(input("Donne un nombre n : "))
resultat = 1
i = 1

while i <= n:
    resultat = resultat * i // math.gcd(resultat, i)
    i = i + 1

print(resultat)
