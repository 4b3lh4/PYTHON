from flask import Flask, render_template
from calculadora import calcular

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculadora.html', etapas ='', resultados = '')  # Aqui está rodando o método GET que é pegando a rota


@app.route('/calcular', methods=['POST']) #aqui o /calcular não endereça uma nova página, ele abre o formulário.
def calcular_route():
    return calcular()

if __name__ == "__main__":
    app.run(debug=True)
