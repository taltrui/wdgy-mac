
import os
import json
import texthelper

CONFIG_PATH = './configs/'


def build_config():
    texthelper.print_info('Cargando configuraciones')
    texthelper.new_line()

    config_dict = dict()

    for index, filename in enumerate(os.listdir(CONFIG_PATH), start=1):
        print('Cargando ' + filename + '...')
        texthelper.separator()

        file = open(CONFIG_PATH + filename)
        data = json.load(file)

        if 'name' not in data:
            texthelper.print_error(
                'El archivo ' + filename + ' no tiene una key "name", no fue agregado como opcion')
            continue

        if 'apps' not in data and 'commands' not in data:
            texthelper.print_error(
                'El archivo ' + filename + ' no tiene apps ni comandos, no fue agregado como opcion')
            continue

        config_dict[index] = {}
        config_dict[index]['name'] = data['name']

        if 'apps' in data:
            config_dict[index]['apps'] = data['apps']
        else:
            texthelper.print_warning(
                'El archivo ' + filename + ' no tiene ninguna app')

        if 'commands' in data:
            config_dict[index]['commands'] = data['commands']
        else:
            texthelper.print_warning(
                'El archivo ' + filename + ' no tiene ningun comando')

        texthelper.print_success(
            'Archivo ' + filename + ' cargado satisfactoriamente')
        texthelper.new_line()

    return config_dict


def print_config_list(config_list):
    for key, value in config_list.items():
        print(str(key) + '. ' + value['name'])
