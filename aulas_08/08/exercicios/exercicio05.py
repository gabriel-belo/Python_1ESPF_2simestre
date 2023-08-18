def concatenar_strings(string1:str,string2:str,separador:str=" ")->str:
    print(f"{string1}{separador}{string2}")

primeiro=str(input("Digite a primeira string: "))
segunda=str(input("Digite a segunda string: "))
concatenar_strings(primeiro,segunda)
# -------------------------------------------------------------
# DO PROFESSOR
def concatenar_strings(string1:str,string2:str,separador:str=" ")->str:
    return string1 + separador + string2
a="banana"
b="abacaxi"
print(concatenar_strings(a,b,"---"))
print(concatenar_strings(a,b,"--"))
print(concatenar_strings(a,b))
