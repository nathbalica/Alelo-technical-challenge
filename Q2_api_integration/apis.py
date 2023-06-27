from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api1', methods=['POST'])
def api1_endpoint():
    try:
        # Processar a lógica da API 1 aqui
        data = request.get_json()
        # ...

        return jsonify({'message': 'API 1 executada com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api2', methods=['POST'])
def api2_endpoint():
    try:
        # Processar a lógica da API 2 aqui
        data = request.get_json()
        # ...

        return jsonify({'message': 'API 2 executada com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
