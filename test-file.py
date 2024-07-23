import unittest
from dignity.lexer_parser import LexerParser

class TestLexerParser(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.sample_code = """
        A: header: | style: 1: #6278 2:#2827 | click: on-time |
        B: h1: | style: must(1: #6278 2:#2827) | click: on-time | $Enforce style definition for B$
        C: body: | style: 1: #6278 2:#2827 | click: on-time |
        D: messages: | style: 1: #6278 2: #2827 | click: on-time |
        Runner: A 1,2,3 | B 1,2,3 | C 1,2,3 | D 1,2,3 |
        """
        self.lexer_parser = LexerParser(self.sample_code)

    def test_tokenize(self):
        self.lexer_parser.tokenize()
        # Check that tokens are not empty
        self.assertNotEqual(len(self.lexer_parser.tokens), 0)
        # Example check: ensure first token is 'HEADER'
        self.assertEqual(self.lexer_parser.tokens[0]['type'], 'HEADER')

    def test_parse(self):
        self.lexer_parser.tokenize()
        self.lexer_parser.parse()
        # Check that AST is not empty
        self.assertNotEqual(len(self.lexer_parser.ast), 0)
        # Example check: ensure AST has specific structure
        self.assertIn('header', self.lexer_parser.ast[0])

    def test_execute(self):
        self.lexer_parser.tokenize()
        self.lexer_parser.parse()
        # Capture the output of the execute method
        with self.assertLogs(level='INFO') as log:
            self.lexer_parser.execute()
            # Check if 'Execution started' is in the logs
            self.assertIn('Execution started', log.output[0])

if __name__ == '__main__':
    unittest.main()
