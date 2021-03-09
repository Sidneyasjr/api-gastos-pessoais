DEBUG = True

USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DB = 'gerenciamento_flask'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "minha-chave-secreta"
