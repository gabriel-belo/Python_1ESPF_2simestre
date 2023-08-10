# tipos de parâmetros: nomeado e posicionais
# anotação dos tipos de parâmetros
def media(nota2: float=0, nota3: float=0, nota1: float=0)-> float:
    m=(nota1+ nota2 + nota3)/ 3
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    return m
