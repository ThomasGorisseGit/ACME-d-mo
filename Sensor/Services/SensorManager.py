import threading
from ..Data import Sensor
from ..Data.Types import Operation
class SensorManager:
    def __init__(self):
        self.sensors : list[Sensor] = []
        self.threads: list[threading.Thread] = []

    def create_sensor(self, name):
        sensor = Sensor(name)
        self.sensors.append(sensor)
        sensor.register()
        
    def generate_data(self):
        
        print("\nStart sending data in background\n")
        for sensor in self.sensors:
            thread = threading.Thread(target=sensor.run)
            thread.start()
            self.threads.append(thread)
    
    def stop_all_sensors(self):
        for sensor in self.sensors:
            sensor.running = False
        for thread in self.threads:
            thread.join()
    def delete_all_sensors(self):
        for sensor in self.sensors:
            sensor.unregister()