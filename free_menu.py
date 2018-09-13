from app01.wx_robot import robot

client = robot.client
client.create_menu({
    'button': [{
        'type': 'click',
        'name': '一个按钮',
        'key': 'one'
    }]
})
