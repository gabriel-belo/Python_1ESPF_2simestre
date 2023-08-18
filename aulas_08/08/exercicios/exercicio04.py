def enviar_email(destinario, assunto= "Sem assunto", corpo= "")-> float:
    print(f"""{destinario}
              {assunto}
              {corpo}""")

a=str(input("Qual o destinatário: "))
b=str(input("Qual o assunto: "))
c=str(input("Digite o corpo: "))
mail=enviar_email(destinario=a, assunto=b, corpo=c)

# --------------------------------------------------------
# Do professor
def enviar_email(destinario, assunto= "Sem assunto", corpo= "")-> float:
    """
    Função recebe destinatário, assunto e corpode um email e exibe as informações
    Caso o assunto não seja informado será utilizado o valor 'sem assunto'
    Caso o corpo não seja informado será utilizado um valor vazio
    """
    print(f"Destinatário: {destinario}")
    print(f"Assunto: {assunto}")
    print(f"Corpo: {corpo}")
enviar_email('gadifrb@gmail.com', corpo="mensagem")