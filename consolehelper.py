import subprocess
from halo import Halo


def execute(command, loading_message):
    p = subprocess.Popen(command, stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    spinner = Halo(text=loading_message, spinner='dots')
    spinner.start()
    while p.poll() is None:
        pass
    data = p.communicate()
    data = {"code": p.returncode, "stdout": data[0].decode(),
            "stderr": data[1].rstrip(b'\n').decode()}
    if data["code"] != 0:
      spinner.fail(loading_message + '. Operación fallida.')
    else:
      spinner.succeed(loading_message + '. Operación exitosa.')
    return data
