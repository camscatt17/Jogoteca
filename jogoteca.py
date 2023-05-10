from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    tetris = Jogo('Tetris', 'Puzzle', 'Atari')
    godOfWar = Jogo('God of War', 'Rack n Slash', 'PS2')
    mortalkombat = Jogo('Mortal Kombat', 'Luta', 'PS2')
    lista = [tetris, godOfWar, mortalkombat]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()
