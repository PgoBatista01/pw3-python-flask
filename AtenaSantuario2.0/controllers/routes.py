from flask import render_template, request, redirect, url_for

def init_app(app):

    # =========================
    # 📚 DADOS
    # =========================

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

    # =========================
    # 🛡️ API CAVALEIROS (JSON LOCAL)
    # =========================
    cavaleirosjson = [
        {
            "id": 1,
            "nome": "Seiya",
            "armadura": "Pégaso",
            "signo": "Sagitário",
            "imagem": "/static/imgs/seiya.png"
        },
        {
            "id": 2,
            "nome": "Shiryu",
            "armadura": "Dragão",
            "signo": "Libra",
            "imagem": "/static/imgs/shiryu.png"
        }
    ]

    # =========================
    # 📚 LINKS DOS MANGÁS (DRIVE)
    # =========================
    mangas_links = {
        "classico": "https://drive.google.com/drive/folders/1PGbkWHPkEt6U6SxmCkw8-_tmvFmJBcq5",
        "saintia": "https://drive.google.com/drive/folders/1B6ystPNV1U2xV56YrrRxh7hxwTCaefr6",
        "rerise": "https://drive.google.com/drive/folders/1HbXzL7reslzYwHK8WOOZ0BwM5U99FR7R",
        "omega": "https://drive.google.com/drive/folders/1YTBkoYv4YKGl77A5xsTsF3uYpBUp6W-I",
        "novels": "https://drive.google.com/drive/folders/1yWo93gq0bN-H6ryxbC0VfLQLmMnjeEjR",
        "next": "https://drive.google.com/drive/folders/1byOCHAatBZ5LQzldrLgvXMwrKQ4d6Am6",
        "gaiden": "https://drive.google.com/drive/folders/1iy8C4pxGbVb6rcZDlrlv_jbd-mvnxiE9",
        "lost": "https://drive.google.com/drive/folders/1G0OtRCDqk98Sbuh7Y_cHo02IwrUfsv7f",
        "epg_assassin": "https://drive.google.com/drive/folders/1AnCbfAPs4nRo_qOH8OXgXR--jQuX9o3O",
        "epg": "https://drive.google.com/drive/folders/1WLp9TjmSilUWyfZOTVcZ9MWhDDJy3Ryc",
        "ep0": "https://drive.google.com/drive/folders/1iU3Q_LMJd8JBXK5wG4RMPzfLjWoQvQBj",
        "enciclopedias": "https://drive.google.com/drive/folders/1OPnLonSk_-UGvDxowJ4nB3duVPcHSWDb",
        "dark": "https://drive.google.com/drive/folders/1-riR33Tw_KdPKNVNsf4D1PQKBPqHYs_0",
        "origin": "https://drive.google.com/drive/folders/16gT0DRZFrW67k9gIqFXXbgaqRbzfvIuE",
        "destiny": "https://drive.google.com/drive/folders/1Pms-ySV2RK--uBdWNQCl_D3bSZH0vyhF"
    }

    # =========================
    # 🏠 HOME
    # =========================
    @app.route('/')
    def home():
        return render_template('index.html')

    # =========================
    # 📖 CURIOSIDADES
    # =========================
    @app.route('/curiosidades')
    def curiosidades():
        return render_template('curiosidades.html', listaCuriosidades=listaCuriosidades)

    @app.route('/cadastro_curiosidades', methods=['GET', 'POST'])
    def cadastro_curiosidades():
        if request.method == 'POST':
            listaCuriosidades.append({
                'titulo': request.form.get('titulo'),
                'conteudo': request.form.get('conteudo')
            })
            return redirect(url_for('curiosidades'))

        return render_template('cadastro_curiosidades.html')

    # =========================
    # 🛡️ CAVALEIROS
    # =========================
    @app.route('/cavaleiros')
    def cavaleiros():
        return render_template('cavaleiros.html', listaCavaleiros=listaCavaleiros)

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

        return render_template('cadastro_cavaleiros.html')

    # =========================
    # 📰 NOTÍCIAS
    # =========================
    @app.route('/noticias')
    def noticias():
        return render_template('noticias.html', listaNoticias=listaNoticias)

    # =========================
    # 📚 MANGÁS (TODOS LINKS)
    # =========================
    @app.route('/mangas')
    def mangas():
        return render_template('mangas.html', mangas=mangas_links)

    # =========================
    # 🔥 API CAVALEIROS
    # =========================
    @app.route('/apicavaleiros')
    @app.route('/apicavaleiros/<int:id>')
    def apicavaleiros(id=None):

        if id:
            cavaleiro = next((c for c in cavaleirosjson if c["id"] == id), None)

            if cavaleiro:
                return render_template('cavaleiro_info.html', c=cavaleiro)
            else:
                return "Cavaleiro não encontrado"

        return render_template('apicavaleiros.html', cavaleirosjson=cavaleirosjson)