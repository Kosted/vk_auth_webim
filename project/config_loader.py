import json, os

SECRET_KEY = None
DEBUG = None
SOCIAL_AUTH_VK_OAUTH2_KEY = None
SOCIAL_AUTH_VK_OAUTH2_SECRET = None
HOST = None
NAME = None
USER = None
PORT = None
PASSWORD = None

try:
    file = open("config.json", 'r')
    config = json.load(file)

    SECRET_KEY = config['SECRET_KEY']

    SOCIAL_AUTH_VK_OAUTH2_KEY = config['SOCIAL_AUTH_VK_OAUTH2_KEY']

    SOCIAL_AUTH_VK_OAUTH2_SECRET = config['SOCIAL_AUTH_VK_OAUTH2_SECRET']

    # DEBUG = config['DEBUG']
    DEBUG = True
    print("DEBUG = ", DEBUG)

    HOST = config['HOST']

    NAME = config['NAME']

    USER = config['USER']

    PORT = config['PORT']

    PASSWORD = config['PASSWORD']

    file.close()

except:

    print("File with SECRET_KEY doesn't exist.\nTry to search on env variable...")

    while SECRET_KEY is None:

        try:

            SECRET_KEY = os.environ['SECRET_KEY']

            DATABASE_URL = os.environ['DATABASE_URL']

            SOCIAL_AUTH_VK_OAUTH2_KEY = os.environ['SOCIAL_AUTH_VK_OAUTH2_KEY']

            SOCIAL_AUTH_VK_OAUTH2_SECRET = os.environ['SOCIAL_AUTH_VK_OAUTH2_SECRET']

            DEBUG = os.environ['DEBUG']

            print("DEBUG = ", DEBUG)

            DATABASE_URL = DATABASE_URL.split('://')[1].split(':')

            USER = DATABASE_URL[0]
            PASSWORD = DATABASE_URL[1].split('@')[0]
            HOST = DATABASE_URL[1].split('@')[1]
            NAME = DATABASE_URL[2].split('/')[1]
            PORT = DATABASE_URL[2].split('/')[0]






        except:

            print("Поиск SECRET_KEY и ссылки на бд в системных переменных...")

