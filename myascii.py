def get_ascii(character):
    """Obtiene la representación en byte de un carácter."""
    return format(ord(character), '08b')

def get_binary(word):
    """Obtiene la representación en byte de una palabra."""
    return ' '.join(format(ord(char), '08b') for char in word)

def get_results(character, word):
    """Obtiene los resultados para un carácter y una palabra."""
    result_character = get_ascii(character)
    result_word = get_binary(word)
    return result_character, result_word