
import ply.yacc as yacc
from myParser import myParser

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    myParser.parse(s)
