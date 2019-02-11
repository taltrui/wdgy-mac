from sh.contrib import git
import text_helper
import utils
import pathlib


def git_clone(repo):
    text_helper.print_info('[GIT] Clonando: ' + utils.take_repo_name(repo))
    try:
        git('clone', repo, './Workspace/' +
            utils.take_repo_name(repo), _cwd=pathlib.Path.home())
    except:
        text_helper.print_error(
            '[GIT] Hubo un error al intentar clonar el repositorio')
        return False
    text_helper.print_success(
        '[GIT] Se clono satisfactoriamente: ' + utils.take_repo_name(repo))


def git_set_credentials(password, username):
    text_helper.print_info('[GIT] Seteando credenciales')
    try:
        git('config', '--global', 'credential.https://github.com.username', username)
        git('config', '--global', 'credential.https://github.com.password', password)
    except:
        text_helper.print_error(
            '[GIT] Hubo un error seteando las credenciales')
        return False
    text_helper.print_success(
        '[GIT] Credenciales seteadas satisfactoriamente')


def git_set_email_and_name(email, name):
    text_helper.print_info('[GIT] Seteando email y usuario')
    try:
        git('config', '--global', 'user.email', email)
        git('config', '--global', 'user.name', name)
    except:
        text_helper.print_error(
            '[GIT] Hubo un error seteando el mail y usuario')
        return False
    text_helper.print_success(
        '[GIT] Mail y usario seteados satisfactoriamente')
