# Gerenciador de Pets

Este é um sistema simples de gerenciamento de pets em linha de comando, que permite cadastrar, listar e excluir informações de animais. Os dados são armazenados de forma persistente em um arquivo JSON (`pets.json`), garantindo que as informações não sejam perdidas ao encerrar o programa.

-----

### Funcionalidades

  - **Inserir Pet**: Adicione um novo animal à sua coleção, informando seu nome, tipo e idade.
  - **Listar Pets**: Exibe todos os pets cadastrados no sistema, com suas respectivas informações.
  - **Excluir Pet**: Remova um pet da sua lista, buscando-o pelo nome.
  - **Menu Interativo**: Um menu de fácil navegação para acessar todas as funcionalidades.
  - **Persistência de Dados**: As informações dos pets são salvas em um arquivo JSON, o que permite que você feche e reabra o programa sem perder seus dados.
  - **Tratamento de Erros**: O programa lida com erros comuns, como entradas inválidas ou arquivos não encontrados, oferecendo uma experiência mais robusta.

-----

### Como Usar

1.  **Execute o Script**: Basta rodar o arquivo Python no seu terminal.

    ```bash
    python main.py
    ```

2.  **Navegue pelo Menu**: O programa irá exibir o menu principal com as seguintes opções:

      - `1 - Inserir`
      - `2 - Excluir`
      - `3 - Listar`
      - `4 - Sair`

3.  **Interaja**: Digite o número da opção desejada e pressione `Enter`. O programa irá guiá-lo para a ação escolhida. Se você inserir um nome de pet que não existe para exclusão, ou digitar um valor inválido, o programa irá notificá-lo e retornar ao menu principal.

-----

### Estrutura do Código

  - `listar()`: Lê o arquivo `pets.json` e imprime os detalhes de cada pet.
  - `inserir()`: Solicita os dados de um novo pet, adiciona-o à lista e salva a lista atualizada no arquivo JSON.
  - `excluir()`: Pede o nome de um pet, remove-o da lista e atualiza o arquivo JSON.
  - `menu()`: A função principal que exibe o menu de opções e utiliza a estrutura `match-case` para chamar as funções correspondentes.
  - **Arquivo `pets.json`**: Onde todos os dados dos pets são armazenados de forma estruturada. Se o arquivo não existir, o programa o criará automaticamente.
