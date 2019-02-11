from colorama import init
import text_helper
import utils
import configurator

init()

text_helper.print_header('Bienvenido al configurador automatico de Manjaro!')
text_helper.new_line()

config = utils.build_config()

text_helper.print_header('Selecciona la configuracion:')

utils.print_config_list(config)

selected_config = input()

configurator.execute_config(config[int(selected_config)])
