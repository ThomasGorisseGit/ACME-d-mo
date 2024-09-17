from .Types import ResourceTypes, JSON

class Resource:
    """Generic class for resources"""
    def __init__(self, rn:str, originator:str, path:str, ty:ResourceTypes):
        self.rn:str = rn
        self.originator :str = originator
        self.path :str = path
        self.ty : ResourceTypes = ty  
    
    def body(self) -> JSON:
        return {}  
    
class AE(Resource):
    """Create an Application Entity"""
    def __init__(self, rn:str, path:str = "cse-in"):
        super().__init__(rn, f'C{rn}', path, ResourceTypes.AE)
    
    def body(self)-> JSON:
        return {
            "m2m:ae": {
                "api": f"N{self.rn}",
                "rr": True,
                "rn": self.rn,
                "srv": ["3"],
            }
        }
class CNT(Resource):
    """Create a Container"""
    def __init__(self, rn:str, path:str = "cse-in", originator:str = "CAdmin"):
        super().__init__(rn, originator, path, ResourceTypes.CNT)
    
    def body(self)->JSON:
        return  {
            "m2m:cnt": {
            "rn": self.rn,
            }
        }

class SUB(Resource):
    """Create a Subscription (it send requests to a given URL)"""
    def __init__(self, rn:str, path:str = "cse-in", originator:str = "CAdmin", url:str = "http://localhost:8080"):
        super().__init__(rn, originator, path, ResourceTypes.SUB)
        self.nu = url
        
    def body(self)->JSON:
        return {
            "m2m:sub": {
                "rn": self.rn,
                "nu": [self.nu],
                "enc": {
                    "net": [3]
                }
            }
        }
        
class CIN(Resource):
    """Create a Content Instance: it stores the data in a [con] field """
    def __init__(self, rn:str, path:str = "cse-in", originator:str = "CAdmin", content:JSON = {}):
        super().__init__(rn, originator, path, ResourceTypes.CIN)
        self.content = content
    
    def body(self):
        return {
            "m2m:cin": {
                "rn": self.rn,
                "con": str(self.content)    # Support only plain text, so we stringify a JSON object
            }
        }