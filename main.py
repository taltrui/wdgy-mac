from colorama import init
import texthelper
import utils
import configurator

init()

texthelper.print_header('Bienvenido al configurador automatico de Manjaro!')
texthelper.new_line()

config = utils.build_config()

texthelper.print_header('Selecciona la configuracion:')

utils.print_config_list(config)

selected_config = input()

configurator.execute_config(config[int(selected_config)])
