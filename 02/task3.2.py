n = int(input("Entrez les digits N à calculer : "))
m = int(input("Entrez les digits M à calculer : "))

def calculate_digits(x):
    return sum(int(digit) for digit in str(x))

somme_n = calculate_digits(n)
somme_m =calculate_digits(m)

resultat = somme_m * somme_n 


print(somme_n)
print(somme_m)
print(resultat)

