with open("input.txt", "r") as file:
    password_list = file.readlines()

def is_valid_password(donne):
    # Supprimer les charctere extra comme 'retour à la ligne'
    donne = donne.strip()
    policy, lettre, password = donne.split()
    # Récupérer le min et max
    min, max = map(int, policy.split('-'))
    # Lettre à verifier
    lettre = lettre[0]
    # compter nombre d'occurence
    nbr_lettre = password.count(lettre)

    return min <= nbr_lettre <= max

somme = 0

for donne in password_list:
    if is_valid_password(donne):
        somme += 1

print(f"\nNombre de mot de passse valides est: {somme}")