import string
import random
import time

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
        while True:
            iters += 1
            result = ''.join(random.choices(characters, k=len(sentence)))
            if result == sentence:
                duration = time.time() - start
                break
        return iters, duration
