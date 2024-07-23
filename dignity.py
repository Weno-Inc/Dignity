import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        patterns = {
            'SECTION': r'[A-Z]:',
            'IDENTIFIER': r'\w+:',
            'STYLE': r'style: \d: #[0-9a-fA-F]+ \d: #[0-9a-fA-F]+',
            'CLICK': r'click: \w+-\w+',
            'RUNNER': r'Runner: .*',
            'PIPE': r'\|',
            'COMMENT': r'\$.*?\$'
        }
        for token_type, pattern in patterns.items():
            matches = re.findall(pattern, self.code)
            for match in matches:
                self.tokens.append((token_type, match))

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.ast = []
        self.parse()

    def parse(self):
        current_section = None
        for token_type, value in self.tokens:
            if token_type == 'COMMENT':
                continue  # Skip comments
            if token_type == 'SECTION':
                current_section = value[0]
                self.ast.append((current_section, []))
            elif current_section:
                self.ast[-1][1].append((token_type, value))

# Example usage
code = '''
A: header: | style: 1: #6278 2:#2827 | click: on-time |
B: h1: | style: must(1: #6278 2:#2827) | click: on-time | $ This is a comment $
C: body: | style: 1: #6278 2:#2827 | click: on-time |
D: messages: | style: 1: #6278 2:#2827 | click: on-time |
Runner: A 1,2,3 | B 1,2,3 | C 1,2,3 | D 1,2,3 |
'''

lexer = Lexer(code)
parser = Parser(lexer.tokens)

print(parser.ast)
