def objetos(itens:str)->str:
    '''
    Imprime os itens de uma lista
    '''
    for elemento in itens:
        print(elemento)
lista=[]
continuar=""
while "N" not in continuar:
    produto=str(input("Qual itens deseja colocar: "))
    continuar=str(input("Gostaria de continuar: ")).strip().upper()
    lista.append(produto)
objetos(lista)#chamar a função