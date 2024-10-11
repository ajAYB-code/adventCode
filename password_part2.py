with open("input.txt", "r") as file:
    password_list = file.readlines()

def is_valid_password(donne):
    # Supprimer les charctere extra comme 'retour à la ligne'
    donne = donne.strip()
    policy, lettre, password = donne.split()
    pos1, pos2 = map(int, policy.split('-'))
    # Lettre à verifier
    lettre = lettre[0]
    premier_position = password[pos1 - 1] == lettre
    second_position = password[pos2 - 1] == lettre

    return premier_position ^ second_position  # XOR pour "exactly one"

somme = 0

for donne in password_list:
    if is_valid_password(donne):
        somme += 1

print(f"\nNombre de mot de passse valides est: {somme}")