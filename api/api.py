# app.py
from flask import Flask, request, jsonify
import logging

# Configurar o logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Lista global para armazenar os dados recebidos
dados_recebidos = []

# Rota POST /receptor que recebe dados no corpo da requisição
@app.route('/receptor', methods=['POST'])
def receptor():
    # Captura o JSON enviado no corpo da requisição
    data = request.get_json()
    
    logging.debug(f"Dados recebidos na rota /receptor: {data}")

    # Acessar os campos enviados
    id_credito = data.get('id_credito')
    id_produto = data.get('id_produto')
    id_cliente = data.get('id_cliente')
    eventos = data.get('eventos', [])
    
    # Adiciona os dados recebidos à lista global
    dados_recebidos.append(data)

    # Retornar os dados como JSON
    return jsonify({
        "id_credito": id_credito,
        "id_produto": id_produto,
        "id_cliente": id_cliente,
        "eventos": eventos
    }), 200

# Rota GET /dados que retorna os dados recebidos
@app.route('/dados', methods=['GET'])
def get_dados():
    logging.debug("Rota /dados chamada.")
    if not dados_recebidos:
        logging.warning("Nenhum dado recebido até o momento.")
        return jsonify({"message": "Nenhum dado disponível."}), 404
    return jsonify(dados_recebidos), 200

# Rodar a aplicação localmente
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
