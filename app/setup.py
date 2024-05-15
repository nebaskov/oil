import os

PROJECT_PATH = os.getcwd()
DATA_PATH = PROJECT_PATH + '/data/'
PICTURES_PATH = PROJECT_PATH + '/pictures/'

envs = f'{PROJECT_PATH=}\n' \
       f'{DATA_PATH=}\n' \
       f'{PICTURES_PATH=}\n'

with open('.env', 'w') as file:
    file.write(envs)
