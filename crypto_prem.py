#definitions variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = 0
lettre = alphabet[index]

#input mot et indice
mot_a_cacher = input("Secret word: ")
decalage = int(input("Key: "))

#opérations:
#boucle for qui parcourt le mot

#if in alph: alph+= pour incrémenter
for c in mot_a_cacher:
    if c in alphabet:
        index += ((26 + decalage) % 26)
    print(alphabet[index])