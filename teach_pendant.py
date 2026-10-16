class TeachPendant:
    """模拟工业机器人的示教器"""

    def __init__(self):
        # 默认使用手动模式
        self.mode = "manual"

    def switch_mode(self, mode):
        """切换示教器的操作模式"""
        if mode not in ["manual", "auto"]:
            return "模式无效，请选择 manual 或 auto"

        self.mode = mode
        return f"已切换到{self.mode}模式"
