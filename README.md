# Analisador Financeiro de Criptomoedas

Este projeto consiste em uma API desenvolvida em Python utilizando o framework FastAPI para análise financeira de criptomoedas.

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/Hargenx/FastAPI_Exemplo.git
    ```

2. Instale as dependências:

    ```bash
    cd FastAPI_Exemplo
    pip install -r requirements.txt
    ```

## Uso

1. Execute o servidor localmente:

    ```bash
    uvicorn main:app --reload
    ```

2. Acesse a documentação da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para visualizar e testar os endpoints.

## Endpoints

- `GET /`: Retorna uma mensagem de boas-vindas.
- `GET /crypto/{crypto_id}`: Obtém dados de uma criptomoeda específica.
- `GET /crypto/{crypto_id}/calculate_value`: Calcula o valor de uma quantidade específica de uma criptomoeda.
- `POST /crypto/{crypto_id}/calculate_value_with_model`: Calcula o valor de uma quantidade específica de uma criptomoeda usando um modelo Pydantic.

## Contribuição

Sinta-se à vontade para contribuir com melhorias! Abra um Pull Request ou crie uma issue para discutir ideias e novas funcionalidades.

## Autor

[Raphael M. S. de Jesus](https://github.com/Hargenx)

## Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).
