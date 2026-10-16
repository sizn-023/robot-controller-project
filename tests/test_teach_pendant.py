from teach_pendant import TeachPendant

def test_initial_mode():
    """测试示教器默认处于手动模式"""
    pendant  = TeachPendant()

    assert pendant.mode == "manual"

def test_switch_to_auto():
    """测试切换到自动模式"""
    pendant = TeachPendant()

    result = pendant.switch_mode("auto")

    assert result == "已切换到auto模式"
    assert pendant.mode =="auto"

def test_switch_to_manual():
    """测试切换到手动模式"""
    pendant = TeachPendant()

    result = pendant.switch_mode("manual")

    assert result == "已切换到manual模式"
    assert pendant.mode =="manual"

def test_invalid_mode():
    """测试输入无效模式时拒绝切换"""
    pendant = TeachPendant()

    result = pendant.switch_mode("unknown")

    assert result == "模式无效，请选择 manual 或 auto"
    assert pendant.mode =="manual"


def test_switch_mode_multiple_times():
    """测试多次切换模式后状态是否正确"""
    pendant = TeachPendant()

    result1 = pendant.switch_mode("auto")
    assert result1 == "已切换到auto模式"
    assert pendant.mode == "auto"

    result2 = pendant.switch_mode("manual")
    assert result2 == "已切换到manual模式"
    assert pendant.mode == "manual"

    result3 = pendant.switch_mode("auto")
    assert result3 == "已切换到auto模式"
    assert pendant.mode == "auto"


def test_invalid_mode_keeps_current_mode(auto_pendant):
    result = auto_pendant.switch_mode("unknown")

    assert result == "模式无效，请选择 manual 或 auto"
    assert auto_pendant.mode == "auto"

def test_empty_mode_keeps_current_mode(auto_pendant):
    result = auto_pendant.switch_mode("")

    assert result == "模式无效，请选择 manual 或 auto"
    assert auto_pendant.mode == "auto"

def test_numeric_mode_keeps_current_mode(auto_pendant):
    result = auto_pendant.switch_mode(123)

    assert result == "模式无效，请选择 manual 或 auto"
    assert auto_pendant.mode == "auto"

import pytest

@pytest.mark.parametrize(
    "invalid_mode",
    [
        "unknown",
        "",
        123,
    ],
)
def test_invalid_modes_parameterized(invalid_mode):
    """验证多种非法输入都不会改变当前模式"""
    pendant = TeachPendant()
    pendant.switch_mode("auto")

    result = pendant.switch_mode(invalid_mode)

    assert result == "模式无效，请选择 manual 或 auto"
    assert pendant.mode == "auto"





def test_auto_pendant_fixture_starts_in_auto_mode(auto_pendant):

    assert auto_pendant.mode == "auto"
    auto_pendant.mode = "manual"

def test_auto_pendant_fixture_is_independent(auto_pendant):

    assert auto_pendant.mode == "auto"
