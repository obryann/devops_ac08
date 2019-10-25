""" Testando web app """
from com.ac08.calculadora import app_web_start


def test_root_status():
    """ testando status da raíz """
    instancia_app = app_web_start.APP.test_client()
    response = instancia_app.get('/')
    assert response.status_code == 200, 'Deveria existir essa rota'


def test_root_url():
    """ testando URL da raíz """
    instancia_app = app_web_start.APP.test_client()
    response = instancia_app.get('/')
    assert response.data.decode('utf-8') == 'Index Page!', 'Deveria ser Index Page!'
