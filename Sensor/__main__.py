from .Services import SensorManager
if __name__ == "__main__":
    
    sensor_manager = SensorManager()
    
    sensor_manager.create_sensor("Temperature")
    sensor_manager.create_sensor("Humidity")
    
    sensor_manager.generate_data()
    user_input = input("Press Enter to stop the sensors")
    if user_input == "":
        print("Stopping sensors")
        sensor_manager.stop_all_sensors()
        print("Sensors stopped")
        print("Deleting sensors")
        sensor_manager.delete_all_sensors()    
        print("Sensors deleted")