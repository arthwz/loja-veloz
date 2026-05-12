# pedidos/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    return jsonify({
        "status": "sucesso",
        "mensagem": "Serviço de Pedidos respondendo!",
        "dados": [{"id": 1, "item": "Notebook"}, {"id": 2, "item": "Mouse"}]
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "saudável"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)