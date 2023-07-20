import configparser
from googleapiclient.discovery import build


class Configurator:
    file_config = 'config.ini'

    config = configparser.ConfigParser()
    config.read(file_config)

    api_key = config['api-key']['api_key']

    service = build('youtube', 'v3', developerKey=api_key)
