from robot_controller import RobotController
def test_initial_state():
    robot = RobotController()
    assert robot.status == "idle"
    assert robot.battery == 100

def test_start_robot():
    robot = RobotController()

    result = robot.start()

    assert result == "机器人启动成功"
    assert robot.status == "running"

def test_move_robot():
    robot = RobotController()
    robot.start()
    result = robot.move(5)
    assert result == "机器人移动了5米，剩余电量:95%"
    assert robot.battery == 95

def test_move_before_start():
    robot = RobotController()
    result = robot.move(5)
    assert result == "机器人未启动，无法移动"
    assert robot.battery == 100

def test_stop_robot():
    robot = RobotController()
    robot.start()
    result = robot.stop()
    assert result == "机器人已停止"
    assert robot.status == "idle"

def test_battery_not_enough():
    robot = RobotController()
    robot.start()
    robot.move(95)
    result = robot.move(10)
    assert result == "电量不足，无法完成移动"
    assert robot.battery == 5

def test_start_with_empty_battery():
    """测试机器人电量耗尽时无法启动"""
    robot = RobotController()

    robot.battery = 0

    result = robot.start()

    assert result == "电量不足，无法启动"
    assert robot.status == "idle"


def test_move_with_insufficient_battery():
    """测试机器人电量不足时无法移动"""
    robot = RobotController()

    robot.start()
    robot.battery = 3

    result = robot.move(5)

    assert result == "电量不足，无法完成移动"
    assert robot.battery == 3