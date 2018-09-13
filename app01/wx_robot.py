import werobot
from app01 import config

robot = werobot.WeRoBot(token=config.token)
robot.config['APP_ID'] = config.app_id
robot.config['APP_SECRET'] = config.app_secret


@robot.text
def hello(message):
    return 'Hello World!'


@robot.key_click('one')
def click(message):
    return '点击了……'
