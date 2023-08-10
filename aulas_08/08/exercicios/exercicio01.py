def mostrar_informacoes(nome: str, idade: int, cidade: str)-> None:
    print(f"O cidadão {nome}, tem {idade} anos  e reside na cidade {cidade}")
#  caso tivesse return nome a -> seria str e não none, mas como não tem 
# return é none 
a=str(input("Nome: "))
b=int(input("Idade: "))
c=str(input("Cidade: "))

mostrar_informacoes(nome= a, idade= b, cidade= c)