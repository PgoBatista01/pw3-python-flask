# importando o flask para a aplicação.

from flask import Flask, render_template

# Carregando o Flask na variavel "APP".
# Declarando variavel no Python.

app = Flask(__name__, template_folder ='Views')

# Variaveis com  _ são variáveis de ambiente no Python.
# (__name__) representa o nome da aplicação.

# Criando a rota pricipal do site.

@app.route('/')


#DEF cria funções no python

def home():
    return render_template('index.html')

@app.route('/games')

def games():
    return render_template('games.html')

@app.route('/consoles')

def consoles():
    return render_template('consoles.html')

#Iniciando o servidor na porta 5000.
#O metodo .run() inicia o servidor.
#Esta verificando se o arquivo gravado em __name__ é o arquivo principal.

if __name__ == '__main__':
    app.run(port=5000, debug=True)

