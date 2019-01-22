import consolehelper
from shlex import quote


def install(packages):
    s = yay("-S", packages)
    if s["code"] != 0:
        raise Exception("Failed to install: {0}".format(s["stderr"]))


def get_installed():
    interim = {}
    s = yay("-Q")
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
    s = yay("-Qu")
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
    results = []
    for x in interim:
        results.append(interim[x])
    return results


def yay(flags, pkgs=[]):
    cmd = ["yay", "--noconfirm", flags]
    if pkgs:
        if type(pkgs) == list:
            cmd += [quote(s) for s in pkgs]
        else:
            cmd += [pkgs]
    return consolehelper.execute(cmd)
