from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc <= 34.9:
        classificacao = "Obesidade grau 1"
    elif 35 <= imc <= 39.9:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

    return imc, classificacao

@app.route('/calcular_imc', methods=['POST'])
def calcular():
    data = request.get_json()
    peso = data['peso']
    altura = data['altura']

    imc, classificacao = calcular_imc(peso, altura)

    return jsonify({"imc": imc, "classificacao": classificacao})

if __name__ == '__main__':
    app.run(debug=True)
