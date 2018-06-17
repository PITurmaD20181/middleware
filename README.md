# middleware

# Instalando as dependências

Este projeto utiliza o `Python3`. Recomendamos o Python na versão `3.6.4`. As dependências do python estão descritas no arquivo `requirements.txt`

1 - Clone o projeto
```shell
git clone https://github.com/PITurmaD20181/middleware.git
```

2 - Entre na pasta do projeto
```shell
cd middleware/
```

3 - Instale as dependências do python, utilizando  o `pip3`:

```shell
pip3 install -r requirements.txt
```

# Executando a aplicação

1 - Tenha a API sendo servida no endereço `0.0.0.0:8000`, com o banco de dados já populado.

2 - A aplicação espera que o arquivo de matriculas esteja com o nome `Chamada.txt`. Caso queira utilizar um arquivo diferente, modifique o código `main.py` ou renomeie o arquivo desejado para `Chamada.txt`. Este arquivo já se encontra no projeto com alguns exemplos.

3 - Execute o script `main.py`:

```shell
python3 main.py
```
