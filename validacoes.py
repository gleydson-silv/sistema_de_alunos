def texto_valido(texto):
    return texto.replace(" ", "").isalpha()

def idade_valida(idade):
    return isinstance(idade, int) and idade > 0

