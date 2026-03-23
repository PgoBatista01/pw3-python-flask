
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='views')


def init_app(app):

    listaConsoles = ['Playstation 5', 'Xbox One','Super Nintendo', 'Atari 2600', 'Nintendo 3DS']
    listaGames =[{'titulo': 'CS-GO', 'ano':2012,'categoria': 'FPS-ONLINE', 'plataforma': 'PC(WINDOWS)'}]

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        # Criar informação para a rota de games
        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"
        jogadores = ['Marcos', 'Richard', "Miguel", 'Renato', 'Pedro']
        return render_template('games.html', titulo=titulo, ano=ano, categoria=categoria, jogadores=jogadores)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        # criando um objeto
        console = {"Nome:": "Playstation 2 ",
                   "Fabricante: ": "Sony", "Ano: ": 2000}
        #Recebendo o valor do formulário
        if request.method == 'POST':
            if request.form.get('novoConsole'):
                listaConsoles.append(request.form.get('novoConsole'))
        
        return render_template('consoles.html', console=console, listaConsoles=listaConsoles)
     #Recebendo as informações de cadastro de jogos
     
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
       
       #Recebendo os dados do formulario e devolvendo para a pagina
       #Verificando se a requisição é do tipo POST
      if request.method == 'POST':
         #Aqui ele ira gravar os dados na lista de jogos 
        listaGames.append({'titulo' : request.form.get('titulo'), 'ano' : request.form.get('ano'), 'categoria' : request.form.get('categoria'),  'plataforma' : request.form.get('plataforma')})
      
        return render_template('cadgames.html', listaGames=listaGames)