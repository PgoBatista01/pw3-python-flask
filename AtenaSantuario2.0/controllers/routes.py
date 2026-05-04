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
        }
    ]
    listaFilmes = [
        {
            "titulo": "O Começo",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-saint-seiya-o-comeco-t319748/"
        },
        {
            "titulo": "A Lenda do Santuário",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-a-lenda-do-santuario-t30816/"
        },
        {
            "titulo": "Teatro Piriri (Apresentação)",
            "link": "https://www.youtube.com/watch?v=w_CFFlAZXtw&t=815s"
        },
        {
            "titulo": "O Santo Guerreiro",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-1-o-santo-guerreiro-t1363/assista-agora/"
        },
        {
            "titulo": "A Grande Batalha dos Deuses",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-2-a-grande-batalha-dos-deuses-t888/"
        },
        {
            "titulo": "A Lenda dos Defensores de Atena",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-3-a-lenda-dos-defensores-de-atena-t1361/"
        },
        {
            "titulo": "Os Guerreiros do Armagedon",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-4-os-guerreiros-do-armagedon-t8704/"
        },
        {
            "titulo": "Episódio Zero",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-episodio-zero-t121496/"
        },
        {
            "titulo": "O Mito dos Cavaleiros Renegados",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-o-mito-dos-cavaleiros-renegados-t40650/"
        },
        {
            "titulo": "Prólogo do Céu",
            "link": "https://filmow.com/os-cavaleiros-do-zodiaco-o-filme-prologo-do-ceu-t1362/"
        }
    ]
    # =========================
    # 🛡️ API JSON
    # =========================
    cavaleirosjson = [
        {
            "id": 1,
            "nome": "Seiya",
            "armadura": "Pégaso",
            "signo": "Sagitário",
            "imagem": "/static/imgs/seiya.png"
        }
    ]

    # =========================
    # 📚 MANGÁS (DRIVE)
    # =========================
    mangas_links = {
        "classico": "https://drive.google.com/drive/folders/1PGbkWHPkEt6U6SxmCkw8-_tmvFmJBcq5",
        "saintia": "https://drive.google.com/drive/folders/1B6ystPNV1U2xV56YrrRxh7hxwTCaefr6",
        "rerise": "https://drive.google.com/drive/folders/1HbXzL7reslzYwHK8WOOZ0BwM5U99FR7R"
    }

    # =========================
    # 🎬 ANIMES (ASSISTIR)
    # =========================
    animes_links = {
        "omega": "https://animesonlineclub.net/anime/saint-seiya-omega-os-cavaleiros-do-zodiaco-omega",
        "lost_canvas": "https://animesonlineclub.net/anime/saint-seiya-the-lost-canvas",
        "soul_gold": "https://animesonlineclub.net/anime/saint-seiya-soul-of-gold",
        "saintia": "https://animesonlineclub.net/anime/saint-seiya-saintia-shou",
        "classico": "https://animesonlineclub.net/anime/os-cavaleiros-do-zodiaco",
        "reboot": "https://animesonlineclub.net/anime/saint-seiya-os-cavaleiros-do-zodiaco"
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
    # 📚 MANGÁS
    # =========================
    @app.route('/mangas')
    def mangas():
        return render_template('mangas.html', mangas=mangas_links)

    # =========================
    # 🎬 ASSISTIR ANIMES
    # =========================
    @app.route('/assistir')
    def assistir():
        return render_template('assistir.html', animes=animes_links)
    
# =========================
# 🎬 FILMES CDZ
# =========================
    @app.route('/filmes')
    def filmes():
        return render_template('filmes.html', listaFilmes=listaFilmes)

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