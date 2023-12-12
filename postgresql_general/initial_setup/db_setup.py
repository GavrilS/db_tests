import os
import psycopg2

DEFAULT_ENV_FILE = 'docker_postgresql_general/.env'
DEFAULT_DB_HOST = 'localhost'
DEFAULT_DB_PORT = '5433'


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
    try:
        conn = psycopg2.connect(
            host=DEFAULT_DB_HOST,
            database=db_name,
            user=db_user,
            password=db_pass,
            port=DEFAULT_DB_PORT
        )
        print('Connection set up successfully!!!')
        return conn
    except Exception as e:
        print('There was an error trying to connect to db: ', str(e))
        exit()


def execute_db_setup(conn):
    try:
        cur = conn.cursor()
        cur.execute(open("test_db_schema.sql", "r").read())
        cur.close()
        conn.commit()
        print('Operations executed and commited!')
    except Exception as e:
        print('There was an error trying to execute to set up .sql commands: ', str(e))
    finally:
        close_db_connection(conn)


def close_db_connection(conn):
    conn.close()
    print('Connection closed!')


if __name__=='__main__':
    load_env_from_file()

    db_pass = os.getenv('POSTGRES_PASSWORD', None)
    db_user = os.getenv('POSTGRES_USER', None)
    db_name = os.getenv('POSTGRES_DB', None)
    print('db_name: ', db_name)
    print('db_user: ', db_user)
    print('db_pass: ', db_pass)

    conn = db_connect(db_name, db_user, db_pass)
    execute_db_setup(conn)
