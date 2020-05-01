
import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)


def p_calc(p):
    '''
    calc : expression
        | var_assign
        | empty
    '''
    print(p[1])


######## STANDARD OUTPUT ##########

def p_expression_print(p):
    '''
    expression : PRINT LRB expression RRB
    '''
    p[0] = ('print', p[3])


def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_expression(p):
    '''
    expression : expression MULTIPLY expression
                | expression DIVIDE expression 
                | expression PLUS expression
                | expression MINUS expression

    '''
    p[0] = (p[2], p[1], p[3])


def p_expression_int_float_string(p):
    '''
    expression : INT
              | FLOAT
              | STRING
    '''
    p[0] = p[1]


def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])


def p_empty(p):
    '''
    empty : 

    '''
    p[0] = None


def p_error(p):
    print("Syntax Error Found")


variableValues = {}


def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            variableValues[p[1]] = run(p[2])
        elif p[0] == 'var':
            if p[1] not in variableValues:
                return "Undeclared Variable Found"
            else:
                return variableValues[p[1]]

    else:
        return p


parser = yacc.yacc()
