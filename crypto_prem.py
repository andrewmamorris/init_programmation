#definitions variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def code_make():
    #input mot et indice
    index = 0
    lettre = alphabet[index]
    mot_a_cacher = input("Secret word: ")
    decalage = int(input("Key: "))
    output_mot = ""

    #opérations:
    #boucle for qui parcourt le mot

    #if in alph: alph+= pour incrémenter
    for c in mot_a_cacher:
        index = alphabet.index(c)
        if c in alphabet:
            index = ((index + decalage) % 26)
            output_mot += alphabet[index]
    print(output_mot)

if __name__ == "__main__":
    code_make()