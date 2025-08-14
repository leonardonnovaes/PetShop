import json
import os

# --- Funções de Manipulação de Dados ---

def listar() -> None:
    """Listar os dados dos Pets Cadastrados"""
    try:
        # Verifica se o arquivo 'pets.json' existe no diretório atual.
        if os.path.exists('./pets.json'):
            # Abre o arquivo 'pets.json' no modo de leitura ('r') com a codificação UTF-8.
            with open('./pets.json', 'r', encoding='utf-8') as arquivo:
                # Carrega o conteúdo do arquivo JSON para uma lista Python.
                pets = json.load(arquivo)
                
                # Verifica se a lista de pets não está vazia.
                if len(pets) > 0:
                    # Itera sobre cada dicionário (pet) na lista.
                    for item in pets:
                        print('-'*40)
                        # Exibe as informações do pet de forma formatada.
                        print(f"Nome: {item['nome']}")
                        print(f"Tipo: {item['tipo']}")
                        print(f"Idade: {item['idade']}")
                else:
                    # Mensagem exibida se o arquivo existir, mas estiver vazio.
                    print('Não há pets cadastrados')
        else:
            # Mensagem exibida se o arquivo não existir.
            print('Não há pets cadastrados')
    except FileNotFoundError:
        # Trata o erro caso o arquivo não seja encontrado, embora a verificação já previna isso.
        print('ERRO: Não foi possível abrir o arquivo')


def inserir() -> None:
    """Cadastrar um novo Pet"""
    try:
        # Tenta abrir o arquivo para leitura.
        if os.path.exists('./pets.json'):
            with open('./pets.json', 'r', encoding='utf-8') as arquivo:
                # Se o arquivo existir, carrega os dados existentes para a lista.
                lista = json.load(arquivo)
        else:
            # Se o arquivo não existir, inicializa uma lista vazia para começar do zero.
            lista = []

        # Solicita os dados do novo pet ao usuário.
        nome = input('Nome: ')
        tipo = input('Tipo: ')
        idade = int(input('Idade: '))  # Converte a idade para um número inteiro.
        
        # Cria um novo dicionário com os dados informados.
        pet = {'tipo': tipo,
               'nome': nome,
               'idade': idade}
        
        # Adiciona o novo dicionário à lista de pets.
        lista.append(pet)
        
        # Abre o arquivo 'pets.json' no modo de escrita ('w').
        # O modo 'w' sobrescreve o arquivo se ele já existir.
        with open('./pets.json', 'w', encoding='utf-8') as arquivo:
            # Escreve a lista completa de pets no arquivo, formatada com indentação 4.
            # `ensure_ascii=False` garante que caracteres especiais (acentos, etc.) sejam salvos corretamente.
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        # Tratamento de erro se o arquivo não puder ser aberto.
        print('ERRO. O arquivo não pode ser aberto.')
    except ValueError:
        # Tratamento de erro se o usuário não digitar um número para a idade.
        print('ERRO. O valor informado para a idade deve ser inteiro')


def excluir() -> None:
    """Excluir um Pet"""
    try:
        # Verifica se o arquivo existe e se há pets para excluir.
        if os.path.exists('./pets.json'):
            pets = []
            with open('./pets.json', 'r', encoding='utf-8') as arquivo:
                pets = json.load(arquivo)
            
            # Se a lista de pets não estiver vazia.
            if len(pets) > 0:
                nome = input('Informe o nome do animal que será excluído: ')
                achou = False
                
                # Itera sobre a lista para encontrar e remover o pet.
                for item in pets:
                    if item['nome'] == nome:
                        pets.remove(item)
                        print('Pet excluído com sucesso')
                        achou = True
                        break  # Sai do loop após encontrar e remover o pet.
                
                # Se o pet foi encontrado e removido, atualiza o arquivo JSON.
                if achou is True:
                    with open('./pets.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(pets, arquivo, indent=4, ensure_ascii=False)
                else:
                    # Mensagem de erro se o pet não for encontrado.
                    print('Este Pet não está cadastrado')
            else:
                # Mensagem de erro se a lista estiver vazia.
                print('Não há pets cadastrados')
        else:
            # Mensagem de erro se o arquivo não existir.
            print('Não há pets cadastrados')
    except FileExistsError:
        # Tratamento de erro se o arquivo não puder ser aberto.
        print('ERRO: Não foi possível abrir o arquivo.')


# --- Função Principal e Menu ---

def menu() -> None:
    """Exibe menu principal do sistema"""
    while True:  # Loop infinito para manter o menu em execução.
        try:
            # Exibe as opções do menu.
            print('\n1 - Inserir')
            print('2 - Excluir')
            print('3 - Listar')
            print('4 - Sair')
            
            # Solicita a opção ao usuário e converte para inteiro.
            opcao = int(input('Escolha a Opção: '))
            
            # Utiliza a declaração `match` (disponível no Python 3.10+) para
            # chamar a função correspondente à opção escolhida.
            match opcao:
                case 1:
                    inserir()
                case 2:
                    excluir()
                case 3:
                    listar()
                case 4:
                    break  # Sai do loop `while True` para encerrar o programa.
                case _:
                    # Opção padrão para números fora do intervalo 1-4.
                    print('Opção inválida')
        except ValueError:
            # Tratamento de erro se o usuário não digitar um número inteiro.
            print('Digite um numero inteiro')

# Inicia o programa chamando a função do menu.
menu()