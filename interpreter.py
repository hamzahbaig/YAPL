
import ply.yacc as yacc
from myParser import parser

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)
