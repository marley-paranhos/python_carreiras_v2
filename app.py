from flask import Flask, render_template, jsonify

app = Flask(__name__)

vagas = [
    {
        'id': 1,
        'titulo': 'Desenvolvedor Backend',
        'localidade': 'BH, Brasil',
        'salario': 'R$ 5.000'
    },
    
    {
        'id': 2,
        'titulo': 'Desenvolvedor Frontend',
        'localidade': 'SP, Brasil',
        'salario': 'R$ 3.000'
    },

    {
        'id': 3,
        'titulo': 'Engenheiro AWS',
        'localidade': 'BH, Brasil',
        'salario': 'R$ 10.000'
    },

    {
        'id': 4,
        'titulo': 'Cientista de Dados',
        'localidade': 'SC, Brasil',
        'salario': 'R$ 6.000'
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html', vagas=vagas)


@app.route('/vagas')
def lista_vagas():
    return jsonify(vagas)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
