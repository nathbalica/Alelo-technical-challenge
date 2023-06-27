# Import dos modulos principais
import os
import logging
import requests
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Carregamento das variáveis de ambiente
load_dotenv()

URL_API_1 = os.getenv('TOOL1_URL', 'http://localhost:5001/api1')
URL_API_2 = os.getenv('TOOL2_URL', 'http://localhost:5001/api2')

app = Flask(__name__)

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Classe para lidar com erros de requisição
class RequestError(Exception):
    pass

# Classe para lidar com erros internos do servidor
class InternalServerError(Exception):
    pass

class InvalidRoute(Exception):
    def __init__(self, response):
        self.response = response


@app.route('/integration', methods=['POST'])
def integrate_tools():
    try:
        if request.path != '/integration':
            logger.error(error_msg)
            raise InvalidRoute(jsonify({'error': 'Página não encontrada'}))

             
        # Recebe os dados da requisição
        data = request.get_json()

        # Verifica se as informações necessárias estão presentes
        if 'tool1_data' not in data or 'tool2_data' not in data:
            raise RequestError('Dados ausentes')

        tool1_data = data['tool1_data']
        tool2_data = data['tool2_data']

        # Integração com a Ferramenta 1
        response = requests.post(URL_API_1, json=tool1_data)
        if response.status_code != requests.codes.ok:
            
            error_msg = (
                f"Erro na integração com a Ferramenta 1: {response.status_code} - {response.text}"
                )
            logger.error(error_msg)
            raise RequestError(error_msg)

        # Integração com a Ferramenta 2
        response = requests.post(URL_API_2, json=tool2_data)
        if response.status_code != requests.codes.ok:
            error_msg = f"Erro na integração com a Ferramenta 2: {response.status_code} - {response.text}"
            logger.error(error_msg)
            raise RequestError(error_msg)

        # Retorna a resposta da integração
        return jsonify({'success': 'Integração realizada com sucesso'}), requests.codes.ok

    except RequestError as e:
        error_msg = f"Erro na solicitação: {str(e)}"
        logger.error(error_msg)
        return jsonify({'error': error_msg}), requests.codes.bad_request

    except InvalidRoute as e:
        error_msg = f"Erro rota incorreta: {str(e)}"
        logger.error(error_msg)
        return e.response, 404

    except Exception as e:
        error_msg = f"Erro interno do servidor: {str(e)}"
        logger.error(error_msg)
        return jsonify({'error': error_msg}), requests.codes.server_error
    


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True)
