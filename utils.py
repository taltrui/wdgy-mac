
import os
import json
import text_helper
import pkg_manager_helper

CONFIG_PATH = './configs/'

yes = {'yes', 'y', 'ye', ''}
no = {'no', 'n'}


def build_config():
    text_helper.print_info('Cargando configuraciones')
    text_helper.new_line()

    config_dict = dict()

    for index, filename in enumerate(os.listdir(CONFIG_PATH), start=1):
        print('Cargando ' + filename + '...')
        text_helper.separator()

        file = open(CONFIG_PATH + filename)
        data = json.load(file)

        if 'name' not in data:
            text_helper.print_error(
                'El archivo ' + filename + ' no tiene una key "name", no fue agregado como opcion')
            continue

        if 'apps' not in data and 'commands' not in data:
            text_helper.print_error(
                'El archivo ' + filename + ' no tiene apps, no fue agregado como opcion')
            continue

        config_dict[index] = {}
        config_dict[index]['name'] = data['name']

        if 'apps' in data:
            config_dict[index]['apps'] = data['apps']
        else:
            text_helper.print_warning(
                'El archivo ' + filename + ' no tiene ninguna app')

        if 'clone' in data:
            config_dict[index]['clone'] = data['clone']
        else:
            text_helper.print_warning(
                'El archivo ' + filename + ' no tiene ningun repositorio a clonar')

        if 'zsh' in data:
            config_dict[index]['zsh'] = data['zsh']
            text_helper.print_info('Se configurarab Zsh y Oh-my-Zsh')
        else:
            text_helper.print_info('Zsh y Oh-my-Zsh no se configuraran')

        text_helper.print_success(
            'Archivo ' + filename + ' cargado satisfactoriamente')
        text_helper.new_line()

    return config_dict


def print_config_list(config_list):
    for key, value in config_list.items():
        print(str(key) + '. ' + value['name'])


def take_repo_name(repo):
    return repo.split('/')[-1].split('.')[0]

def yes_no_query(prompt):

    choice = input(prompt + ' [Yes/No] ').lower()
    
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        text_helper.print_error('Responde con si o no...')

def filter_packages(packages):
    installed = pkg_manager_helper.yay_get_installed()
    upgradable = pkg_manager_helper.yay_get_upgradable()

    filtered_packages_dict = dict()
    filtered_packages_dict['upgradable'] = []
    filtered_packages_dict['installed'] = []
    filtered_packages_dict['to_install'] = []

    for package in packages:
        if package in upgradable:
            filtered_packages_dict['upgradable'].append(package)
            continue
        if package in installed:
            filtered_packages_dict['installed'].append(package)
            continue
        filtered_packages_dict['to_install'].append(package)
    
    return filtered_packages_dict