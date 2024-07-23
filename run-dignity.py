# run_dignity.py

import sys
from dignity.py import LexerParser

def main():
    if len(sys.argv) != 2:
        print("Usage: <filename>.dig")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)

    lexer_parser = LexerParser(code)
    lexer_parser.tokenize()
    lexer_parser.parse()
    lexer_parser.execute()

if __name__ == "__main__":
    main()
