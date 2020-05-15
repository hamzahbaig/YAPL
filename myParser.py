
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
    calc : expression
        | var_declaration
        | empty
    '''
    print("TREE ->", p[1])
    print(run(p[1]))


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


def p_bracket_expression(p):
    '''
    expression : LRB expression MULTIPLY expression RRB
                | LRB expression DIVIDE expression RRB
                | LRB expression PLUS expression RRB
                | LRB expression MINUS expression RRB
                | LRB expression POWER expression RRB
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
    expression : FALSE
                | TRUE
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
        elif p[0] == "^":
            return run(p[1]) ** run(p[2])
        elif p[0] == "++":
            ans = run(p[1])
            if p[1][0] == "var":
                ans += 1
                variableValues[p[1][1]]["value"] = ans
                return ans
            elif p[1][0] == "const":
                ans += 1
                return ans
        elif p[0] == "--":
            ans = run(p[1])
            if p[1][0] == "var":
                ans -= 1
                variableValues[p[1][1]]["value"] = ans
                return ans
            elif p[1][0] == "const":
                ans -= 1
                return ans
        elif p[0] == '=':
            if p[2] not in variableValues:
                variableValues[p[2]] = {"type": p[1], "value": run(p[3])}
            else:
                return "Redeclaration Error"
        elif p[0] == 'var':
            if p[1] not in variableValues:
                return "Undeclared Variable Found"
            else:
                return variableValues[p[1]]['value']
        elif p[0] == "const":
            return p[1]
        elif p[0] == "bool":
            return p[1]
        elif p[1] == "print":
            tobePrinted = ""
            for arg in p[2]:
                tobePrinted += str(run(arg)) + " "
            print(tobePrinted)

    else:
        return p


parser = yacc.yacc()
