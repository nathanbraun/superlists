from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--password=Decker1955',
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()


def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database', '--password=Decker1955', '--host={}'.format(host)],
        cwd=THIS_FOLDER
    )
