n = int(input("Entrez les digits à calculer : "))

def calculate_digits(n):
    return sum(int(digit) for digit in str(n))

print(calculate_digits(n))
