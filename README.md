# Migration Updater

Este script Python foi desenvolvido para atualizar as migrations em um projeto, mantendo a ordem correta e adicionando a data atualizada aos arquivos.

## Estrutura de Pastas

- `migrations/`: Pasta principal
  - `input/`: Pasta contendo as migrations originais
  - `output/`: Pasta onde as migrations atualizadas serão armazenadas

## Requisitos

- Python 3.10

## Uso

1. Certifique-se de ter o Python 3 instalado em seu sistema.
2. Clone o repositório e navegue até a pasta do script.
3. Execute o script Python:

    ```bash
    python main.py
    ```

4. O script copiará as migrations da pasta `input` para a pasta `output`, atualizando as datas e mantendo a ordem correta.

## Personalização

- Se necessário, ajuste o script para atender a requisitos específicos.
- Os arquivos originais de migration devem seguir o padrão `YYYY_MM_DD_XXXXXX_migration_name.formato`.
