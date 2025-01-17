from core.application import BaseApplication
import time

class Application(BaseApplication):
    """menu"""

    def __init__(self, name, hal, server, manager):
        super().__init__(name, hal, server, manager)
        # self.requires["ball"] = ["balls"]
        self.requires["hand_pose"] = ["raw_data"]
        self.requires["hand_sign"] = ["sign"]
        self.time = 0

    def listener(self, source, event, data):
        super().listener(source, event, data)
        
        if source == "hand_sign" and event == "sign" and data is not None:
            self.hand_pose_data["hands_sign"] = data
            # self.server.send_data(self.name, self.hand_pose_data)
            
        if source == "hand_pose" and event == "raw_data" and data is not None:
            self.hand_pose_data = data
            self.server.send_data(self.name, self.hand_pose_data)
