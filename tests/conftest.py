
import pytest
from teach_pendant import TeachPendant


@pytest.fixture(scope="function")
def auto_pendant():
    print(">>> 创建 auto_pendant fixture")
    pendant = TeachPendant()
    pendant.switch_mode("auto")
    yield pendant
    print(">>> 清理 auto_pendant fixture")
    pendant.switch_mode("auto")

