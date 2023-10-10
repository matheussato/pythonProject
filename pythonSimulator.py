#link do video: https://youtu.be/EAynY_qXrAM
#SUBALGORITMOS
margem = ' '*8
opcao = ""
cadastroEmpresas = dict()
cadastroCandidatos = dict()
cadastroRecrutadores = dict()
curriculo = dict()
vagas = dict()
registroVagas = list()


def opcaoDif(opcao):
    return opcao != 9


def opcaoMenu():
    return int(input("Digite agora a opção:"))


def incorreto():
    return print("Email ou senha incorretos.")


def linha():
    return print("=-=" * 20)


def emailCadastro():
    return input("Digite o email de cadastro: ")


def emailLogin ():
    return input("Digite seu email de login: ")


def senhaCadastro():
    return input("Digite a senha de cadastro: ")


def senhaLogin ():
    return input("Digite sua senha:")


def cadastroCandidato():
    if opcao == 1:
        linha()
    cadastroCandidatos['Email'] = input("Digite seu email de cadastro de candidato.....: ")
    cadastroCandidatos['Senha'] = input("Digite a sua senha de cadastro de candidato.....: ")
    cadastroCandidatos['Nome'] = input("Digite seu nome completo.....: ")
    cadastroCandidatos['Idade'] = input("Digite a sua data de nascimento.....: ")


def cadastroEmpresa():
    cadastroEmpresas['Email'] = input("Digite o email de cadastro da empresa.....: ")
    cadastroEmpresas['Senha'] = input("Digite a senha de cadastro da empresa.....: ")
    cadastroEmpresas['Nome'] = input("Digite o nome da empresa que deseja cadastrar.....: ")
    cadastroEmpresas['CNPJ'] = int(input("Digite o cnpj da empresa que deseja cadastrar.....: "))
    cadastroEmpresas['localTrabalho'] = input("Digite a localização da empresa.....: ")
    cadastroEmpresas['descricaoEmpresa'] = input("Digite uma breve descrição da sua empresa.....: ")

def cadastroRecrutador():
    cadastroRecrutadores['Email'] = input("Digite seu email de cadastro de recrutador.....: ")
    cadastroRecrutadores['Senha'] = input("Digite a sua senha de cadastro de recrutador.....: ")
    cadastroRecrutadores['Nome'] = input("Digite seu nome completo.....: ")
    cadastroRecrutadores['Empresa'] = input("Digite a sua empresa contratante.....: ")


def cadastroCurriculo():
    curriculo['Telefone'] = int(input("Digite o telefone de cadastro.....: "))
    curriculo['CPF'] = int(input("Digite o cpf de cadastro.....: "))
    curriculo['RG'] = int(input("Digite o rg de cadastro.....: "))
    curriculo['Area de Interesse'] = input("Digite a area de interesse em que deseja atuar.....: ")
    curriculo['Experiencia'] = input("Digite a sua experiência na area, caso possua alguma.....: ")
    curriculo['Idiomas'] = input("Digite os idiomas que você domina.....: ")
    curriculo['Horário preferencial'] = input("Digite o horário de preferência em que deseja trabalhar.....: ")
    curriculo['Curso'] = input("Digite o curso que você está fazendo.....: ")
    curriculo['Descrição das qualidades do candidato'] = input("Descreva suas qualidades em algumas linhas.....: ")


def criarVaga(vagas: dict, registroVagas: list, areaDaVaga: str) -> None:
    vagas['Area da vaga'] = areaDaVaga
    vagas['Tipo de vaga'] = input("A vaga é de estagio ou trabalho formal?.....: ")
    vagas['Tipo de trabalho'] = input("A vaga é remota ou presencial?.....: ")
    vagas['Carga horária semanal'] = input("Qual a carga horária semanal?.....: ")
    vagas['Jornada de trabalho'] = input("Qual a jornada de trabalho diária? (ex: das 9AM até as 17PM).....: ")
    vagas['Salário'] = input("Qual o salário ofertado para a vaga?.....: ")
    vagas['Ensino Superior'] = input("É necessário possuir ensino superior completo para esta vaga?.....: ")
    registroVagas.append(vagas.copy())


def listarVagas():
    print('--------------- Início da listagem ----------------')
    for i in range(0, len(vagas), 1):
        print(margem, end = '')
        print("Vaga : ", i+1)
        print(f"Area da vaga.......: {registroVagas[i]['Area da vaga']}")
        print(f"Tipo de vaga......: {registroVagas[i]['Tipo de vaga']}")
        print(f"Tipo de trabalho......: {registroVagas[i]['Tipo de trabalho']}")
        print(f"Carga horária semanal.......: {registroVagas[i]['Carga horária semanal']}")
        print(f"Jornada de trabalho......: {registroVagas[i]['Jornada de trabalho']}")
        print(f"Salário......: {registroVagas[i]['Salário']}")
        print(f"Necessita ensino superior?.......: {registroVagas[i]['Ensino Superior']}")
        print('--------------- Final da Listagem ----------------')



