from shlex import quote
import consolehelper
import texthelper


def install(packages):
    filtered_pkgs = filer_packages(packages)

    if len(filtered_pkgs['installed']) > 0:
        texthelper.print_info(
            'Los siguientes paquetes se encuentran instalados y actualizados, se omitiran:')
        print(','.join(filtered_pkgs['installed']))

    if len(filtered_pkgs['upgradable']) > 0:
        texthelper.print_info(
            'Los siguientes paquetes se encuentran instalados y pueden ser actualizados:')
        print(','.join(filtered_pkgs['upgradable']))
        texthelper.new_line()
        should_upgrade = input(
            'Ingrese Y para actualizar o N para omitir: ')

        while should_upgrade != 'Y' and should_upgrade != 'N':
            should_upgrade = input(
                'Ingrese Y para actualizar o N para omitir: ')

        if should_upgrade == 'Y':
            upgrade = pacman('-S', filtered_pkgs['upgradable'])
            if upgrade["code"] != 0:
                raise Exception(
                    "Fallo al actualizar: {0}".format(upgrade["stderr"]))
            else:
                texthelper.print_success(
                    'Se actualizo satisfactoriamente: ' + ', '.join(filtered_pkgs['upgradable']))

    if len(filtered_pkgs['to_install']) > 0:
        install = pacman("-S", filtered_pkgs['to_install'])
        if install["code"] != 0:
            raise Exception(
                "Fallo la instalacion: {0}".format(install["stderr"]))
        else:
            texthelper.print_success(
                'Se instalo satisfactoriamente: ' + ', '.join(filtered_pkgs['to_install']))


def filer_packages(packages):
    installed_pkg = get_installed()
    upgradable_list = []
    not_installed_list = []
    installed_list = []
    if isinstance(packages, list):
        for package in packages:
            if not package in installed_pkg:
                not_installed_list += [package]
            elif installed_pkg[package]['upgradable']:
                upgradable_list += [package]
            else:
                installed_list += [package]
    else:
        if not packages in installed_pkg:
            not_installed_list += [packages]
        elif installed_pkg[packages]['upgradable']:
            upgradable_list += [packages]
        else:
            installed_list += [packages]
    return {'upgradable': upgradable_list, 'to_install': not_installed_list, 'installed': installed_list}


def get_installed():
    interim = {}
    s = pacman("-Q")
    if s["code"] != 0:
        raise Exception(
            "Failed to get installed list: {0}".format(s["stderr"])
        )
    for x in s["stdout"].split('\n'):
        if not x.split():
            continue
        x = x.split(' ')
        interim[x[0]] = {
            "id": x[0], "version": x[1], "upgradable": False,
            "installed": True
        }
    s = pacman("-Qu")
    if s["code"] != 0 and s["stderr"]:
        raise Exception(
            "Failed to get upgradable list: {0}".format(s["stderr"])
        )
    for x in s["stdout"].split('\n'):
        if not x.split():
            continue
        x = x.split(' -> ')
        name = x[0].split(' ')[0]
        if name in interim:
            r = interim[name]
            r["upgradable"] = x[1]
            interim[name] = r
    return interim


def pacman(flags, pkgs=[]):
    cmd = ["sudo", "pacman", "--noconfirm", flags]
    if pkgs:
        if type(pkgs) == list:
            cmd += [quote(s) for s in pkgs]
        else:
            cmd += [pkgs]
    return consolehelper.execute(cmd)
