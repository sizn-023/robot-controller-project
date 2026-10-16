
class RobotController:
    """模拟一个简单机器人控制器"""
    def __init__(self):
        self.status = "idle"
        self.battery = 100

    def start(self):
        """启动机器人"""
        if self.battery <= 0:
            return "电量不足，无法启动"
        self.status = "running"
        return "机器人启动成功"

    def stop(self):
        """停止机器人"""
        self.status = "idle"
        return "机器人已停止"

    def move(self,distance):
        """模拟机器人移动指定距离"""
        if self.status != "running":
            return "机器人未启动，无法移动"
        if distance <= 0:
            return "移动距离必须大于0"
        #每移动1米消耗1%的电量
        if self.battery < distance:
            return "电量不足，无法完成移动"
        self.battery -= distance
        return f"机器人移动了{distance}米，剩余电量:{self.battery}%"