def menuPrincipal():
        print('''
        Você já possui cadastro?
        ----------------------------
        [ 1 ] - Não
        [ 2 ] - Sim
        [ 9 ] - Encerrar programa
    ''')


def menuLogin():
    print('''
        FAZER LOGIN NO SISTEMA
    ----------------------------
    [ 1 ] - Fazer login de candidato
    [ 2 ] - Fazer login de empresa
    [ 3 ] - Fazer login de recrutador
    [ 9 ] - Encerrar programa''')


def menuCadastro():
        print('''   
        FAZER CADASTRO NO SISTEMA
    ---------------------------- 
    [ 1 ] - Fazer cadastro de candidato
    [ 2 ] - Fazer cadastro de empresa
    [ 3 ] - Fazer cadastro de recrutador
    [ 9 ] - Encerrar programa
    ''')


def loginSucesso():
    print("Login realizado com sucesso!")


def menuCandidato():
    print('''
    MENU DO CANDIDATO | O que deseja fazer?
     ----------------------------
    [ 1 ] - Atualizar currículo
    [ 2 ] - Vagas disponíveis
    [ 0 ] - Voltar ao menu principal
    ''')


def menuEmpresa():
    print('''
    MENU DA EMPRESA | O que deseja fazer?
     ----------------------------
    [ 1 ] - Criar vaga
    [ 0 ] - Voltar ao menu principal
    ''')


def menuRecrutador():
        print('''
        MENU DO RECRUTADOR | O que deseja fazer?
         ----------------------------
        [ 1 ] - Gerenciar candidato
        [ 0 ] - Voltar ao menu principal
        ''')


#PROGRAMA PRINCIPAL


while opcaoDif(opcao):
    try:
        menuPrincipal()
        opcao = opcaoMenu()
    except ValueError as err:
        print("Formáto inválido. Insira um número.")
    if opcao == 1:
        linha()
        menuCadastro()
        linha()
        opcao = opcaoMenu()
        if opcao == 1:
            linha()
            cadastroCandidato()
        elif opcao == 2:
            linha()
            cadastroEmpresa()
        elif opcao == 3:
            linha()
            cadastroRecrutador()

    elif opcao == 2:
        linha()
        menuLogin()
        opcao = opcaoMenu()
        if opcao == 1:
            linha()
            emailCandidato = emailLogin()
            senhaCandidato = senhaLogin()
            if emailCandidato in cadastroCandidatos['Email'] and senhaCandidato in cadastroCandidatos['Senha']:
                loginSucesso()
                menuCandidato()
                opcao = opcaoMenu()
                linha()
                while True:
                    if opcao == 1:
                        linha()
                        cadastroCurriculo()
                    elif opcao == 2:
                        listarVagas()
                        linha()
                    elif opcao == 0:
                        break
            else: incorreto()
            linha()

        elif opcao == 2:
            linha()
            emailEmpresa = emailLogin()
            senhaEmpresa = senhaLogin()
            if emailEmpresa in cadastroEmpresas['Email'] and senhaEmpresa in cadastroEmpresas['Senha']:
                linha()
                loginSucesso()
                menuEmpresa()
                opcao = opcaoMenu()
                while True:
                    if opcao == 1:
                        linha()
                        print("\n" + margem + "****** [Digite . em area da vaga para finalizar o cadastro] ******")
                        areaVaga = input("Digite a area da vaga (ex: Analista de dados, desenvolvedor web,etc..).....: ")
                        if areaVaga != '.':
                            criarVaga(vagas, registroVagas, areaVaga)
                        else:
                            break
                    elif opcao == 0:
                        break
            else: incorreto()
            linha()

        elif opcao == 3:
            linha()
            emailRecrutador = emailLogin()
            senhaRecrutador = senhaLogin()
            if emailRecrutador in cadastroRecrutadores['Email'] and senhaRecrutador in cadastroRecrutadores['Senha']:
                linha()
                loginSucesso()
                menuRecrutador()
                opcao = opcaoMenu()
                while True:
                    if opcao == 1:
                        break
                        ... #DESENVOLVIMENTO FUTURO
                    elif opcao == 0:
                        break
            else: incorreto()
            linha()



    elif opcao == 9:
         exit()
    else: print("Opção inválida. Tente novamente.")
    linha()
    linha()