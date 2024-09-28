import string
import random
import time
import math

# Listas de caracteres posibles:
letters_low = list(string.ascii_lowercase)
letters_upp = list(string.ascii_uppercase)
special = ['.', ',', ';', '-', ' ', '¿', '?', '¡', '!', 'ñ', 'Ñ']
# Lista concatenada:
chars = []
chars.extend(letters_low)
chars.extend(letters_upp)
chars.extend(special)

# Función del mono:
def monkey_writting(sentence: str, characters=chars):
    '''
    Función del mono escribiendo.

    Parámetros:
    --------
    - sentence: Cadena de texto a simular. De preferencia una sola palabra.
    - charcaters (opcional): Lista customizada de caracteres que el mono va tecleando.

    Devuelve:
    --------
    - iters: Iteraciones que realizó el programa.
    - duration: Duración (en segundos) del programa.
    - probab: Probabilidad N (1 en N) de que el mono tipee la cadena de texto ingresada.
    '''
    iters = 0
    start = time.time()
    validation = True
    for char in sentence:
        if char not in chars:
            validation = False
            break
    if not validation:
        return 'Error', 'Error'
    else:
        result = ''.join(random.choices(characters, k=len(sentence)))
        probs = [(1/len(chars))**-1 for i in range(len(sentence))]
        probab = int(math.prod(probs))
        while True:
            iters += 1
            if result == sentence:
                duration = time.time() - start
                break
            else:
                result = result[1:] + random.choices(characters)[0]
        return iters, duration, probab
