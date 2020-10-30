"""
Engine
"""
from lexer  import Lexer

class Printer:
    
    def __init__(self):
        self.feed_rate = None 
    
    def print_model(self, file):
        self.lexer = Lexer(file)
        self.ast = self.lexer.get_ast()
        for command in self.ast:
            command.execute()
            print(command.parameters)
            
printer = Printer()
printer.print_model('g-code_test.txt')