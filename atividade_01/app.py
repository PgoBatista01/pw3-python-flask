from flask import Flask, render_template, request

app = Flask(__name__, template_folder='views')

# ======================
# ROTAS DO SITE
# ======================

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/personagem')
def personagem():
    return render_template('personagem.html')


@app.route('/sagas')
def sagas():
    return render_template('sagas.html')


@app.route('/noticias')
def noticias():
    return render_template('noticias.html')


# ======================
# FORMULÁRIO (GET + POST)
# ======================

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    personagem = None

    if request.method == 'POST':
        personagem = {
            "nome": request.form['nome'],
            "armadura": request.form['armadura'],
            "descricao": request.form['descricao']
        }

    return render_template('formulario.html', personagem=personagem)


# ======================
# LISTA
# ======================

@app.route('/list')
def lista():
    return render_template('lista.html')


# ======================
# INICIAR SERVIDOR
# ======================

if __name__ == '__main__':
    app.run(port=5000, debug=True)