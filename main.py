from abc import ABC, abstractmethod
import psutil
import time
from datetime import datetime
from plyer import notification

class Sensor(ABC):
    def __init__(self):
        self.start_time = datetime.now()

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def danger(self, current_val):
        pass

class CpuSensor(Sensor):
    def get_value(self):
        return psutil.cpu_percent(interval=1)
    
    def danger(self, current_val):
        if current_val > 90: return "PLEASE TURN OFF THE PC! IM GONNA EXPLODE!"
        if current_val > 70: return "It's getting heavy in here."
        if current_val > 40: return "CPU is choking, check your background apps."
        return "CPU in good health"

class RamSensor(Sensor):
    def get_value(self):
        return psutil.virtual_memory().percent

    def danger(self, current_val):
        if current_val > 90: return "RAM leak detected! Close some tabs!"
        if current_val > 70: return "Memory is getting crowded."
        return "RAM in good health"

class Notifier:
    def __init__(self, file="monitor_log.txt"):
        self.filename = file

    def send_alert(self, sensor_name, message):
        time = datetime.now()
        log = f"{time} {sensor_name}: {message}"
        
        with open(self.filename, "a") as f:
            f.write(log + "\n")
            
        notification.notify(
            title=f"Ghost: {sensor_name} Alert",
            message=message,
            app_name="Ghost Monitor",
            timeout=5
        )

class Monitor:
    def __init__(self, notifier_obj):
        self.sensors = []
        self.notifier = notifier_obj

    def add_sensor(self, sensor_obj):
        self.sensors.append(sensor_obj)
    
    def start(self):
        print("--- Ghost Monitoring Active ---")
        while True:
            for s in self.sensors:
                val = s.get_value()
                msg = s.danger(val)
                name = type(s).__name__ 
                
                print(f"{name}: {val}% - {msg}")

                if "good health" not in msg.lower():
                    self.notifier.send_alert(name, msg)
            
            time.sleep(1)

if __name__ == "__main__":
    ghost_voice = Notifier()
    mypc = Monitor(ghost_voice)

    cpu_instance = CpuSensor()
    ram_instance = RamSensor()

    mypc.add_sensor(cpu_instance)
    mypc.add_sensor(ram_instance)

    mypc.start()