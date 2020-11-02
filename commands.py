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
    
    def __repr__(self):
        return str((self.name, self.parameters))
        
    def execute(self):
        print(f'execute() hasn\'t been implemented for {self.name} yet')


"""
===============================================================================
G-CODE COMMANDS
===============================================================================


Common Parameter Descriptions (from https://marlinfw.org/docs/gcode/):

    E: The E axis describes the position of the filament in terms of input to
    the extruder feeder.

    F: The maximum movement rate of the move between the start and end point.
    The feedrate set here applies to subsequent moves that omit this parameter.
"""        

        
class G0(Command):
    """
    G0 [E<pos>] [F<rate>] [X<pos>] [Y<pos>] [Z<pos>]
    
    G0 is for linear movement
    """
    pass


class G1(Command):
    """
    G0 [E<pos>] [F<rate>] [X<pos>] [Y<pos>] [Z<pos>]
    
    G1 is for linear movement while extruding
    """
    pass


class G4(Command):
    """
    G4 [P<time in ms>] [S<time in sec>]
    
    G4 is for waiting a few (micro)seconds
    """
    pass


class G12(Command):
    pass
