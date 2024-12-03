from flask import Flask, jsonify

app = Flask(__name__)

# Variável global para armazenar a instância do DataHandler
data_handler = None

@app.route('/latest', methods=['GET'])
def get_latest():
    """Retorna o último dado recebido."""
    if data_handler is not None:
        latest_data = data_handler.get_data()
        if latest_data is not None:
            return jsonify({"latest": latest_data}), 200
    return jsonify({"error": "No data available"}), 404

@app.route('/history', methods=['GET'])
def get_history():
    """Retorna o histórico completo de dados."""
    if data_handler is not None:
        try:
            with open(data_handler.file_name, 'r') as file:
                history = [line.strip() for line in file.readlines()]
            return jsonify({"history": history}), 200
        except FileNotFoundError:
            return jsonify({"error": "No data available"}), 404
    return jsonify({"error": "Data handler not initialized"}), 500

def start_api(handler_instance):
    """Inicializa a API com uma instância de DataHandler."""
    global data_handler
    data_handler = handler_instance
    app.run(host="0.0.0.0", port=5000)
