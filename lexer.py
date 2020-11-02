"""
Reading the g-code file
"""

from commands import Parameter, G0


class Lexer:
    
    def __init__(self, file: str):
        self.file = file
        self.parser = Parser(self.file)
        
    def get_ast(self):
        self.parser.parse_file()
        return self.parser.create_ast()


class Parser:
    """Parser for shit"""
    
    def __init__(self, file):
        self.file = file
        self.token_list = []
        self.ast = []
    
    def parse_file(self):
        with open(self.file, 'r') as gcode:
            for line_raw in gcode:
                # print(line_raw)
                line = line_raw[:-1]  # get rid of \n
                # print(line)
                elements = line.split(' ')
                for element in elements:
                    if element:  # filter out whitespaces
                        # print(element)
                        if element[0] == 'G':
                            kind = 'command'
                        elif element[0] == 'M':
                            kind = 'command'
                        elif element[0] == ';':
                            continue
                        else:
                            kind = 'parameter'
                        self.token_list.append(Token(kind, element))

        # print(self.token_list)
    
    def create_ast(self):
        self.ast = []
        i = 0
        while i < len(self.token_list):
            if self.token_list[i].kind == 'command':
                counter = 0
                while i + counter + 1 < len(self.token_list) and self.token_list[i + counter + 1].kind != 'command':
                    counter += 1
                # print(counter)
                if self.token_list[i].value == 'G0':
                    # print('parameters:', self.token_list[i + 1 : i + counter + 1])
                    self.ast.append(G0(
                            'G0',
                            [Parameter(
                                name=token.value[0], value=float(token.value[1:])
                            ) for token in self.token_list[i + 1:i + counter + 1]]
                            ))
                    i += counter
            i += 1
        # print(self.ast)
        return self.ast


class Token:
    
    def __init__(self, kind: str, value: str):
        self.kind = kind
        self.value = value
    
    def __repr__(self):
        return f'(kind: {self.kind}, value: {self.value}'


lexer = Lexer('g-code_test.txt')
