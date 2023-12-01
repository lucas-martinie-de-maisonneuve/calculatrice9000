historique_calcul = []
historique_resultat = []

print("""
                Opérateurs disponibles : +   -   /   *
                Au format 2 + 3 * 2 / 4""")

def est_nombre(terme):
    try:
        float(terme)
        return True
    except ValueError:
        return False

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
        else:
            raise ValueError(f"Opérateur non pris en charge : {terme}")

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

    if len(nombres) == 1:
        return nombres[0]
    else:
        raise ValueError("Expression mathématique invalide. Vérifiez le format.")

while True:
    expression = input("""
    |-----------------------------------------------------------|
    |        'his' pour historique / 'del' pour l'effacer       |
    |    Veuillez entrer une expression mathématique ci-dessous |
    |-----------------------------------------------------------|
                       
        ===> """)
    historique_calcul.append(expression)

    if expression.lower() == 'his':
        if historique_calcul and historique_resultat:
            print("""
                    Historique des résultats:""")
            for i, (calcul, resultat) in enumerate(zip(historique_calcul, historique_resultat), 1):
                print(f"""

                {i}. {calcul} = {resultat}""")
        else:
            print("""
                    L'historique est vide.""")
    elif expression.lower() == 'del':
        historique_calcul = []
        historique_resultat = []
        print("""
                    Historique effacé.""")
    else:
        while True:
            try:
                termes = expression.split()
                resultat = evaluer(termes)
                historique_resultat.append(resultat)
                print(f"""
                    {expression} = {resultat}""")
                break
            except ValueError as e:
                print(f"Erreur : {str(e)}.")
                expression = input("""
         
        ===> """)
                historique_calcul.append(expression)
