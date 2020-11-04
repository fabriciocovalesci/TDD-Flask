from app import create_app
from flask import Flask, template_rendered

def test_create_app():
    assert isinstance(create_app(), Flask)


def test_login_deve_retornar_sucesso():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        response = client.get('/login')

    assert response.status_code == 200


def test_login_html():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        request = client.get('/login')

    assert '<html>' in request.data.decode()

def test_endpoint_de_login_retorna_template_login():
    app = create_app()
    app.config['TESTING'] = True

    templates = []

    def gravador_templates(remetente, template, context, **extra):
        templates.append(template)

    template_rendered.connect(gravador_templates, app)

    with app.test_client() as client:
        client.get('/login')

    assert templates[0].name == 'login.html'

    template_rendered.disconnect(gravador_templates, app)
