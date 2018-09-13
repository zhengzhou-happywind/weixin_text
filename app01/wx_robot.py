import werobot
from app01 import config

robot = werobot.WeRoBot(token=config.token)


@robot.handler
def hello(message):
    return 'Hello World!'
