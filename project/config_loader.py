import json, os

SECRET_KEY = None
DATABASE_URL = None
DEBUG = False

try:
    file = open("config.json", 'r')
    config = json.load(file)

    SECRET_KEY = config['SECRET_KEY']
    print("TOKEN найден в config файле")

    DATABASE_URL = config['DATABASE_URL']
    print("DATABASE_URL найден в config файле")

    SOCIAL_AUTH_VK_OAUTH2_KEY = config['SOCIAL_AUTH_VK_OAUTH2_KEY']
    print("SOCIAL_AUTH_VK_OAUTH2_KEY найден в config файле")

    SOCIAL_AUTH_VK_OAUTH2_SECRET = config['SOCIAL_AUTH_VK_OAUTH2_SECRET']
    print("SOCIAL_AUTH_VK_OAUTH2_SECRET найден в config файле")

    DEBUG = True
    print("Запущен DEBUG мод")

    file.close()

except:

    print("File with SECRET_KEY doesn't exist.\nTry to search on env variable...")

    while SECRET_KEY is None:

        try:

            SECRET_KEY = os.environ['SECRET_KEY']
            print("SECRET_KEY обнаружен в системных переменных")

            DATABASE_URL = os.environ['DATABASE_URL']
            print("DATABASE_URL обанружен в системных переменных")

            SOCIAL_AUTH_VK_OAUTH2_KEY = os.environ['SOCIAL_AUTH_VK_OAUTH2_KEY']
            print("SOCIAL_AUTH_VK_OAUTH2_KEY обанружен в системных переменных")

            SOCIAL_AUTH_VK_OAUTH2_SECRET = os.environ['SOCIAL_AUTH_VK_OAUTH2_SECRET']
            print("SOCIAL_AUTH_VK_OAUTH2_SECRET обанружен в системных переменных")

        except:

            print("Поиск SECRET_KEY и ссылки на бд в системных переменных...")

