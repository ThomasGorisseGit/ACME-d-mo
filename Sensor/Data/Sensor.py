import random
import time
from datetime import datetime

from .Resources import AE, CNT, SUB, CIN

from ..Services.Sender import Sender
from .Types import Operation
from ..config import MAIN_SERVER_URL
class Sensor:
    def __init__(self, name:str):
        self.name = name
        
        self.sender = Sender()
        
        self.application_entity = None
        self.container = None
        self.subscription = None
        
        self.running = False

    def register(self):
        """Register on ACME :
        Works as a tree :
        
        /Create an Application entity
        -> Create a Container
            --> Create a Subscription 
            --> Insert the Data here
        """
        if self.name is None:
            self.name = random.randint(0, 1000)
            
            
        self.application_entity = AE(
            rn          = f'Sensor_{self.name}',              # rn = Resource Name. It must be unique so we add sensorID to prevent conflicts
            path        = "cse-in"                           # path = where the resource is located. cse-in is the root of the tree 
        )
        # Note that an application entity is creating an originator based on its resource name (rn).
        
        self.container = CNT(
            rn          = f'data_container',              
            originator  = self.application_entity.originator,     # originator = the entity that created the resource
            path        = f'cse-in/{self.application_entity.rn}'  # child of the application entity
        ) 
        # url = application_name to lowercase:
        self.subscription = SUB(
            rn          = f'forward_data',
            originator  = self.application_entity.originator,        
            path        = f'cse-in/{self.application_entity.rn}/{self.container.rn}', 
            url         = f'{MAIN_SERVER_URL}/{self.name.lower()}'           # The latest data inserted is automatically sent to this URL. 
        )
        try :
            self.sender.send(Operation.CREATE, self.application_entity)
            self.sender.send(Operation.CREATE, self.container)
            self.sender.send(Operation.CREATE, self.subscription)
            
        except Exception as e:
            return False
        return True        
    
    def unregister(self):
        """Delete the resources created by the sensor"""
        
        self.application_entity.path = 'cse-in/' + self.application_entity.rn
        # it is recursive, so we need just need to delete the application entity
        try:
            self.sender.send(Operation.DELETE, self.application_entity)
        except Exception as e:
            return False
        return True
    
    
    def run(self):
        self.running = True
        while self.running:
            # Generate data
            data = random.randint(0, 100)
            
            content_instance = CIN(
                rn=f'data_{random.randint(0, 1000)}',         # rn = Resource Name
                path = f'cse-in/{self.application_entity.rn}/{self.container.rn}',
                originator=self.application_entity.originator,
                content={
                        "time":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        "test-result": data
                        }
                
            )
            self.sender.send(Operation.CREATE, content_instance)
            time.sleep(5)
            
    def stop(self):
        self.running = False