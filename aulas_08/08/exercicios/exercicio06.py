def comprar_produto(produto:str="Produto desconhecido", quantidade: int=1):
    '''
    Retornar uma string com a informação da compra realizada
    '''
    print(f"O produto comprado é {produto} e a quantidade é {quantidade}")

p=str(input("Qual o produto: "))
q=int(input("Quantos produtos: "))
compra=comprar_produto(p, q)