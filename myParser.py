
import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)


def p_calc(p):
    '''
    calc : expression
        | var_declaration
        | empty
    '''
    print("TREE ->",p[1])


def p_print_expresion(p):
    '''
    expression : PRINT LRB optargs RRB 
    '''
    p[0] = ('call',p[1], p[3])

def p_optargs(p):
    'optargs : args'
    p[0] = p[1]

def p_optargsempty(p):
    'optargs : '
    p[0] = []

def p_args(p):
    'args : expression COMMA args'
    p[0] = [p[1]] + p[3]

def p_args_last(p): #one argument
    'args : expression'
    p[0] = [p[1]]



def p_var_declaration(p):
    '''
    var_declaration : TYPEINT IDENTIFIER EQUALS INT
                    | TYPEDOUBLE IDENTIFIER EQUALS DOUBLE
                    | TYPESTRING IDENTIFIER EQUALS STRING
    '''
    p[0] = (p[3], p[1], p[2], p[4])


def p_expression(p):
    '''
    expression : expression MULTIPLY expression
                | expression DIVIDE expression 
                | expression PLUS expression
                | expression MINUS expression

    '''
    p[0] = (p[2], p[1], p[3])


def p_expression_int_double_string(p):
    '''
    expression : INT
              | DOUBLE
              | STRING
    '''
    p[0] = ('const',p[1])

def p_expression_identifier(p):
    '''
    expression : IDENTIFIER
    '''
    p[0] = ('var',p[1])



def p_empty(p):
    '''
    empty : 

    '''
    p[0] = None


def p_error(p):
    print("Syntax Error Found")


variableValues = {}
toBePrinted = ""

def run(p):
    global toBePrinted
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
        elif p[0] == "print":
            print("SUBCOMMAND",p[1])
            toBePrinted += str(run(p[1]))
            print(toBePrinted)

    else:
        return p
    toBePrinted = ""


parser = yacc.yacc()
