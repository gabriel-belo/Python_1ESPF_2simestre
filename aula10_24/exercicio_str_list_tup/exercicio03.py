def quantidade_vogais(texto:str)->str:
    texto.lower()
    cont=0
    for letra in  texto:
        if letra in "aeiou":
            cont+=1
    return cont
texto= str(input("Diigite um texto: "))
print(f"O número de vezes que essas letras aparecem no texto é {quantidade_vogais(texto)}")