import sh
import text_helper


def pacman_install(pkgs):
    text_helper.print_header('[PACMAN] Instalando: ' + " ".join(pkgs))
    try:
        sh.contrib.sudo.pacman('-S', '--noconfirm', " ".join(pkgs))
    except:
        text_helper.print_error('[PACMAN] Hubo un error en la instalacion')
        return False
    text_helper.new_line()
    return True


def pacman_upgrade(pkgs):
    text_helper.print_header('[PACMAN] Actualizando: ' + " ".join(pkgs))
    try:
        sh.contrib.sudo.pacman('-U', '--noconfirm', " ".join(pkgs))
    except:
        text_helper.print_error('[PACMAN] Hubo un error en la actualizacion')
        return False
    text_helper.new_line()
    return True


def pacman_get_installed():
    text_helper.print_header('[PACMAN] Obteniendo paquetes instalados')
    try:
        pkg_list = sh.pacman('-Q')
    except:
        text_helper.print_error(
            '[PACMAN] Hubo un error al obtener la lista de paquetes instalados')
        return False
    text_helper.new_line()
    return pkg_list


def pacman_get_upgradable():
    text_helper.print_header('[PACMAN] Obteniendo paquetes actualizables')
    try:
        pkg_list = sh.pacman('-Qu')
    except:
        text_helper.print_error(
            '[PACMAN] Hubo un error al obtener la lista de paquetes actualizables')
        return False
    text_helper.new_line()
    return pkg_list


def yay_install(pkgs):
    text_helper.print_header('[YAY] Instalando: ' + " ".join(pkgs))
    try:
        sh.yay('-S', '--noconfirm', " ".join(pkgs))
    except sh.exit_code != 0:
        text_helper.print_error(
            '[YAY] Hubo un error en la instalacion de los paquetes')
        return False
    text_helper.new_line()
    return True


def yay_upgrade(pkgs):
    text_helper.print_header('[YAY] Actualizando: ' + " ".join(pkgs))
    try:
        sh.yay('-U', '--noconfirm', " ".join(pkgs))
    except:
        text_helper.print_error('[YAY] Hubo un error en la actualizacion')
        return False
    
    text_helper.new_line()
    return True


def yay_get_installed():
    text_helper.print_header('[YAY] Obteniendo paquetes instalados')
    try:
        pkg_list = sh.yay('-Q')
    except sh.exit_code != 0:
        text_helper.print_error(
            '[YAY] Hubo un error al obtener la lista de paquetes instalados')
        return False
    text_helper.new_line()
    return pkg_list


def yay_get_upgradable():
    text_helper.print_header('[YAY] Obteniendo paquetes actualizables')
    try:
        pkg_list = sh.yay('-Qu')
    except sh.exit_code != 0:
        text_helper.print_error(
            '[YAY] Hubo un error al obtener la lista de paquetes actualizables')
        return False
    text_helper.new_line()
    return pkg_list
