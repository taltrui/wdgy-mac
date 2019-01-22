import texthelper
import os

api_names = ['api', 'Api', 'API', 'backend', 'BACKEND', 'Backend']
web_names = ['Web', 'web', 'WEB']
mobile_names = ['mobile', 'Mobile', 'MOBILE']


def git_config():
    texthelper.print_header('Primero configuremos git...')
    pc_user = os.environ['USER']
    texthelper.new_line()
    username = input('Ingresa tu usuario de git:')
    password = input('Ahora tu contraseña:')
    git_credentials_file = open('/home/' + os.environ['USER'] + '/' + '.git-credentials', 'w+')


def execute_config(config):
    print_desc(config['name'])


def print_desc(name):
    if name in api_names:
        texthelper.print_error(
            'CUIDADO, ESTAS A PUNTO DE ENTRAR EN LA DICTADURA DE IGNACIO CAPUCCIO')
    if name in web_names:
        texthelper.print_success(
            'Buena capo, entraste al mejor team de Widergy!')
    if name in mobile_names:
        texthelper.print_warning('Beep boop... team not found... beep boop...')
