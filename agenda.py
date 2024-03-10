def criar_contato(nome, telefone, email, favorito):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    contatos.append(contato)

def exibir_contatos():
    print(contatos)

contatos = []

while True:
    print("Agenda de Contatos")
    print("--------------------------------------------------")
    print("(1) Novo contato")
    print("(2) Exibir contatos")
    print("(3) Editar contato existente")
    print("(4) Excluir contato")
    print("(5) Favoritar/Desfavoritar um contato existente")
    print("(6) Sair da agenda")
    print("--------------------------------------------------")

    opt = int(input("Digite a opção: "))

    if opt == 1:
        print("Novo Contato")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        favorito = input("Contato favorito?\n(1) Sim\n(0) Não\n")
        criar_contato(nome, telefone, email, bool(favorito))
    elif opt == 2:
        exibir_contatos()
    elif opt == 3:
        print("Altera um contato")
    elif opt == 4:
        print("Deleta um contato")
    elif opt == 5:
        print("Favorita/desfavorita um contato")
    elif opt == 6:
        print("Agenda encerrada")
        break
    else:
        print("Opção inválida. Por favor selecione a correta")
        