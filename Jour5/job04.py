def chiffre_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''
    for lettre in message:
        if lettre in alphabet:
            index = alphabet.index(lettre)
            index_decale = (index + decalage) % len(alphabet)
            lettre_chiffree = alphabet[index_decale]
            message_chiffre += lettre_chiffree
        else:
            message_chiffre += lettre
    return message_chiffre

message = "bonjour"
decalage = 3
message_chiffre = chiffre_cesar(message, decalage)
print(message_chiffre)