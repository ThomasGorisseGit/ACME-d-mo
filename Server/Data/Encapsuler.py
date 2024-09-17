class Encapsuler:
    def __init__(self):
        """A Simple class that encapsulates the data
            stores the temperatures and humidities in two different lists
        """
        self.temperatures = []
        self.humidities = []
    
    def add_temperature(self, temperature):
        self.temperatures.append(temperature)
        
    def add_humidity(self, humidity):
        self.humidities.append(humidity)