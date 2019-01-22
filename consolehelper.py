import subprocess


def execute(command):
    p = subprocess.Popen(command, stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    data = p.communicate()
    data = {"code": p.returncode, "stdout": data[0].decode(),
            "stderr": data[1].rstrip(b'\n').decode()}
    print(data)
    return data
