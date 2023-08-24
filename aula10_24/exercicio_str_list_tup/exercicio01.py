def conta_caracteres(texto: str)-> str:
    """Recebe uma string e retorne o número de cractéres nela"""
    return len(texto)

def converte_maiusculo(texto: str)->str:
    """Recebe uma string e retorna ela em maiúsculo"""
    return texto.upper()

texto=str(input("Digite uma frase:"))
print(f"Quantidade de caracteres {conta_caracteres(texto)}")
print(converte_maiusculo(texto))