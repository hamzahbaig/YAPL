import ply.lex as lex
import ply.yacc as yacc
import sys


tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'EQUALS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE'
]

#  Name should be same as tokens above.

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='

t_ignore = r' '


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NAME(t):
    r'[a-zA-z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE')
)

def p_calc(p):
    '''
    calc : expression
        | empty
    '''
    print("HAMZAH")
    print(p[1])


def p_empty(p):
    '''
    empty : 

    '''
    p[0] = None

def p_expression(p):
    '''
    expression : expression MULTIPLY expression
                | expression DIVIDE expression 
                | expression PLUS expression
                | expression MINUS expression

    '''
    print("BAIG")
    p[0] = (p[2],p[1],p[3])


def p_expression_int_float(p):
    '''
    expression : INT
              | FLOAT

    '''
    p[0] = p[1]


parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)
