from flask import Flask, request
from ..Data.Encapsuler import Encapsuler

class Consumer:
    """API used to handle the notifications from ACME
    """
    def __init__(self):
        self.app : Flask = Flask(__name__)
        self.setup()
        self.data_encaps = Encapsuler()
        
        self.app.run(
            host="localhost",
            port=5000,
            debug=True
        )
        
    def setup(self):
        self.app.route("/", methods = ["GET"])(self.index)
        self.app.route("/temperature", methods = ["POST"])(self.temperatures)
        self.app.route("/humidity", methods = ["POST"])(self.humidities)
        
    def index(self):
        return {
            "temperatures": self.data_encaps.temperatures,
            "humidities": self.data_encaps.humidities
        }
    
    def temperatures(self):
        temperature = self.handle_m2m_request(request)
        self.data_encaps.add_temperature(
            temperature=temperature
            )
        return {"temperature":temperature}, 201
    
    def humidities(self):
        humidity = self.handle_m2m_request(request)
        self.data_encaps.add_humidity(
            humidity=humidity
            )
        return {"humidity":humidity}, 201
    
    def handle_m2m_request(self, request) -> dict:
        return eval(request.json["m2m:sgn"]["nev"]["rep"]["m2m:cin"]["con"])