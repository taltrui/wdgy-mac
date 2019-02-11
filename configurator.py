import text_helper
import os
import pkg_manager_helper
import git_helper
import utils

api_names = ['api', 'Api', 'API', 'backend', 'BACKEND', 'Backend']
web_names = ['Web', 'web', 'WEB']
mobile_names = ['mobile', 'Mobile', 'MOBILE']


def execute_config(config):
    if(utils.yes_no_query('Configuramos git?')):
        if _git_config():
            text_helper.print_success('Listo! Git configurado')
        else:
            text_helper.print_error('Hubo un error al configurar git')
            if not utils.yes_no_query('Seguimos?'):
                exit()

    if not pkg_manager_helper.pacman_install(['yay']):
        text_helper.print_error(
            'Yay no pudo ser instalado... Saliendo del configurador...')
        exit()

    text_helper.print_header('Chequeando paquetes...')

    filtered_packages = utils.filter_packages(config['apps'])

    if filtered_packages['upgradable']:
       text_helper.print_header('Paquetes actualizables: ' + " ".join(filtered_packages['upgradable']))
       if utils.yes_no_query('Actualizar paquetes?'):
           pkg_manager_helper.yay_upgrade(filtered_packages['upgradable'])
    else:
        text_helper.print_info('No hay paquetes con actualizaciones disponibles')

    if filtered_packages['installed']:
        text_helper.print_info('Los siguientes paquetes estan instalados y actualizados, se omitiran: ' + " ".join(filtered_packages['installed']))

    if  filtered_packages['to_install']:
        if not pkg_manager_helper.yay_install(filtered_packages['to_install']):
            exit()
    else:
        text_helper.print_info('No hay paquetes para instalar')

    
    

def _git_config():
    text_helper.print_header('Vamos a configurar git...')
    text_helper.new_line()

    email = input('Ingresa el mail de Widergy: ')
    while email == '':
        email = input(
            'No tenes mail? Anda a hablar con el Commander, volve y lo escribis: ')

    name = input('Tu nombre completo: ')
    while name == '':
        name = input(
            'No tenes nombre? Quien sos? El innombrable?: ')

    username = input('Tu usuario de git: ')
    while username == '':
        username = input('Pone algo fiera: ')

    password = input('Y ahora tu contraseña: ')
    while password == '':
        password = input(
            'Ah segurisima tu contraseña eh, dale, ponela posta: ')

    git_credentials_file = open(
        '/home/' + os.environ['USER'] + '/' + '.git-credentials', 'w+')
    git_credentials_file.write(
        'https://' + username + ':' + password + '@github.com')
    git_credentials_file.close()

    if git_helper.git_set_credentials(password, username) and git_helper.git_set_email_and_name(email, name):
        return True
    else:
        return False
    


def print_desc(name):
    if name in api_names:
        return text_helper.print_error(
            'CUIDADO, ESTAS A PUNTO DE ENTRAR EN LA DICTADURA DE IGNACIO CAPUCCIO')
    if name in web_names:
        return text_helper.print_success(
            'Buena capo, entraste al mejor team de Widergy!')
    if name in mobile_names:
        return text_helper.print_warning('SORRY, APP CRASHED, TRY AGAIN LATER')
