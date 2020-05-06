import ply.lex as lex

reservedWords=(
        'print',
        'return',
)

tokens = (
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'EQUALS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LRB',  # (
    'RRB',  # )
    'PRINT',
    'SEMICOLON',  # ;
    'COMMA',  # ,
    'STRING'
)

#  Name should be same as tokens above.

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='



t_LRB = r'\('
t_RRB = r'\)'
t_SEMICOLON = r';'
t_COMMA = r'\,'
t_ignore = r' '


def t_STRING(t):
	r'"[^"]*"'
	t.value = t.value[1:-1]
	return t


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
