import texthelper
import os
import consolehelper
import pacman
import yay

api_names = ['api', 'Api', 'API', 'backend', 'BACKEND', 'Backend']
web_names = ['Web', 'web', 'WEB']
mobile_names = ['mobile', 'Mobile', 'MOBILE']


def git_config():
    texthelper.print_header('Primero configuremos git...')
    texthelper.new_line()

    username = input('Ingresa tu usuario de git: ')
    while username == '':
        username = input('Pone algo fiera: ')

    email = input('El mail de Widergy: ')
    while email == '':
        email = input(
            'No tenes mail? Anda a hablar con Pablo, volve y lo escribis: ')
    name = input('Tu nombre completo: ')
    while name == '':
        name = input(
            'No tenes nombre? Quien sos? El innombrable?: ')

    password = input('Y ahora tu contraseña: ')
    while password == '':
        password = input(
            'Ah segurisima tu contraseña eh, dale, ponela posta: ')

    git_credentials_file = open(
        '/home/' + os.environ['USER'] + '/' + '.git-credentials', 'w+')
    git_credentials_file.write(
        'https://' + username + ':' + password + '@github.com')
    git_credentials_file.close()

    email_com = consolehelper.execute(
        ['git', 'config', '--global', 'user.email', email])
    name_com = consolehelper.execute(
        ['git', 'config', '--global', 'user.name', name])

    texthelper.new_line()
    if email_com["code"] == 0 and name_com["code"] == 0:
        texthelper.print_success('Bien! Credenciales de Git configuradas!')
        texthelper.new_line()
    else:
        texthelper.print_error(
            "Upa, hubo un error, no pudimos configurar tus credenciales de Git!")
        texthelper.new_line()
        print('Si podes configurar tus credencales manualmente, apreta enter y segui con la ejecucion, si no, es tu momento para cerrar y volver a abrir el configurador')
        input()


def execute_config(config):
    print_desc(config['name'])
    texthelper.new_line()
    texthelper.print_info('Instalando yay...')
    pacman.install(['evolution'])

def print_desc(name):
    if name in api_names:
        texthelper.print_error(
            'CUIDADO, ESTAS A PUNTO DE ENTRAR EN LA DICTADURA DE IGNACIO CAPUCCIO')
    if name in web_names:
        texthelper.print_success(
            'Buena capo, entraste al mejor team de Widergy!')
    if name in mobile_names:
        texthelper.print_warning('SORRY, APP CRASHED, TRY AGAIN LATER')
