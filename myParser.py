
import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUALEQUAL', "NE"),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'POWER'),
    ('right', 'NOT'),
)


def p_calc(p):
    '''
    calc : multiple
        | empty
    '''
    p[0] = ("Tree", p[1])


def p_print_expresion(p):
    '''
    expression : PRINT LRB optargs RRB
    '''
    p[0] = ('call', 'print', p[3])


def p_optargs(p):
    'optargs : args'
    p[0] = p[1]


def p_optargsempty(p):
    'optargs : '
    p[0] = []


def p_args(p):
    'args : expression COMMA args'
    p[0] = [p[1]] + p[3]


def p_args_last(p):  # one argument
    'args : expression'
    p[0] = [p[1]]


def p_var_declaration(p):
    '''
    var_declaration : TYPEINT IDENTIFIER EQUALS expression
                    | TYPEDOUBLE IDENTIFIER EQUALS expression
                    | TYPESTRING IDENTIFIER EQUALS expression
                    | TYPEBOOL IDENTIFIER EQUALS expression
    '''
    p[0] = (p[3], p[1], p[2], p[4])


def p_expression(p):
    '''
    expression : expression MULTIPLY expression
                | expression DIVIDE expression
                | expression PLUS expression
                | expression MINUS expression
                | expression POWER expression
                | expression EQUALEQUAL expression
                | expression NE expression
                | expression LT expression
                | expression LE expression
                | expression GT expression
                | expression GE expression
                | expression AND expression
                | expression OR expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_multiple_lines(p):
    '''
    multiple : expression SEMICOLON multiple
             | var_declaration SEMICOLON multiple
    '''
    p[0] = [p[1]] + p[3]


def p_multiple_empty(p):
    'multiple : '
    p[0] = []


def p_expression_dowhile(p):
    '''
    expression : DO LCB multiple RCB WHILE LRB expression RRB
    '''
    p[0] = ('dowhile', p[7], p[3])



def p_bracket_expression(p):
    '''
    expression : LRB expression MULTIPLY expression RRB
                | LRB expression DIVIDE expression RRB
                | LRB expression PLUS expression RRB
                | LRB expression MINUS expression RRB
                | LRB expression POWER expression RRB
                | LRB expression EQUALEQUAL expression RRB
                | LRB expression NE expression RRB
                | LRB expression LT expression RRB
                | LRB expression LE expression RRB
                | LRB expression GT expression RRB
                | LRB expression GE expression RRB
                | LRB expression AND expression RRB
                | LRB expression OR expression RRB
    '''
    p[0] = (p[3], p[2], p[4])


def p_increment_decrement(p):
    '''
    expression : expression INCREMENT
               | expression DECREMENT 
    '''
    p[0] = (p[2], p[1])


def p_bracket_increment_decrement(p):
    '''
    expression : LRB expression INCREMENT RRB
               | LRB expression DECREMENT RRB
    '''
    p[0] = (p[3], p[2])


def p_expression_int_double_string(p):
    '''
    expression : INT
              | DOUBLE
              | STRING
    '''
    p[0] = ('const', p[1])


def p_expression_bool(p):
    '''
    expression : False
                | True
    '''
    p[0] = ('bool', p[1])


def p_expression_identifier(p):
    '''
    expression : IDENTIFIER
    '''
    p[0] = ('var', p[1])


def p_expression_negate(p):
    '''
    expression : MINUS expression
    '''
    p[0] = ("*", -1, p[2])


def p_not_expression(p):
    '''
    expression : NOT expression
    '''
    p[0] = ("not", p[2])


def p_not_expression_bracket(p):
    '''
    expression : LRB NOT expression RRB
    '''
    p[0] = ("not", p[3])


def p_empty(p):
    '''
    empty :

    '''
    p[0] = None


def p_error(p):
    print("Syntax Error Found")


parser = yacc.yacc()
