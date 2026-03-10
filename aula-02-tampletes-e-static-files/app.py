# importando o flask para a aplicação.

from flask import Flask, render_template

# Carregando o Flask na variavel "APP".
# Declarando variavel no Python.

app = Flask(__name__, template_folder='Views')

# Variaveis com  _ são variáveis de ambiente no Python.
# (__name__) representa o nome da aplicação.

# Criando a rota pricipal do site.


@app.route('/')
# DEF cria funções no python.
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    # Criando variaveis para a rota de GAMES.

    titulo = "Portal 2"
    ano = 2011
    categoria = "Puzzle"
    # Enviando as variaveis para o HTML.
    return render_template('games.html', titulo=titulo, ano=ano,  categoria=categoria, jogadores=jogadores)


# Lista de Jogadores (uma lista e um vetor/array)
jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']


@app.route('/consoles')
def consoles():
    # Criando um Objeto.
    Console = {"Nome": " Playstation 2", "Fabricante": "Sony", "Ano": 2000}
    return render_template('consoles.html', Console=Console)

# Iniciando o servidor na porta 5000.
# O metodo .run() inicia o servidor.
# Esta verificando se o arquivo gravado em __name__ é o arquivo principal.


if __name__ == '__main__':
    app.run(port=5000, debug=True)
