from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Exemplo de "modelo generativo"
def gerar_lista_alimentos(perfil):
    alimentos_base = ["Arroz", "Feijão", "Frango", "Banana", "Brócolis"]
    return [[random.choice(alimentos_base) for _ in range(3)] for _ in range(5)]

@app.route('/', methods=['POST'])
def gerar():
    data = request.get_json()
    perfil = data.get("perfil", "geral")
    lista = gerar_lista_alimentos(perfil)
    return jsonify(lista)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
