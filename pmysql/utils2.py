import MySQLdb


def conectar():
    try:
        conn = MySQLdb.connect(
            db='produtos',
            host='localhost',
            user='kleuber',
            password='kleuber201317',
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexao ao banco de dados {e}')


def desconectar(conn):
    if conn:
        conn.close()


def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando Produtos')
        print('-----------------')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Nome: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print('----------------------')
    else:
        print('Infelizmente ainda nao existem veículos cadastrados')
    desconectar(conn)


def inserir():
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do veículo: ')
    preco = float(input('Informe o valor do veículo: R$'))
    estoque = int(input('Informe a quantidade de veículos no pátio: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'veículo {nome} foi inserido com sucesso!')
    else:
        print('Erro ao realizar o cadastro do veículo')
    desconectar(conn)


def atualizar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do veículo cujo qual deseja atualizar: '))
    nome = input('Informe o nome do veículo: ')
    preco = float(input('Informe o valor do veículo: '))
    estoque = int(input('Informe a quantidade de veículos no pátio: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print('O veículo foi atualizado com sucesso')
    else:
        print(f'Erro ao atualizar o veículo de código {codigo}')
    desconectar(conn)


def deletar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o ID do veículo que deseja excluir: '))

    cursor.execute(f"DELETE FROM produtos WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Veículo com ID:{codigo} excluido com sucesso!')
    else:
        print('Erro ao tentar excluir veículo com código informado.')
    desconectar(conn)


def menu():
    print('===========Gerenciador de Produtos==============')
    print('Selecione uma opçao:')
    print('1 - Listar Veículos')
    print('2 - Inserir Veículo')
    print('3 - Atualizar Veículo')
    print('4 - Excluir Veículo')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opçao inválida!')
    else:
        print('Opçao inválida!')
