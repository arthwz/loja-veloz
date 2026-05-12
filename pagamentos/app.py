from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pagamentos', methods=['GET'])
def processar_pagamento():
    return jsonify({
        "status": "sucesso",
        "mensagem": "Serviço de Pagamentos respondendo!",
        "gateway_externo": "conectado"
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "saudável"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)