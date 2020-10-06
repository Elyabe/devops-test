
# :rocket: Nano API conteineirizada
[![Python](https://img.shields.io/static/v1?label=Python&message=3.8&colorA=purple&color=black&logo=Python&logoColor=white)](https://www.python.org/) [![Docker](https://img.shields.io/static/v1?label=Docker&message=v6&colorA=blue&color=black&logo=Docker&logoColor=white)](https://www.docker.com/) [![MySQL](https://img.shields.io/static/v1?label=PostgreSQL&message=11&colorA=darkblue&color=black&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

## :book: Overview 
Nano aplicação que gera gráfico de pizza do percentual de vendas de um supermercado por gênero (considerado apenas masculino e feminino) em um intervalo de datas a partir de uma base de dados.

Obs: Os dados de vendas foram obtidos na plataforma [Kaggle]() e pode ser acessado por este [link](https://www.kaggle.com/aungpyaeap/supermarket-sales)

### Sumário
* [Executando os scripts](#dark_sunglasses-executando_os_scripts)
* [Demonstração](#dark_sunglasses-Demonstração-da-aplicação)



## :dark_sunglasses: Executando os scripts

1. Clone este projeto;
    <pre> git clone https://github.com/Elyabe/vila-task-reminder.git </pre>

2. Configure as variáveis de ambiente execute o seguinte comando também na raíz do projeto
    <pre> cp .example.env .env </pre> 
3. Lance o container com o comando:
    <pre>docker-compose up --build -d</pre>

    A fim de facilitar as tarefas de desenvolvimento, a API está conteineirizada utilizando o <i> docker-compose</i> em três contêineres:

    - **ploomes**: Conteiner com nano API rest
    - **ploomes_db_postgres_1**: Conteiner suporte da base de dados Postgres 

    Aguarde até que o docker informe que os contêineres foram lançados com sucesso.


4. Teste o pequeno *script*
    
    4.1. **(Opcional)** Pode ser necessário conceder permissões de execução ao script.
            <pre>chmod +x run_test.sh</pre>

    4.2. Execute o teste
    - Popule a base de dados;
        <pre>sh run_test.sh init</pre>
    - Realize uma chamada à API;
        <pre>sh run_test.sh test</pre>
    - A imagem contendo o gráfico gerado pela API será disponibilizada no diretório atual;
    - Uma um link estará disponível também para visualização em um *browser*.


## :dark_sunglasses: Demonstração da aplicação

> [Vídeo demonstração](https://youtu.be/TiIDHRZhpXw)