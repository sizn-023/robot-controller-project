import pytest
from robot_controller import RobotController

@pytest.mark.smoke

def test_initial_state():
    """测试机器人初始状态"""
    robot = RobotController()

    assert robot.status == "idle"
    assert robot.battery == 100


def test_start_robot():
    """测试机器人启动功能"""
    robot = RobotController()

    result = robot.start()

    assert result == "机器人启动成功"
    assert robot.status == "running"


def test_move_robot():
    """测试机器人正常移动"""
    robot = RobotController()
    robot.start()

    result = robot.move(5)

    assert "机器人移动了5米" in result
    assert robot.battery == 95


def test_move_before_start():
    """测试机器人未启动时执行移动指令"""
    robot = RobotController()

    result = robot.move(5)

    assert "未启动" in result
    assert robot.battery == 100


def test_stop_robot():
    """测试机器人停止功能"""
    robot = RobotController()
    robot.start()

    result = robot.stop()

    assert result == "机器人已停止"
    assert robot.status == "idle"


def test_move_distance_invalid():
    """测试非法移动距离"""
    robot = RobotController()
    robot.start()

    result = robot.move(0)

    assert result == "移动距离必须大于0"
    assert robot.battery == 100



def test_move_zero_distance():
    """测试移动距离为0时，机器人应拒绝执行"""

    robot = RobotController()
    robot.start()

    result = robot.move(0)

    assert result == "移动距离必须大于0"
    assert robot.battery == 100


def test_move_negative_distance():
    """测试移动距离为负数时，机器人应拒绝执行"""

    robot = RobotController()
    robot.start()

    result = robot.move(-1)

    assert result == "移动距离必须大于0"
    assert robot.battery == 100


def test_move_consumes_correct_battery():
    robot = RobotController()

    robot.start()
    result = robot.move(5)

    assert result == "机器人移动了5米，剩余电量:95%"
    assert robot.battery == 95


import pytest

@pytest.mark.parametrize(
        "distance, expected_battery",
        [
            (1, 99),
            (5, 95),
            (10, 90),
            (20, 80),
        ],
    )
def test_move_battery_parameterized(distance, expected_battery):
        """验证不同移动距离对应的电量变化"""
        robot = RobotController()
        robot.start()

        robot.move(distance)

        assert robot.battery == expected_battery

def test_move_consumes_one_percent_per_meter():
    robot = RobotController()
    robot.start()

    robot.move(1)
    assert robot.battery == 99

def test_bug_battery_consumption():
    """验证机器人移动5米后，电量应该剩余95%"""
    robot = RobotController()
    robot.start()
    robot.move(5)
    assert robot.battery == 95

def test_can_use_auto_pendant_fixture(auto_pendant):
    assert auto_pendant.mode == "auto"





