from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='views')

def init_app(app):

    listaCuriosidades = [
        {
            'titulo': 'Origem das Armaduras',
            'conteudo': 'As armaduras foram criadas na antiguidade para proteger os cavaleiros de Atena.'
        }
    ]

    listaCavaleiros = [
        {
            'nome': 'Seiya',
            'armadura': 'Pégaso',
            'signo': 'Sagitário',
            'afiliacao': 'Bronze',
            'status': 'Vivo',
            'tecnicas': 'Meteoro de Pégaso',
            'poder': 'Cosmos elevado',
            'personalidade': 'Determinado'
        }
    ]
    
    listaNoticias = [
    {
        "id": 1,
        "titulo": "Saga do Céu confirmada",
        "descricao": "Novo arco de Cavaleiros do Zodíaco chega em maio.",
        "imagem": "sagadoceu.png",
        "link": "https://ovicio.com.br/os-cavaleiros-do-zodiaco-saga-do-ceu-tem-lancamento-confirmado-para-maio/"
    },
    {
        "id": 2,
        "titulo": "Novo anime anunciado",
        "descricao": "Nova adaptação confirmada oficialmente.",
        "imagem": "anime.png",
        "link": "https://olhardigital.com.br/2026/03/06/curiosidades/saint-seiya-prepara-nova-animacao-que-pode-finalmente-adaptar-a-saga-de-zeus-apos-decadas-de-espera/"
    },
    {
        "id": 3,
        "titulo": "Mangá continua",
        "descricao": "Histórias inéditas seguem no Japão.",
        "imagem": "manga.png",
        "link": "https://www.cavzodiaco.com.br/noticia/23/02/2026/novo-manga-masami-kurumada-mostra-primeiros-esbocos-da-saga-do-ceu-dos-cavaleiros-do-zodiaco"
    }
]
    
    @app.route('/')
    def home():
        return render_template('index.html')

    
    @app.route('/curiosidades')
    def curiosidades():
        return render_template('curiosidades.html', listaCuriosidades=listaCuriosidades)

   
    @app.route('/cavaleiros')
    def cavaleiros():
        return render_template('cavaleiros.html', listaCavaleiros=listaCavaleiros)

    
    @app.route('/cadastro_curiosidades', methods=['GET', 'POST'])
    def cadastro_curiosidades():

        if request.method == 'POST':
            listaCuriosidades.append({
                'titulo': request.form.get('titulo'),
                'conteudo': request.form.get('conteudo')
            })
            return redirect(url_for('curiosidades'))

        return render_template('cadastro_curiosidades.html', listaCuriosidades=listaCuriosidades)

    @app.route('/cadastro_cavaleiros', methods=['GET', 'POST'])
    def cadastro_cavaleiros():

        if request.method == 'POST':
            listaCavaleiros.append({
                'nome': request.form.get('nome'),
                'armadura': request.form.get('armadura'),
                'signo': request.form.get('signo'),
                'afiliacao': request.form.get('afiliacao'),
                'status': request.form.get('status'),
                'tecnicas': request.form.get('tecnicas'),
                'poder': request.form.get('poder'),
                'personalidade': request.form.get('personalidade')
            })
            return redirect(url_for('cavaleiros'))

        return render_template('cadastro_cavaleiros.html', listaCavaleiros=listaCavaleiros)

    
    @app.route('/noticias')
    def noticias():
        
        return render_template('noticias.html', listaNoticias=listaNoticias)


init_app(app)

if __name__ == '__main__':
    app.run(debug=True)