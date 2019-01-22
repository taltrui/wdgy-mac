from colorama import init
import subprocess
import texthelper

init()

texthelper.new_line()
texthelper.print_header('Bienvenido al configurador automatico de Manjaro!')
texthelper.new_line()

texthelper.print_header('Primero selecciona el equipo al que perteneces')
print('1. Web' + '\n' + '2. Mobile' + '\n' + '3. API' + '\n' + '4. QA')
