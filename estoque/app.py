from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/estoque', methods=['GET'])
def get_estoque():
    return jsonify({
        "status": "sucesso",
        "mensagem": "Serviço de Estoque respondendo!",
        "itens_disponiveis": 150
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "saudável"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)