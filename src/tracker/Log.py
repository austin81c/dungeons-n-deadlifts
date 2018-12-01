import datetime


class Log:
    def __init__(self):
        self.description = "Default Log"
        self.log_items = []

    def log_event(self, log_item):
        self.log_items.append(log_item)
        print("Logged new event:", log_item.description)

class LogItem:
    def __init__(self, dxd_skill, irl_type, duration, description):
        self.timestamp = datetime.datetime
        self.dxd_skill = dxd_skill
        self.irl_type = irl_type
        self.duration = duration
        self.description = description