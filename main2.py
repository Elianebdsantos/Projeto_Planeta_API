# API É UM LOCAL PARA DISPONIBILIZAR RECURSOS E/OU FUNCIONALIDADES É UMA PONTE
# 1. OBJETIVO: Criar uma API que disponibiliza a consulta, criação, edição e exclusão
# 2. URL base - localhost
# 3. Endpoints-
#     localhost/carros (GET)
#     localhost/carros (PUT)
#     localhost/carros (DELETE)
#     localhost/carros id (GET)

from flask import Flask, jsonify, request, make_response
from bd import Planeta

# Instanciar o módulo Flask na nossa variável app
app = Flask('planeta')

# PRIMEIRO MÉTODO - VISUALIZAR DADOS (GET)
# app.route -> definir que essa função é uma rota para que o Flask execute o método
@app.route('/planeta', methods=['GET'])
def get_planeta():
    return jsonify(Planeta)

# PRIMEIRO MÉTODO PARTE 2 - VISUALIZAR DADOS POR ID (GET / ID)
@app.route('/planeta/<int:id>', methods=['GET'])
def get_planeta_id(id):
    for planeta in Planeta:
        if planeta.get('id') == id:
            return jsonify(planeta)
    

# SEGUNDO MÉTODO - CRIAR NOVOS DADOS (POST)
@app.route('/planeta', methods=['POST'])
def criar_planeta():
    planeta = request.json
    Planeta.append(planeta)
    return make_response(
        jsonify(mensagem='Planeta cadastrado com sucesso', planeta=planeta)
    )

# TERCEIRO MÉTODO - EDITAR DADOS (PUT)
@app.route('/planeta/<int:id>', methods=['PUT'])
def editar_planeta_id(id):
    planeta_alterado = request.get_json()
    for indice, planeta in enumerate(Planeta):
        if planeta.get('id') == id:
            Planeta[indice].update(planeta_alterado)
            return jsonify(Planeta[indice])

# QUARTO MÉTODO - DELETAR DADOS (DELETE)
@app.route('/planeta/<int:id>', methods=['DELETE'])
def excluir_delete(id):
    for indice, planeta in enumerate(Planeta):
        if planeta.get('id') == id:
            del Planeta[indice]
            return jsonify({"mensagem": "Dados do planeta excluídos com sucesso!"})



app.run(port=5000, host='localhost')
