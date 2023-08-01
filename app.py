from flask import Flask, jsonify, request

app = Flask(__name__)

pacientes = [
    {   'id': 0,
        'cpf': 0,
        'nome': 'vazio'
    }
]

#consultar todos
@app.route('/pacientes',methods=['GET'])
def obter_pacientes():
    return jsonify(pacientes)

@app.route('/pacientes/<int:id>',methods=['GET'])
def obter_pacientes_por_id(id):
    for paciente in pacientes:
        if id == paciente.get('id'):
            return jsonify(paciente)    
    return jsonify({'erro': 'ID Passado não existe'})

@app.route('/pacientes/<int:id>',methods=['PUT'])
def editar_paciente_por_id(id):
    paciente_alterado = request.get_json()
    for indice,paciente in enumerate(pacientes):
        if paciente.get('id') == id:
            pacientes[indice].update(paciente_alterado)
            return jsonify(pacientes[indice])
    return jsonify({'erro': 'ID Passado não existe'})

        
@app.route('/pacientes',methods=['POST'])
def incluir_novo_paciente():
    novo_paciente = request.get_json()
    
    for paciente in pacientes:
        cpf_cadastrado =  paciente.get('cpf') == novo_paciente.get('cpf')
        id_cadastrado = paciente.get('id') == novo_paciente.get('id')
        
        if cpf_cadastrado and id_cadastrado:
            return jsonify({'erro': 'CPF e ID já cadastrados'})
        elif cpf_cadastrado:
            return jsonify({'erro':'CPF já cadastrado'})
        elif id_cadastrado:
            return jsonify({'erro': 'ID já cadastrado'})
       
    pacientes.append(novo_paciente)
    return jsonify(pacientes)
            
           


@app.route('/pacientes/<int:id>',methods=['DELETE'])
def excluir_pacientes(id):
    for indice, paciente in enumerate(pacientes):
            if paciente.get('id') == id:
                pacientes.pop(indice)
                
    return jsonify(pacientes)


app.run(port=5000, host='localhost', debug=True)