from app01.wx_robot import robot

if __name__ == '__main__':
    client = robot.client
    client.create_menu({
        'button': [
            {
                'type': 'click',
                'name': '一个按钮',
                'key': 'one'
            },
            {
                'type': 'click',
                'name': '第二个',
                'key': 'two'
            }
        ]
    })
