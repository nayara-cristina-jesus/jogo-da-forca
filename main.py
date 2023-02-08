## Jogo da Forca

import string
import random
from estrutura_forca import dicionario_visual_de_vidas
from palavras import palavras

def valida_palavra(palavras):
    palavra = random.choice(palavras)  
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)
    return palavra.upper()

def forca():
    palavra = valida_palavra(palavras)
    letras_de_palavras = set(palavra)  
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()  

    vidas = 7
   
    while len(letras_de_palavras) > 0 and vidas > 0:
        print('Você tem', vidas, 'vidas restantes e já tentou estas letras: ', ' '.join(letras_usadas))

        lista_de_palavra = [letra if letra in letras_usadas else '-' for letra in palavra]
        print(dicionario_visual_de_vidas[vidas])   
        print('Palavra: ', ' '.join(lista_de_palavra))

        letra_do_usuario = input('Letra: ').upper()
        if letra_do_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_do_usuario)
            if letra_do_usuario in letras_de_palavras:
                letras_de_palavras.remove(letra_do_usuario)
                print('')

            else:
                vidas = vidas - 1  
                print('\nA letra,', letra_do_usuario, 'não está na palavra.')

        elif letra_do_usuario in letras_usadas:
            print('\nVocê já tentou essa letra. Tente adivinhar outra letra.')

        else:
            print('\nEssa não é uma letra válida.')

    if vidas == 0:
        print(dicionario_visual_de_vidas[vidas])
        print('Infelizmente você foi enforcado. A palavra era', palavra)
    else:
        print('Uhu! Você adivinhou a palavra', palavra,'!!!')

forca()
