1
def criar_contato(nome, telefone, email, favorito):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    if favorito == '1':
        contato['favorito'] = True
    else:
        contato['favorito'] = False
    contatos.append(contato)

def exibir_contatos(): 
    i = 1
    for contato in contatos:
        is_favorito = ' '
        if contato['favorito'] == True:
            is_favorito = 'X'

        print(f"({i})[Nome: {contato['nome']}|Telefone: {contato['telefone']}|Email: {contato['email']}|Favorito:[{is_favorito}]]")
        i=i+1
    print("--------------------------------------------------")

def editar_contato(id):
    contato_a_editar = contatos[int(id)-1]
    nome = input("Novo nome: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email: ")
    favorito = input("Contato favorito?\n(1) Sim\n(0) Não\n")
    contatos[int(id)-1] = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    print("Alteração realizada! \n")
    print("--------------------------------------------------")

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
        criar_contato(nome, telefone, email, favorito)
    elif opt == 2:
        exibir_contatos()
    elif opt == 3:
        id_contato = input("Qual contato deseja editar?")
        editar_contato(id_contato)
    elif opt == 4:
        print("Deleta um contato")
    elif opt == 5:
        print("Favorita/desfavorita um contato")
    elif opt == 6:
        print("Agenda encerrada")
        break
    else:
        print("Opção inválida. Por favor selecione a correta")
        