import random
from ..Data.Types import HTTPMethods, Operation, JSON, ResourceTypes
from ..Data.Resources import Resource
from ..config import ACME_URL
from requests import request, Response
class Sender:
    def __init__(self):
        self.acme_url = ACME_URL
        self.headers: JSON = {}
    def reset_headers(self):
        """There are 3 mandatories headers for each request:
        - X-M2M-Origin: Originator
        - X-M2M-RI: Request identifier
        - X-M2M-RVI: Release version indicator
        """
        self.headers = {
            "Content-Type": "application/json",
            "X-M2M-Origin": "",                            # Originator 
            "X-M2M-RI": str(random.randint(0, 1000)),      # RI: Request identifier -> Random number to identify the request 
            "X-M2M-RVI": "3",                              # RVI: Release version indicator -> 3 is the latest version
        }
        
    def send(self, 
            operation    : Operation,
            resource     : Resource,
            ) -> Response:
        # Reset the headers before sending a new request
        self.reset_headers()
        
        method : HTTPMethods = None
        match operation:
            case Operation.CREATE:
                
                method = HTTPMethods.POST
                
                # to create a resource, we need to specify the type of the resource in the content application field
                self.headers["Content-Type"] = f"application/json;ty={resource.ty.value}" 
                
            case Operation.RETRIEVE:
                method = HTTPMethods.GET
            case Operation.UPDATE:
                method = HTTPMethods.PUT
            case Operation.DELETE:
                method = HTTPMethods.DELETE
            case Operation.NOTIFY:
                method = HTTPMethods.POST
                
        self.headers["X-M2M-Origin"] = resource.originator
        

        response = request(
            method=method.value,
            url=f"{self.acme_url}/{resource.path}",
            headers=self.headers,
            json=resource.body()
            )
        if response.status_code != 201:
            error_format = {eval(response.text)["m2m:dbg"]}
            
            error = f'Error while creating thes resource: {resource.ty.name} \nReason: {error_format} \nCode: {response.status_code}'
            
            print(error)
            raise Exception(error)
        elif resource.ty != ResourceTypes.CIN:  
            print(f'{resource.ty.name} created successfully')
        return response