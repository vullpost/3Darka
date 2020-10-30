"""
Command class with all needed commands as child classes
"""
from typing import List



class Parameter:
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f'(name: {self.name}, value: {self.value})'


class Command:
    
    def __init__(self, name, parameters: List[Parameter]):
        self.name = name
        self.parameters = parameters
        
    def execute(self):
        print(f'execute() hasn\'t been implemented for {self.name} yet')
        
        
class G0(Command):
    pass