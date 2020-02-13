# Le module operator fournit des fonctions mathématiques. Utile lorsque l’opérateur mathématique est fournit par un user input.
import operator
# Le but de cet exercice est de créer une calculatrice qui prend 3 input de l'utilisateur et effectue le calcul demandé

# Salutation
print('Bienvenue dans ma petite calculatrice')

# Store l'input du premier nombre en int
num1 = int(input("Entrez un premier nombre : "))

# Store l'input de l'opérateur en string
ops = input("Entrez un opérateur mathématique (+, -, *, /) : ")

# Store l'input du 2e nombre en int
num2 = int(input("Entrez un deuxième nombre : "))

# Associe le string de l'opérateur à sa fonction mathématique appropriée
math = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# Vérifie que l'opérateur est valide
if ops not in math :
    print("Veuillez recommencer et entrez un opérateur valide")
else:
    # Appel la fonction en passant par le dictionnaire en lui envoyant les arguments de manière "concaténée"
    print(math[ops](num1, num2))
