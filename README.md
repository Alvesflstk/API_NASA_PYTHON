# API de Dados de Astronautas

Esta é uma API desenvolvida com Flask que fornece informações confidenciais dos capacetes e trajes espaciais de astronautas.

## Funcionalidades

- **Endpoint `/confidencial`**: Retorna informações dos capacetes e trajes espaciais de astronautas.

## Estrutura do Projeto

O projeto consiste nos seguintes arquivos principais:

- `app.py`: Arquivo principal da aplicação Flask que define os endpoints da API.
- `index.html`: Arquivo de template HTML para a página inicial da aplicação (apenas renderiza um template básico).

## Pré-requisitos

- Python 3.x instalado.
- Flask instalado (`pip install Flask`).

## Instalação e Execução

1. Clone o repositório:

    ```bash
    git clone 
    ```

2. Instale as dependências:

    ```bash
    pip install Flask
    ```

3. Execute a aplicação:

    ```bash
    python app.py
    ```
## Endpoints

### `/`

- **Método:** GET
- **Descrição:** Retorna a página inicial da API.

### `/confidencial`

- **Método:** GET
- **Descrição:** Retorna informações confidenciais dos capacetes e trajes espaciais de astronautas.

### Exemplo de Uso

Para obter os dados confidenciais dos astronautas, faça uma requisição GET para `/confidencial`.

Exemplo de resposta:

```json
{
  "dr.man_capacete": "Dados do capacete do Dr. Man",
  "dra.brand_capacete": "Dados do capacete da Dra. Brand",
  "dr.man_traje": "Dados do traje do Dr. Man",
  "dra.man_traje": "Dados do traje da Dra. Brand"
}
