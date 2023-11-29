def est_nombre(terme):
    try:
        float(terme)
        return True
    except ValueError:
        return False

# Fonctions pour les opérations
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division par zéro impossible.")

# Priorités des opérations (La priorité sera plus forte sur les opérateurs définis à 2)
priorites = {'+': 1, '-': 1, '*': 2, '/': 2}

def evaluer(expression):
    nombres = []
    operateurs = []

    for terme in expression:
        if est_nombre(terme):
            nombres.append(float(terme))

        elif terme in priorites:
            while operateurs and priorites[terme] <= priorites[operateurs[-1]]:
                operateur = operateurs.pop()
                b = nombres.pop()
                a = nombres.pop()
                if operateur == '+':
                    nombres.append(addition(a, b))
                elif operateur == '-':
                    nombres.append(soustraction(a, b))
                elif operateur == '*':
                    nombres.append(multiplication(a, b))
                elif operateur == '/':
                    nombres.append(division(a, b))
            
            operateurs.append(terme)

    while operateurs:
        operateur = operateurs.pop()
        if nombres:
            b = nombres.pop()
        else:
            raise ValueError("Expression mathématique invalide. Vérifiez le format.")
        if nombres:
            a = nombres.pop()
        else:
            raise ValueError("Expression mathématique invalide. Vérifiez le format.")
        if operateur == '+':
            nombres.append(addition(a, b))
        elif operateur == '-':
            nombres.append(soustraction(a, b))
        elif operateur == '*':
            nombres.append(multiplication(a, b))
        elif operateur == '/':
            nombres.append(division(a, b))

    return nombres[0]

expression = input("""
                   
            Veuillez entrer une expression mathématique
            (ex: 2 + 3 * 2 / 4) 
            
            Opérateur disponible:
            +   -   /   *
                   
            """)
termes = expression.split()

resultat = evaluer(termes)
print("Résultat :", resultat)
