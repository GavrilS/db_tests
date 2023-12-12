import os
# import psycopg2

DEFAULT_ENV_FILE = 'docker_postgresql_general/.env'


def load_env_from_file(env_file=DEFAULT_ENV_FILE):
    with open(env_file, "r") as f:
        content = f.readlines()

    print('content: ', content)
    for env_var in content:
        var = env_var.replace('\n', '')
        elements = var.split('=')
        key = elements[0]
        value = elements[1]
        os.environ[key] = value


def db_connect(db_name, db_user, db_pass):
    pass


if __name__=='__main__':
    load_env_from_file()

    db_pass = os.getenv('POSTGRES_PASSWORD', None)
    db_user = os.getenv('POSTGRES_USER', None)
    db_name = os.getenv('POSTGRES_DB', None)
    print('db_name: ', db_name)
    print('db_user: ', db_user)
    print('db_pass: ', db_pass)
