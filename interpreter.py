
import ply.yacc as yacc
from myParser import parser




def makeTree(tree):
    print("Hamzah")

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)
