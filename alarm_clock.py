class AlarmClock:
    def __init__(self):
        self.current_time = ""
        self.alarm_on_or_off = False
        self.alarm_set_time = ""
    
    def set_time(self, string):
        self.current_time = string
        print(self.current_time)

    def set_alarm_on_or_off(self, boolean):
        self.alarm_on_or_off == boolean
    
    def set_alarm_time(self, string):
        self.alarm_set_time = string
        print(self.alarm_set_time)