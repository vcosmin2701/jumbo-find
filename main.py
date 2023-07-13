import configparser
from googleapiclient.discovery import build

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['api-key']['api_key']

service = build('youtube', 'v3', developerKey=api_key)

request = service.channels().list(
    part='statistics',
    forUsername='sentdex'
)

response = request.execute()

print(response)
