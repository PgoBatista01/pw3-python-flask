from flask import Flask, render_template

app = Flask(__name__, template_folder='Views')

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/personagem')
def personagem():
    return render_template('personagem.html')

@app.route('/sagas')
def sagas():
    return render_template('sagas.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='Views')

@app.route('/formulario', methods=['GET','POST'])
def formulario():
    personagem = None

    if request.method == 'POST':
        personagem = {
            "nome": request.form['nome'],
            "armadura": request.form['armadura'],
            "descricao": request.form['descricao']
        }

    return render_template('formulario.html', personagem=personagem)
#Iniciando o servidor na porta 5000.
#O metodo .run() inicia o servidor.
#Esta verificando se o arquivo gravado em __name__ é o arquivo principal. 

